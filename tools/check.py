#!/usr/bin/env python3
"""教材HTMLの自動検証。

使い方:
    python tools/check.py 1                # Unit 1 のワークブックと単語帳を検証
    python tools/check.py 1 --workbook     # ワークブックだけ
    python tools/check.py --all            # 存在する全単元

Playwright が入っていれば、スマホ幅の横スクロールとA4印刷ページ数も見ます。
    pip install playwright && playwright install chromium

2026-09-15 改訂（難度改訂に対応）
  - 「30問固定」をやめ、パート構成（A〜F）と設問数レンジで見る
  - 並べ替えで余分な語を1語混ぜた問題（data-extra="1"）を語数チェックから差し引く
  - 並べ替えの語群が単語単位に割れているかを見る
  - 和訳を出さないと決めたパート（A・C・E）に q-ja が無いかを見る
  - 読解本文の語数と新出語数は「参考」として出すだけで NG にしない
"""

import argparse
import html as htmlmod
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UNITS = ROOT / "units"
MASTER = ROOT / "tools" / "master-vocab.json"

# ---------------------------------------------------------------- 制作基準

# パートごとの設問数レンジ。REVISION-PLAN.md の構成に対応する
PART_SPEC = {
    "A": (3, 6,  "形の確認（4択）"),
    "B": (5, 8,  "語順（並べ替え）"),
    "C": (5, 8,  "誤文訂正"),
    "D": (6, 10, "英作文"),
    "E": (4, 6,  "読解"),
    "F": (2, 3,  "自由記述"),
}
TOTAL_RANGE = (28, 36)

# 和訳（span.q-ja）を出さないパート
NO_JA_PARTS = {"A", "C", "E"}

# 並べ替えの語群は1ブロック1語が原則。まとまりで扱う複合語だけ例外にする
COMPOUND_OK = {
    "video game", "video games",
    "junior high school", "high school",
    "art club", "soccer club", "art room", "music room",
}

# 読解本文の語数のめやす（単元帯ごと）。参考表示のみ
def reading_band(n: int):
    if n <= 2:
        return (40, 60)
    if n <= 6:
        return (60, 80)
    return (80, 120)

# 1単元の新出語数のめやす。参考表示のみ
VOCAB_BAND = (25, 40)

# 見出し語に寄せられない不規則な形は、ここに書き足していく
IRREGULAR = {
    "am": "be", "is": "be", "are": "be", "was": "be", "were": "be",
    "his": "his", "her": "her", "its": "its",
    "children": "child", "men": "man", "women": "woman",
    "feet": "foot", "teeth": "tooth", "people": "people",
    "went": "go", "had": "have", "did": "do", "said": "say",
    "got": "get", "saw": "see", "ate": "eat", "made": "make",
}

CONTRACTIONS = {
    "i'm": ["i", "be"], "you're": ["you", "be"], "he's": ["he", "be"],
    "she's": ["she", "be"], "it's": ["it", "be"], "we're": ["we", "be"],
    "they're": ["they", "be"], "that's": ["that", "be"],
    "don't": ["do", "not"], "doesn't": ["do", "not"], "isn't": ["be", "not"],
    "aren't": ["be", "not"], "can't": ["can", "not"], "cannot": ["can", "not"],
    "wasn't": ["be", "not"], "weren't": ["be", "not"], "let's": ["let", "us"],
}

# 基本語リストに載せる語。単元の単語帳には出さない
BASIC = set("""
i you he she it we they me him us them my your his her its our their
mine yours hers ours theirs be am is are was were do does did don't doesn't
a an the and but or so not very too also now here there well
in on at to for with from of under about
what who whose which where when why how
one two three four five six seven eight nine ten
""".split())


def strip_tags(s: str) -> str:
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return htmlmod.unescape(s)


def words_of(text: str):
    return re.findall(r"[A-Za-z][A-Za-z']*", text)


def lemma(w: str):
    """語をできるだけ見出し語に寄せる。戻り値は候補のリスト。"""
    w = w.lower().strip("'")
    if w in CONTRACTIONS:
        return CONTRACTIONS[w]
    if w in IRREGULAR:
        return [IRREGULAR[w]]
    out = {w}
    if w.endswith("'s"):
        out.add(w[:-2])
    if w.endswith("ies") and len(w) > 4:
        out.add(w[:-3] + "y")
    if w.endswith("es") and len(w) > 3:
        out.add(w[:-2])
    if w.endswith("s") and not w.endswith("ss") and len(w) > 2:
        out.add(w[:-1])
    if w.endswith("ing") and len(w) > 5:
        out.add(w[:-3])
        out.add(w[:-3] + "e")
        out.add(w[:-4])
    if w.endswith("ed") and len(w) > 4:
        out.add(w[:-2])
        out.add(w[:-1])
    return sorted(out)


def build_corpus(wsrc: str):
    """ワークブック本文を、2択と空欄を吸収できるトークン列にする。

    2択「( am / is )」はどちらでも一致する集合に、空欄「(　　　)」は
    任意の1語に一致するワイルドカードにする。図解のように語が別要素へ
    分かれている箇所も、日本語を落とせば語順どおりに並ぶ。
    """
    body = wsrc.split("<body>", 1)[-1]
    body = re.sub(r'<span class="q-ja">.*?</span>', " ", body, flags=re.S)
    text = strip_tags(body)

    tokens = []
    pos = 0
    for m in re.finditer(r"[(（]([^()（）]*)[)）]", text):
        tokens += [{w.lower()} for w in words_of(text[pos:m.start()])]
        inner = m.group(1)
        alts = words_of(inner)
        if "/" in inner and len(alts) >= 2:
            tokens.append({w.lower() for w in alts})
        elif not alts or re.fullmatch(r"[\s　①-⑳]*", inner):
            tokens.append(None)          # 空欄 = 任意の1語
        else:
            tokens += [{w.lower()} for w in alts]
        pos = m.end()
    tokens += [{w.lower()} for w in words_of(text[pos:])]
    return tokens


def corpus_has(tokens, sent_words):
    """例文の語列が、トークン列のどこかに現れるか。"""
    if not sent_words:
        return True
    target = [w.lower() for w in sent_words]
    n = len(target)
    for i in range(len(tokens) - n + 1):
        for j in range(n):
            slot = tokens[i + j]
            if slot is not None and target[j] not in slot:
                break
        else:
            return True
    return False


def load_master():
    if MASTER.exists():
        return json.loads(MASTER.read_text(encoding="utf-8"))
    return {"units": {}}


def find_file(prefix: str, n: int):
    hits = sorted(UNITS.glob(f"{prefix}{n:02d}_*.html"))
    return hits[0] if hits else None


# ---------------------------------------------------------------- ワークブック

def collect_questions(body: str):
    """(パート記号, li の中身) の並びを、本文に現れた順で返す。"""
    out = []
    for m in re.finditer(r'<ol class="q"([^>]*)>(.*?)</ol>', body, re.S):
        attrs, blk = m.group(1), m.group(2)
        pm = re.search(r'data-part="([A-F])"', attrs)
        part = pm.group(1) if pm else None
        for li in re.findall(r"<li([^>]*)>(.*?)</li>", blk, re.S):
            out.append((part, li[0], li[1]))
    return out


def check_workbook(path: Path, n: int, report: list):
    src = path.read_text(encoding="utf-8")
    body = src.split("<body>", 1)[-1]

    items = collect_questions(body)
    questions = [t[2] for t in items]

    answers = []
    for m in re.finditer(r'<ol class="a"[^>]*>(.*?)</ol>', body, re.S):
        answers += re.findall(r"<li[^>]*>(.*?)</li>", m.group(1), re.S)

    # --- パート構成
    nopart = sum(1 for t in items if t[0] is None)
    if nopart:
        report.append((False, f"設問のパート指定　{nopart}問に data-part がありません"
                              '（<ol class="q" data-part="A"> の形で指定する）'))
    else:
        report.append((True, "設問のパート指定　全問にあり"))

    counts = {}
    for part, _, _ in items:
        if part:
            counts[part] = counts.get(part, 0) + 1

    bad_parts = []
    for p, (lo, hi, name) in PART_SPEC.items():
        c = counts.get(p, 0)
        if not (lo <= c <= hi):
            bad_parts.append(f"  {p} {name}: {c}問（{lo}〜{hi}問が正）")
    report.append((not bad_parts, "パートごとの設問数"
                   + ("" if not bad_parts else "\n" + "\n".join(bad_parts))))

    lo, hi = TOTAL_RANGE
    total_ok = lo <= len(questions) <= hi
    report.append((total_ok, f"設問数の合計 {len(questions)}問（{lo}〜{hi}問が正）"))

    report.append((len(answers) == len(questions),
                   f"解答 {len(answers)}問（設問数 {len(questions)} と一致すること）"))

    # --- 並べ替え：語群が単語単位か
    chunk_bad = []
    for i, (part, attrs, q) in enumerate(items):
        if part != "B":
            continue
        text = strip_tags(q)
        m = re.search(r"\[(.+?)\]", text, re.S)
        if not m:
            continue
        for chunk in m.group(1).split("/"):
            c = re.sub(r"\s+", " ", chunk).strip()
            if not c:
                continue
            if len(words_of(c)) > 1 and c.lower() not in COMPOUND_OK:
                chunk_bad.append(f"  {i+1:02d}: 「{c}」が2語以上")
    report.append((not chunk_bad, "並べ替えの語群が単語単位"
                   + ("" if not chunk_bad else "\n" + "\n".join(chunk_bad))))

    # --- 並べ替え：選択肢の語数と正解文の語数（余分な語は差し引く）
    mismatches = []
    for i, (part, attrs, q) in enumerate(items):
        text = strip_tags(q)
        m = re.search(r"\[(.+?)\]", text, re.S)
        if not m:
            continue
        inside = words_of(m.group(1))
        outside = words_of(text[m.end():])
        if i >= len(answers):
            continue
        key = re.search(r'<span class="a-key">(.*?)</span>', answers[i], re.S)
        if not key:
            continue
        ans = words_of(strip_tags(key.group(1)))
        em = re.search(r'data-extra="(\d+)"', attrs)
        extra = int(em.group(1)) if em else 0
        if len(inside) + len(outside) - extra != len(ans):
            mismatches.append(
                f"  {i+1:02d}: 選択肢{len(inside)}+外{len(outside)}−余分{extra}語 ≠ 正解{len(ans)}語")
    report.append((not mismatches, "並べ替えの語数一致"
                   + ("" if not mismatches else "\n" + "\n".join(mismatches))))

    # --- 和訳を出さないパートに q-ja が無いか
    ja_bad = []
    for i, (part, attrs, q) in enumerate(items):
        if part in NO_JA_PARTS and 'class="q-ja"' in q:
            ja_bad.append(f"  {i+1:02d}（パート{part}）")
    report.append((not ja_bad, "和訳を出さないパート（A・C・E）に和訳なし"
                   + ("" if not ja_bad else "\n" + "\n".join(ja_bad))))

    # --- 読解本文の語数（参考）
    reads = re.findall(r'<div class="reading">(.*?)</div>', body, re.S)
    if reads:
        wc = len(words_of(strip_tags(reads[0])))
        blo, bhi = reading_band(n)
        report.append((True, f"［参考］読解本文 {wc}語（めやす {blo}〜{bhi}語）"))
    else:
        report.append((True, "［参考］読解本文が見つかりません"))

    # --- 出題に使った語が解説パートに出ているか（参考）
    split = body.find('class="page-break"')
    explain = set()
    if split > 0:
        for w in words_of(strip_tags(body[:split])):
            explain.update(lemma(w))
    unseen = set()
    for q in questions:
        for w in words_of(strip_tags(q)):
            if w.lower() in BASIC:
                continue
            if not (set(lemma(w)) & explain):
                unseen.add(w.lower())
    report.append((True, f"［参考］解説に出ていない出題語 {len(unseen)}語"
                   + (f"　{', '.join(sorted(unseen))}" if unseen else "")))
    return questions, answers


# ------------------------------------------------------------------- 単語帳

def check_vocab(vpath: Path, wpath: Path, n: int, report: list):
    vsrc = vpath.read_text(encoding="utf-8")
    wsrc = wpath.read_text(encoding="utf-8")

    heads = [strip_tags(h).strip().lower()
             for h in re.findall(r'<span class="v-word">(.*?)</span>', vsrc, re.S)]
    vlo, vhi = VOCAB_BAND
    report.append((len(heads) > 0, f"見出し語 {len(heads)}語"))
    if heads and not (vlo <= len(heads) <= vhi):
        report.append((True, f"［参考］新出語がめやす（{vlo}〜{vhi}語）から外れています"))

    dup = sorted({h for h in heads if heads.count(h) > 1})
    report.append((not dup, "見出し語の重複なし" + ("" if not dup else f"　{', '.join(dup)}")))

    # 既出語（Unit 1..N-1）
    master = load_master()
    known = set(BASIC)
    for k, v in master.get("units", {}).items():
        if int(k) < n:
            known.update(w.lower() for w in v)

    covered = set()
    for h in heads:
        for w in words_of(h):
            covered.update(lemma(w))
    for h in known:
        for w in words_of(h):        # 熟語は語ごとにばらして数える
            covered.update(lemma(w))

    # ワークブック本文の全語がカバーされているか
    #   誤答例（×の行・打ち消し線）は意図的な誤りなので数えない
    wclean = re.sub(r'<div class="contrast-row bad">.*?</div>', " ", wsrc, flags=re.S)
    wclean = re.sub(r'<span class="strike">.*?</span>', " ", wclean, flags=re.S)
    wbody = strip_tags(wclean.split("<body>", 1)[-1])
    proper = set(re.findall(r"\b[A-Z][a-z]+\b", wbody))  # 人名・地名は除外
    missing = set()
    for w in words_of(wbody):
        if len(w) == 1 and w.lower() not in ("a", "i"):
            continue  # 「-s」「A:」などの断片
        if w in proper and w.lower() not in {x.lower() for x in covered}:
            continue
        if w.lower() in BASIC:
            continue
        if not (set(lemma(w)) & covered):
            missing.add(w.lower())
    report.append((not missing, f"ワークブックの語の網羅　未収録 {len(missing)}語"
                   + (f"\n  {', '.join(sorted(missing))}" if missing else "")))

    # 例文がワークブック本文に実在するか
    corpus = build_corpus(wsrc)
    bad = []
    for ex in re.findall(r'<p class="v-ex">(.*?)</p>', vsrc, re.S):
        m = re.search(r'<span class="en">(.*?)</span>', ex, re.S)
        if not m:
            continue
        sent = re.sub(r"\s+", " ", strip_tags(m.group(1))).strip()
        if not corpus_has(corpus, words_of(sent)):
            bad.append(sent)
    report.append((not bad, f"例文がワークブック本文と一致　不一致 {len(bad)}件"
                   + ("\n  " + "\n  ".join(bad) if bad else "")))

    return heads


# ------------------------------------------------------------------ 表示検証

def check_render(paths, report):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        report.append((True, "表示検証はスキップ（playwright 未導入）"))
        return
    with sync_playwright() as p:
        b = p.chromium.launch()
        for path in paths:
            pg = b.new_page(viewport={"width": 375, "height": 800})
            pg.goto(path.as_uri())
            pg.wait_for_timeout(900)
            sw = pg.evaluate("document.documentElement.scrollWidth")
            report.append((sw <= 375, f"{path.name}　スマホ幅375pxで横スクロールなし（実測 {sw}px）"))
            pdf = path.parent / "_tmp.pdf"
            pg.pdf(path=str(pdf), format="A4", print_background=True, prefer_css_page_size=True)
            pages = len(re.findall(rb"/Type\s*/Page[^s]", pdf.read_bytes()))
            pdf.unlink(missing_ok=True)
            report.append((True, f"{path.name}　印刷 A4 {pages}ページ"))
            pg.close()
        b.close()


# ---------------------------------------------------------------------- main

def run(n: int, do_wb: bool, do_vocab: bool, do_render: bool):
    print(f"\n=== Unit {n} " + "=" * 44)
    report = []
    rendered = []

    wpath = find_file("unit", n)
    vpath = find_file("vocab", n)

    if do_wb and wpath:
        print(f"[ワークブック] {wpath.name}")
        check_workbook(wpath, n, report)
        rendered.append(wpath)
    elif do_wb:
        report.append((False, f"unit{n:02d}_*.html が見つかりません"))

    if do_vocab and vpath and wpath:
        print(f"[単語帳]      {vpath.name}")
        heads = check_vocab(vpath, wpath, n, report)
        rendered.append(vpath)
        master = load_master()
        master.setdefault("units", {})[str(n)] = heads
        MASTER.parent.mkdir(exist_ok=True)
        MASTER.write_text(json.dumps(master, ensure_ascii=False, indent=1), encoding="utf-8")
    elif do_vocab and not vpath:
        report.append((True, f"vocab{n:02d}_*.html は未作成"))

    if do_render:
        check_render(rendered, report)

    ng = 0
    for ok, msg in report:
        print(("  OK   " if ok else "  NG   ") + msg)
        ng += 0 if ok else 1
    print(f"  ---- {len(report)}項目中 {ng}件 NG")
    return ng


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("unit", nargs="?", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--workbook", action="store_true")
    ap.add_argument("--vocab", action="store_true")
    ap.add_argument("--no-render", action="store_true")
    a = ap.parse_args()

    do_wb = a.workbook or not a.vocab
    do_vo = a.vocab or not a.workbook

    if a.all:
        nums = sorted({int(p.name[4:6]) for p in UNITS.glob("unit??_*.html")})
    elif a.unit:
        nums = [a.unit]
    else:
        ap.error("単元番号か --all を指定してください")

    total = sum(run(n, do_wb, do_vo, not a.no_render) for n in nums)
    print(f"\n合計 NG {total}件")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
