#!/usr/bin/env python3
"""教材HTMLの自動検証。

使い方:
    python tools/check.py 1                # Unit 1 のワークブックと単語帳を検証
    python tools/check.py 1 --workbook     # ワークブックだけ
    python tools/check.py --all            # 存在する全単元
    python tools/check.py --word-test      # word-test.html を単語帳と照合
    python tools/check.py --index          # index.html のボタン・まとめの枠を照合
    python tools/check.py --review 1       # units/review01.html（第1部の総合テスト）
    python tools/check.py --review final   # units/review-final.html（中1の総まとめ）

Playwright が入っていれば、スマホ幅の横スクロールとA4印刷ページ数も見ます。
    pip install playwright && playwright install chromium

2026-09-15 改訂（難度改訂に対応）
  - 「30問固定」をやめ、パート構成（A〜F）と設問数レンジで見る
  - 並べ替えで余分な語を1語混ぜた問題（data-extra="1"）を語数チェックから差し引く
  - 並べ替えの語群が単語単位に割れているかを見る
  - 和訳を出さないと決めたパート（A・C・E）に q-ja が無いかを見る
  - 読解本文の語数と新出語数は「参考」として出すだけで NG にしない

2026-09-22 追記（Unit 16 一般動詞の過去形に対応）
  - 短縮形の表に didn't を足した
  - 過去形 -ied（studied → study）と子音字を重ねた -ed（stopped → stop）を原形に寄せる
  - 語の網羅チェックで、「-ed」「-ght」のような語尾の表記（ハイフンで始まる綴り）を語として数えない

2026-09-25 追記（UPDATE-PLAN.md 工程2）
  - --index を追加。index.html のボタン・各部のまとめの枠を単語帳の実データと照合する

2026-09-26 追記（UPDATE-PLAN.md 工程3）
  - --review N を追加。総合テストの配点・data-unit・模範解答・読解の語数・
    範囲より後の文法の不使用を見る
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
    "didn't": ["do", "not"],
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
    if w.endswith("ied") and len(w) > 4:       # studied → study（y→ied）
        out.add(w[:-3] + "y")
    if w.endswith("ed") and len(w) > 5 and w[-3] == w[-4]:
        out.add(w[:-3])                        # stopped → stop（子音字を重ねる）
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
    # 「-ed」「-ght」のような語尾の表記は語ではないので数えない
    wbody = re.sub(r"(?<![A-Za-z])-[a-z]+", " ", wbody)
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


# -------------------------------------------------------------- 単語テスト

PARTS_SPEC = [(1, 4), (5, 7), (8, 11), (12, 16)]
WORD_TEST = ROOT / "word-test.html"


def _wt_clean(s: str) -> str:
    """タグと実体参照を外し、全角空白と連続空白をつめる。"""
    s = htmlmod.unescape(re.sub(r"<[^>]+>", "", s))
    return re.sub(r"\s+", " ", s.replace("　", " ")).strip()


def vocab_pairs(vpath: Path):
    """単語帳から (見出し語, 和訳) を取り出す。和訳は v-sense の <p> から、
    <span class="sub"> の補足を除いたもの。意味が複数あれば「／」でつなぐ。"""
    src = vpath.read_text(encoding="utf-8")
    m = re.search(r'<ol class="vocab">(.*?)</ol>', src, re.S)
    if not m:
        return []
    out = []
    for li in re.findall(r"<li>(.*?)</li>", m.group(1), re.S):
        w = re.search(r'<span class="v-word">(.*?)</span>', li, re.S)
        if not w:
            continue
        senses = []
        for sd in re.findall(r'<div class="v-sense">(.*?)</div>', li, re.S):
            pm = re.search(r"<p>(.*?)</p>", sd, re.S)
            if not pm:
                continue
            body = re.sub(r'<span class="sub">.*?</span>', "", pm.group(1), flags=re.S)
            t = _wt_clean(body)
            if t:
                senses.append(t)
        out.append((_wt_clean(w.group(1)), "／".join(senses)))
    return out


def check_word_test(report: list):
    if not WORD_TEST.exists():
        report.append((False, "word-test.html が無い"))
        return
    src = WORD_TEST.read_text(encoding="utf-8")

    m = re.search(r'<ol id="words">(.*?)</ol>', src, re.S)
    if not m:
        report.append((False, 'word-test.html に <ol id="words"> が無い'))
        return
    listed = []
    for li in re.findall(r"<li\b[^>]*>", m.group(1)):
        g = re.search(r'data-g="(\d+)"', li)
        u = re.search(r'data-u="(\d+)"', li)
        en = re.search(r'data-en="([^"]*)"', li)
        ja = re.search(r'data-ja="([^"]*)"', li)
        if not (g and u and en and ja):
            report.append((False, f"data 属性が足りない項目がある　{li}"))
            return
        listed.append((int(g.group(1)), int(u.group(1)),
                       htmlmod.unescape(en.group(1)),
                       htmlmod.unescape(ja.group(1))))
    report.append((len(listed) > 0, f"一覧の語数 {len(listed)}語"))

    # 単語帳から作り直したものと突き合わせる
    want = []
    for n in range(1, 17):
        vs = sorted(UNITS.glob(f"vocab{n:02d}_*.html"))
        if not vs:
            continue
        for en, ja in vocab_pairs(vs[0]):
            want.append((1, n, en, ja))

    report.append((len(listed) == len(want),
                   f"語数が単語帳と一致　一覧 {len(listed)}語 / 単語帳 {len(want)}語"))

    missing = [w for w in want if w not in listed]
    extra = [w for w in listed if w not in want]
    report.append((not missing, f"単語帳にあって一覧に無い語 {len(missing)}件"
                   + ("\n  " + "\n  ".join(f"Unit {u} {en} / {ja}" for _, u, en, ja in missing[:20]) if missing else "")))
    report.append((not extra, f"一覧にあって単語帳に無い語 {len(extra)}件"
                   + ("\n  " + "\n  ".join(f"Unit {u} {en} / {ja}" for _, u, en, ja in extra[:20]) if extra else "")))

    # 並び順も単語帳どおりか
    report.append((listed == want, "一覧の並びが単語帳の順と一致"))

    # 重複
    seen = {}
    for g, u, en, ja in listed:
        seen.setdefault(en.lower(), []).append(u)
    dup = {k: v for k, v in seen.items() if len(v) > 1}
    report.append((not dup, f"一覧に重複なし　重複 {len(dup)}件"
                   + ("\n  " + ", ".join(f"{k}(Unit {'/'.join(map(str, v))})" for k, v in dup.items()) if dup else "")))

    # 和訳が空でない
    blank = [(u, en) for _, u, en, ja in listed if not ja.strip()]
    report.append((not blank, f"和訳が空の語 {len(blank)}件"
                   + ("\n  " + ", ".join(f"Unit {u} {en}" for u, en in blank) if blank else "")))

    # 部の定義
    pm = re.search(r"const PARTS=\[(.*?)\];", src, re.S)
    if not pm:
        report.append((False, "PARTS の定義が読めない"))
    else:
        got = [tuple(int(x) for x in p.split(",")) for p in re.findall(r"\[(\d+,\d+)\]", pm.group(1))]
        report.append((got == PARTS_SPEC,
                       f"部の定義が4部で一致　{got}"))
        counts = [sum(1 for _, u, _, _ in listed if a <= u <= b) for a, b in PARTS_SPEC]
        report.append((sum(counts) == len(listed),
                       f"部ごとの語数 {counts}　合計 {sum(counts)}語"))

    # 単元名の数
    um = re.search(r"const UNITS=\[(.*?)\];", src, re.S)
    nu = len(re.findall(r'"(?:[^"\\]|\\.)*"', um.group(1))) if um else 0
    report.append((nu == 16, f"単元名 {nu}件"))

    # 外部読み込みは Google Fonts だけ
    ext = [u for u in re.findall(r'(?:src|href)="(https?://[^"]+)"', src)
           if "fonts.googleapis.com" not in u and "fonts.gstatic.com" not in u]
    report.append((not ext, f"外部読み込みは Google Fonts だけ　ほか {len(ext)}件"
                   + ("\n  " + "\n  ".join(ext) if ext else "")))


def run_word_test():
    print("== word-test.html")
    report = []
    check_word_test(report)
    ng = 0
    for ok, msg in report:
        print(("  OK   " if ok else "  NG   ") + msg)
        ng += 0 if ok else 1
    print(f"  ---- {len(report)}項目中 {ng}件 NG")
    return ng


# ---------------------------------------------------------------- index.html
# 2026-09-25 追記（UPDATE-PLAN.md「3.」工程2）
INDEX = ROOT / "index.html"


def check_index(report: list):
    if not INDEX.exists():
        report.append((False, "index.html が無い"))
        return
    src = INDEX.read_text(encoding="utf-8")

    # JS なし・外部読み込みは Google Fonts だけ
    report.append(("<script" not in src.lower(), "index.html に script が無い（JS なし）"))
    ext = [u for u in re.findall(r'(?:src|href)="(https?://[^"]+)"', src)
           if "fonts.googleapis.com" not in u and "fonts.gstatic.com" not in u]
    report.append((not ext, f"外部読み込みは Google Fonts だけ　ほか {len(ext)}件"))

    # 共通リンクの先頭が単語テスト
    tm = re.search(r'<ul class="tools">\s*<li><a href="([^"]+)"', src)
    report.append((bool(tm) and tm.group(1) == "word-test.html",
                   "共通リンクの先頭が単語テスト（word-test.html）"))

    # 単元カード：ワークブック／単語帳／単語テストの3つ
    cards = re.findall(r'<span class="u-no">Unit (\d+)</span>.*?<p class="u-links three">(.*?)</p>', src, re.S)
    report.append(([int(n) for n, _ in cards] == list(range(1, 17)),
                   f"3つボタンの単元カード {len(cards)}件（Unit 1〜16 の順）"))
    bad = []
    for n, body in cards:
        n = int(n)
        links = re.findall(r'<a class="(\w+)" href="([^"]+)">(.*?)</a>', body)
        kinds = [k for k, _, _ in links]
        if kinds != ["work", "vocab", "test"]:
            bad.append(f"Unit {n} ボタンの並び {kinds}")
            continue
        vs = sorted(UNITS.glob(f"vocab{n:02d}_*.html"))
        vhref, whref, thref = links[1][1], links[0][1], links[2][1]
        if not vs or vhref != f"units/{vs[0].name}":
            bad.append(f"Unit {n} 単語帳のリンク {vhref}")
        else:
            slug = vs[0].name[len("vocabNN_"):]
            if whref != f"units/unit{n:02d}_{slug}":
                bad.append(f"Unit {n} ワークブックのリンク {whref}")
            cnt = len(vocab_pairs(vs[0]))
            wm = re.search(r"(\d+)語", links[1][2])
            if not wm or int(wm.group(1)) != cnt:
                bad.append(f"Unit {n} 単語帳の語数表示 {links[1][2]}（単語帳 {cnt}語）")
        if thref != f"word-test.html?unit={n}":
            bad.append(f"Unit {n} 単語テストのリンク {thref}")
    report.append((not bad, f"単元カードのリンク先・語数 NG {len(bad)}件"
                   + ("\n  " + "\n  ".join(bad) if bad else "")))

    # 各部のまとめの枠
    counts = []
    for a, b in PARTS_SPEC:
        c = 0
        for n in range(a, b + 1):
            vs = sorted(UNITS.glob(f"vocab{n:02d}_*.html"))
            c += len(vocab_pairs(vs[0])) if vs else 0
        counts.append(c)
    for i, (a, b) in enumerate(PARTS_SPEC, 1):
        m = re.search(rf'<div class="review" id="review{i}">(.*?)</div>', src, re.S)
        if not m:
            report.append((False, f"第{i}部のまとめの枠が無い"))
            continue
        body = m.group(1)
        ok_head = f"第{i}部のまとめ" in body and f"Unit {a}〜{b}" in body
        ok_test = f'href="word-test.html?part={i}">単語テスト　{counts[i-1]}語</a>' in body
        rv = UNITS / f"review{i:02d}.html"
        if rv.exists():
            ok_rev = f'href="units/review{i:02d}.html"' in body
            rev_msg = "総合テストへのリンク"
        else:
            ok_rev = "準備中" in body and f"review{i:02d}.html" not in body
            rev_msg = "総合テストは準備中"
        report.append((ok_head and ok_test and ok_rev,
                       f"第{i}部のまとめ　Unit {a}〜{b}・単語テスト {counts[i-1]}語・{rev_msg}"))
    # 部の枠は各部の単元リストの直後にある
    order = re.findall(r'<ul class="units">|<div class="review" id="review\d">', src)
    report.append((order == ['<ul class="units">', '<div class="review" id="review1">',
                             '<ul class="units">', '<div class="review" id="review2">',
                             '<ul class="units">', '<div class="review" id="review3">',
                             '<ul class="units">', '<div class="review" id="review4">'],
                   "まとめの枠が各部の最後にある"))

    # 中1のまとめ
    m = re.search(r'<div class="review final" id="review-final">(.*?)</div>', src, re.S)
    total = sum(counts)
    if not m:
        report.append((False, "中1のまとめの枠が無い"))
    else:
        body = m.group(1)
        rv = UNITS / "review-final.html"
        ok_rev = ('href="units/review-final.html"' in body) if rv.exists() else ("準備中" in body)
        ok_test = f'href="word-test.html?grade=1">単語テスト　{total}語</a>' in body
        last = src.rfind('<div class="review') == src.find('<div class="review final"')
        report.append((ok_rev and ok_test and last,
                       f"中1のまとめ（最下段）　単語テスト {total}語・総まとめ{'へのリンク' if rv.exists() else 'は準備中'}"))
    report.append(("--ink" in src and re.search(r"\.review\.final\{[^}]*background:var\(--ink\)", src) is not None,
                   "中1のまとめは濃い地（--ink）"))


def run_index():
    print("== index.html")
    report = []
    check_index(report)
    ng = 0
    for ok, msg in report:
        print(("  OK   " if ok else "  NG   ") + msg)
        ng += 0 if ok else 1
    print(f"  ---- {len(report)}項目中 {ng}件 NG")
    return ng


# ---------------------------------------------------------------- 総合テスト
# 2026-09-26 追記（UPDATE-PLAN.md「2. 総合テスト」工程3）

# 大問の配点。和歌山県公立入試の配点から、リスニング25点を文法25点に置き換えたもの
BIG_SPEC = [
    (1, "文法", 25),
    (2, "資料つきの読解", 18),
    (3, "対話文の読解", 21),
    (4, "条件英作文", 10),
    (5, "長文の読解", 26),
]
REVIEW_TOTAL = 100

# 機械で正誤が決まる種類と、ルールで目安の点を付ける種類
AUTO_TYPES = {"choice", "multi", "order", "seq", "fill", "fix"}
WRITTEN_TYPES = {"en", "ja"}

# 部ごとの調整（UPDATE-PLAN.md「2. 中1の範囲で作るための調整」）
# key: 部番号か "final" → (Unit の範囲, 読解本文の語数レンジ, 条件英作文の語数下限)
REVIEW_SPEC = {
    1: ((1, 4), (50, 110), 10),
    2: ((5, 7), (70, 140), 15),
    3: ((8, 11), (80, 160), 20),
    4: ((12, 16), (90, 180), 25),
    "final": ((1, 16), (100, 200), 25),
}

# 「その範囲より後で扱う文法を使っていない」を機械で見るための目安。
# first が範囲の最終 Unit より後なら、その形が本文・選択肢・正解に出てはいけない。
# first=99 は中1で扱わない文法。綴りだけで判断する目安なので、
# 取りこぼしも誤検出もありうる。NG が出たら人の目で確かめて直す。
# 4つ目は「拾わない語」。be動詞＋-ing形に見える形容詞（is interesting）など、
# 綴りだけでは見分けられない語をここで外す。
LATER_GRAMMAR = [
    (3,  "this / that / these / those", r"\b(this|that|these|those)\b"),
    (6,  "一般動詞の否定文・疑問文（do / does）", r"\b(don't|doesn't|do not|does not|do you|do they|do we|does he|does she)\b"),
    (8,  "目的格・所有代名詞", r"\b(him|us|them|mine|yours|hers|ours|theirs)\b"),
    (10, "疑問詞", r"\b(what|who|whose|which|where|when|why|how)\b"),
    (12, "命令文・Let's", r"\blet's\b"),
    (13, "助動詞 can", r"\bcan(not|'t)?\b"),
    (14, "現在進行形", r"\b(am|is|are|'m|'re)\s+\w+ing\b",
     {"interesting", "exciting", "boring", "surprising", "amazing", "tiring",
      "relaxing", "charming", "willing", "morning", "evening", "spring",
      "everything", "something", "anything", "nothing", "during", "nursing"}),
    (15, "be動詞の過去形", r"\b(was|were|wasn't|weren't)\b"),
    (16, "一般動詞の過去形", r"\b(went|did|didn't|saw|ate|made|got|took|came|said|wrote|bought|played|visited|watched|enjoyed|studied|walked|cooked|helped|cleaned|looked|talked|listened|opened|started|stopped|lived|liked|wanted|worked|called|asked|used|needed)\b"),
    (99, "不定詞", r"\bto\s+(go|be|play|see|do|eat|study|visit|make|get|help|write|buy|take|come|meet|watch|use|learn|start|live|talk|speak|drink|run|swim|sing|walk|work|know|find|give|show|call|ask|open|listen)\b"),
    (99, "動名詞", r"\b(enjoy|enjoys|like|likes|start|starts|begin|begins|finish|finishes|stop|stops|practice|practices)\s+\w+ing\b"),
    (99, "比較", r"(\bthan\b|\bbetter\b|\bbest\b|\bworse\b|\bworst\b|\bmore\s+\w+|\bmost\s+\w+)"),
    (99, "受動態", r"\b(am|is|are|was|were)\s+\w+(ed|en)\s+by\b"),
    (99, "現在完了", r"\b(have|has|had)\s+(been|\w+ed|\w+en)\b",
     {"red", "bed", "need", "speed", "seed", "ten", "often", "kitchen",
      "children", "open", "garden", "seven", "listen", "when", "then",
      "men", "pen", "green", "hundred", "bread", "salad"}),
    (99, "未来の表し方", r"(\bwill\b|\bgoing to\b)"),
]


def review_path(which):
    return UNITS / ("review-final.html" if which == "final" else "review%02d.html" % int(which))


def _attr(tag: str, name: str):
    m = re.search(r'\s%s="([^"]*)"' % name, tag)
    return htmlmod.unescape(m.group(1)) if m else None


def _paper(src: str) -> str:
    m = re.search(r'<div id="paper">(.*?)\n</div>\s*\n<div class="subbar"', src, re.S)
    return m.group(1) if m else ""


def check_review(which, report: list):
    path = review_path(which)
    label = "review-final.html" if which == "final" else path.name
    if not path.exists():
        report.append((False, f"{label} が無い"))
        return
    src = path.read_text(encoding="utf-8")
    spec = REVIEW_SPEC[which]
    (ua, ub), (ra, rb), min_words = spec

    # 外部読み込みは Google Fonts だけ
    ext = [u for u in re.findall(r'(?:src|href)="(https?://[^"]+)"', src)
           if "fonts.googleapis.com" not in u and "fonts.gstatic.com" not in u]
    report.append((not ext, f"外部読み込みは Google Fonts だけ　ほか {len(ext)}件"))

    body = _paper(src)
    report.append((bool(body), "テンプレートの #paper に本文が入っている"))
    if not body:
        return

    # 大問
    secs = re.findall(r'(<section class="big"[^>]*>)(.*?)</section>', body, re.S)
    got_big = [(int(_attr(t, "data-big") or 0), _attr(t, "data-name") or "", int(_attr(t, "data-pt") or 0))
               for t, _ in secs]
    report.append((len(secs) == len(BIG_SPEC) and [b[0] for b in got_big] == [b[0] for b in BIG_SPEC],
                   f"大問が{len(BIG_SPEC)}つ（data-big 1〜{len(BIG_SPEC)} の順）　実際 {len(secs)}つ"))
    bad = [f"大問{n}（{nm}）{pt}点：計画は{BIG_SPEC[i][2]}点"
           for i, (n, nm, pt) in enumerate(got_big) if i < len(BIG_SPEC) and pt != BIG_SPEC[i][2]]
    report.append((not bad, "大問の配点 25・18・21・10・26"
                   + ("\n  " + "\n  ".join(bad) if bad else "")))

    # 設問。選択肢の <li> と混ざらないよう、data-type を持つ <li> だけを問題として拾い、
    # 次の問題の <li> までをその問題の中身とする
    qs = []
    for tag, inner in secs:
        big = int(_attr(tag, "data-big") or 0)
        ms = list(re.finditer(r'<li[^>]*\sdata-type="[^"]*"[^>]*>', inner))
        for i, m in enumerate(ms, 1):
            end = ms[i].start() if i < len(ms) else len(inner)
            qs.append((big, i, m.group(0), inner[m.end():end]))
    report.append((len(qs) > 0, f"設問 {len(qs)}問"))

    miss = []
    for b, i, t, _ in qs:
        for a in ("data-unit", "data-pt", "data-type"):
            if not _attr(t, a):
                miss.append(f"大問{b}-問{i} に {a} が無い")
    report.append((not miss, f"全設問に data-unit・data-pt・data-type がある　NG {len(miss)}件"
                   + ("\n  " + "\n  ".join(miss[:10]) if miss else "")))

    kinds = sorted({_attr(t, "data-type") for _, _, t, _ in qs} - AUTO_TYPES - WRITTEN_TYPES)
    report.append((not kinds, f"data-type が決めた種類のどれか　ほか {kinds}"))

    # 配点
    total = sum(int(_attr(t, "data-pt") or 0) for _, _, t, _ in qs)
    report.append((total == REVIEW_TOTAL, f"設問の配点合計 {total}点（100点）"))
    bad = []
    for (tag, inner), (n, nm, _) in zip(secs, BIG_SPEC):
        s = sum(int(_attr(t, "data-pt") or 0) for b, i, t, _ in qs if b == n)
        d = int(_attr(tag, "data-pt") or 0)
        if s != d:
            bad.append(f"大問{n} 設問の合計 {s}点 ≠ 大問の {d}点")
    report.append((not bad, "大問ごとの配点と設問の合計が一致"
                   + ("\n  " + "\n  ".join(bad) if bad else "")))

    # Unit が範囲内
    bad = []
    used = set()
    for b, i, t, _ in qs:
        for u in (_attr(t, "data-unit") or "").split():
            if not u.isdigit() or not (ua <= int(u) <= ub):
                bad.append(f"大問{b}-問{i} data-unit={u}")
            else:
                used.add(int(u))
    report.append((not bad, f"data-unit が Unit {ua}〜{ub} の中　NG {len(bad)}件"
                   + ("\n  " + "\n  ".join(bad[:10]) if bad else "")))
    report.append((used == set(range(ua, ub + 1)),
                   f"範囲の Unit がすべて出題に入っている　抜け {sorted(set(range(ua, ub + 1)) - used)}"))

    # 機械採点の問題は正解が要る
    bad = []
    for b, i, t, x in qs:
        ty, a = _attr(t, "data-type"), _attr(t, "data-a")
        if ty in AUTO_TYPES and not a:
            bad.append(f"大問{b}-問{i}（{ty}）に data-a が無い")
            continue
        if ty == "choice":
            n = len(re.findall(r'type="radio"', x))
            if n < 2 or not a.isdigit() or not (1 <= int(a) <= n):
                bad.append(f"大問{b}-問{i} 選択肢{n}個に対して data-a={a}")
        elif ty == "multi":
            n = len(re.findall(r'type="checkbox"', x))
            vs = [v.strip() for v in a.split(",")]
            if len(vs) != 2 or not all(v.isdigit() and 1 <= int(v) <= n for v in vs):
                bad.append(f"大問{b}-問{i} 選択肢{n}個に対して data-a={a}（2つ選ぶ）")
        elif ty == "seq":
            n = len(re.findall(r"<select", x))
            vs = [v.strip() for v in a.split(",")]
            if n < 2 or sorted(vs) != sorted(str(k + 1) for k in range(n)):
                bad.append(f"大問{b}-問{i} select {n}個に対して data-a={a}")
        elif ty == "order":
            ws = re.findall(r"<span>(.*?)</span>", x)
            if not ws:
                bad.append(f"大問{b}-問{i} 並べかえの語群（p.words > span）が無い")
            else:
                for cand in a.split("|"):
                    if len(strip_tags(cand).split()) != len(ws):
                        bad.append(f"大問{b}-問{i} 語群{len(ws)}語と正解「{cand}」の語数が違う")
    report.append((not bad, f"機械採点の問題の正解　NG {len(bad)}件"
                   + ("\n  " + "\n  ".join(bad[:10]) if bad else "")))

    # 判断が要る問題は模範解答と採点の目安が要る
    bad = []
    w_qs = [(b, i, t, x) for b, i, t, x in qs if _attr(t, "data-type") in WRITTEN_TYPES]
    for b, i, t, x in w_qs:
        ty = _attr(t, "data-type")
        if '<p class="model">' not in x:
            bad.append(f"大問{b}-問{i} に模範解答（p.model）が無い")
        if '<p class="rubric">' not in x:
            bad.append(f"大問{b}-問{i} に採点の目安（p.rubric）が無い")
        if ty == "ja" and not _attr(t, "data-kw"):
            bad.append(f"大問{b}-問{i}（ja）に data-kw が無い")
        if ty == "en" and not (_attr(t, "data-kw") or _attr(t, "data-min")):
            bad.append(f"大問{b}-問{i}（en）に data-kw も data-min も無い")
    report.append((bool(w_qs) and not bad,
                   f"判断が要る問題 {len(w_qs)}問に模範解答と採点の目安　NG {len(bad)}件"
                   + ("\n  " + "\n  ".join(bad[:10]) if bad else "")))

    # 条件英作文（大問4）の語数条件
    mins = [_attr(t, "data-min") for b, i, t, _ in qs if b == 4 and _attr(t, "data-type") == "en"]
    report.append((mins == [str(min_words)],
                   f"大問4 条件英作文の語数条件 {mins}（計画は{min_words}語以上）"))

    # 読解本文の語数
    bad = []
    for k, rd in enumerate(re.findall(r'<div class="reading">(.*?)</div>', body, re.S), 1):
        n = len(re.findall(r"[A-Za-z][A-Za-z'\-]*", strip_tags(rd)))
        if not (ra <= n <= rb):
            bad.append(f"読解本文{k} {n}語（目安 {ra}〜{rb}語）")
    report.append((not bad, f"読解本文の語数（目安 {ra}〜{rb}語）　NG {len(bad)}件"
                   + ("\n  " + "\n  ".join(bad) if bad else "")))

    # 後で扱う文法を使っていない
    text = strip_tags(body)
    answers = " ".join(filter(None, [_attr(t, "data-a") for _, _, t, _ in qs]))
    models = " ".join(strip_tags(m) for m in re.findall(r'<p class="model">(.*?)</p>', body, re.S))
    hay = text + " " + answers + " " + models
    bad = []
    for rule in LATER_GRAMMAR:
        first, name, pat = rule[0], rule[1], rule[2]
        stop = rule[3] if len(rule) > 3 else set()
        if first <= ub:
            continue
        hits = sorted({m.group(0).strip() for m in re.finditer(pat, hay, re.I)
                       if m.group(0).split()[-1].lower().strip(".,!?") not in stop})
        if hits:
            where = f"Unit {first} で扱う" if first <= 16 else "中1では扱わない"
            bad.append(f"{name}（{where}）：{ '、'.join(hits[:5]) }")
    report.append((not bad, f"範囲より後の文法を使っていない　NG {len(bad)}件"
                   + ("\n  " + "\n  ".join(bad) if bad else "")))


def run_review(which, do_render=True):
    label = "review-final.html" if which == "final" else "review%02d.html" % int(which)
    print(f"== units/{label}")
    report = []
    check_review(which, report)
    p = review_path(which)
    if do_render and p.exists():
        check_render([p], report)
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
    ap.add_argument("--word-test", action="store_true",
                    help="word-test.html を単語帳と突き合わせる")
    ap.add_argument("--index", action="store_true",
                    help="index.html のボタン・まとめの枠を照合する")
    ap.add_argument("--review", metavar="N",
                    help="総合テストを検査する。N は 1〜4（部ごと）か final（中1の総まとめ）")
    a = ap.parse_args()

    if a.review is not None:
        which = "final" if a.review.lower() == "final" else int(a.review)
        if which not in REVIEW_SPEC:
            ap.error("--review は 1〜4 か final")
        total = run_review(which, not a.no_render)
        print(f"\n合計 NG {total}件")
        sys.exit(1 if total else 0)

    if a.word_test or a.index:
        total = (run_word_test() if a.word_test else 0) + (run_index() if a.index else 0)
        print(f"\n合計 NG {total}件")
        sys.exit(1 if total else 0)

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
