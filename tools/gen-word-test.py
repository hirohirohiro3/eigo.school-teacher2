#!/usr/bin/env python3
"""単語帳の見出し語・和訳から word-test.html の語の一覧を機械生成する。

手で語を書き写さない。和訳は <div class="v-sense"> の <p> から取り、
<span class="sub"> の補足は除く。意味が複数ある語は「／」でつなぐ。

2026-10-08 改訂（UPDATE-PLAN-g2g3.md 順18：単語テストに中2の語を足す）
  - 中1（units/）に加えて、単語帳がある学年（g2/、のちに g3/）の語も一覧に足す。
    中1は data-g="1"、中2は data-g="2"。並びは学年→単元→単語帳の順
  - 以前のテンプレート（gen-word-test.tpl.html）は word-test.html の改修
    （目次から直接来たときの選択など）より古いので使わない。word-test.html を
    その場で書きかえる：<ol id="words"> の中身・語数の表示・学年ごとの単元名と部
  - 単元名・部の名前は各学年の目次（index.html・g2/index.html）から取る
  - 語の重複は止めずに報告する（同じ語を別の単元の単語帳でも立てている場合。
    単元の単語テストではその単元の単語帳どおりに出したいので一覧からは外さない）
"""
import re, html, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRADES = {
    1: dict(dir="units", index="index.html", units=16,
            parts=[(1, 4), (5, 7), (8, 11), (12, 16)], sfx=""),
    2: dict(dir="g2", index="g2/index.html", units=16,
            parts=[(1, 4), (5, 8), (9, 12), (13, 16)], sfx="_G2"),
    3: dict(dir="g3", index="g3/index.html", units=15,
            parts=[(1, 4), (5, 8), (9, 12), (13, 15)], sfx="_G3"),
}


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def clean(s):
    s = html.unescape(strip_tags(s))
    s = s.replace("　", " ")
    return re.sub(r"\s+", " ", s).strip()


def entries(path):
    src = path.read_text(encoding="utf-8")
    ol = re.search(r'<ol class="vocab">(.*?)</ol>', src, re.S).group(1)
    out = []
    for li in re.findall(r"<li>(.*?)</li>", ol, re.S):
        m = re.search(r'<span class="v-word">(.*?)</span>', li, re.S)
        if not m:
            continue
        en = clean(m.group(1))
        senses = []
        for sd in re.findall(r'<div class="v-sense">(.*?)</div>', li, re.S):
            pm = re.search(r"<p>(.*?)</p>", sd, re.S)
            if not pm:
                continue
            p = re.sub(r'<span class="sub">.*?</span>', "", pm.group(1), flags=re.S)
            t = clean(p)
            if t:
                senses.append(t)
        out.append((en, "／".join(senses)))
    return out


def js_list(items):
    return ",".join('"%s"' % t.replace("\\", "\\\\").replace('"', '\\"') for t in items)


def main():
    out_path = ROOT / "word-test.html"
    src = out_path.read_text(encoding="utf-8")
    esc = lambda s: html.escape(s, quote=True)

    words = []
    for g, spec in GRADES.items():
        gdir = ROOT / spec["dir"]
        vocab = {n: sorted(gdir.glob(f"vocab{n:02d}_*.html")) for n in range(1, spec["units"] + 1)}
        if not any(vocab.values()):
            continue  # まだ単語帳が無い学年
        idx = (ROOT / spec["index"]).read_text(encoding="utf-8")
        titles = [clean(t) for t in re.findall(r'<span class="u-title">(.*?)</span>', idx)]
        parts = [clean(h) for h in re.findall(r"<h2><span>(.*?)</span></h2>", idx)]
        assert len(titles) == spec["units"], (g, len(titles))
        assert len(parts) == 4, (g, len(parts))

        per_unit = {}
        for n, p in vocab.items():
            if not p:
                continue
            assert len(p) == 1, (g, n, p)
            e = entries(p[0])
            per_unit[n] = len(e)
            words += [(g, n, en, ja) for en, ja in e]
        counts = [sum(per_unit.get(u, 0) for u in range(a, b + 1)) for a, b in spec["parts"]]
        print(f"中{g}: 単元ごと {per_unit}  部 {counts}  合計 {sum(counts)}")

        sfx = spec["sfx"]
        for name, val in ((f"UNITS{sfx}", js_list(titles)),
                          (f"PARTS{sfx}", ",".join("[%d,%d]" % p for p in spec["parts"])),
                          (f"PART_NAMES{sfx}", js_list(parts))):
            pat = re.compile(r"const %s=\[.*?\];" % name, re.S)
            if not pat.search(src):
                sys.exit(f"word-test.html に const {name}=[...] が無い（JS 側の受け皿を先に作る）")
            src = pat.sub(lambda m: f"const {name}=[{val}];", src, count=1)

    seen = {}
    for g, n, en, ja in words:
        seen.setdefault(en.lower(), []).append((g, n, ja))
    for k, v in seen.items():
        if len(v) > 1:
            print("参考：複数の単元の単語帳に同じ見出し語", k, v, file=sys.stderr)

    li = "\n".join(
        f'<li data-g="{g}" data-u="{n}" data-en="{esc(en)}" data-ja="{esc(ja)}"></li>'
        for g, n, en, ja in words)
    src, k = re.subn(r'<ol id="words">.*?</ol>', lambda m: f'<ol id="words">\n{li}\n</ol>', src, count=1, flags=re.S)
    assert k == 1
    src, k = re.subn(r"この教材の語 \d+語をすべて見る", f"この教材の語 {len(words)}語をすべて見る", src, count=1)
    assert k == 1
    out_path.write_text(src, encoding="utf-8")
    print("word-test.html を書き出しました", len(words), "語", out_path.stat().st_size, "バイト")


if __name__ == "__main__":
    main()
