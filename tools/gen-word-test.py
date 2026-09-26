#!/usr/bin/env python3
"""units/vocabNN_*.html の見出し語・和訳から word-test.html を機械生成する。

手で語を書き写さない。和訳は <div class="v-sense"> の <p> から取り、
<span class="sub"> の補足は除く。意味が複数ある語は「／」でつなぐ。
"""
import re, glob, html, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = [(1, 4), (5, 7), (8, 11), (12, 16)]


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
        en = clean(m.group(1))
        senses = []
        for sd in re.findall(r'<div class="v-sense">(.*?)</div>', li, re.S):
            p = re.search(r"<p>(.*?)</p>", sd, re.S).group(1)
            p = re.sub(r'<span class="sub">.*?</span>', "", p, flags=re.S)
            senses.append(clean(p))
        out.append((en, "／".join(s for s in senses if s)))
    return out


def main():
    idx = (ROOT / "index.html").read_text(encoding="utf-8")
    titles = re.findall(r'<span class="u-title">(.*?)</span>', idx)
    parts = [clean(h) for h in re.findall(r"<h2><span>(.*?)</span></h2>", idx)]
    assert len(titles) == 16, len(titles)
    assert len(parts) == 4, len(parts)

    words = []
    per_unit = {}
    for n in range(1, 17):
        p = sorted(ROOT.glob(f"units/vocab{n:02d}_*.html"))
        assert len(p) == 1, (n, p)
        e = entries(p[0])
        per_unit[n] = len(e)
        for en, ja in e:
            words.append((n, en, ja))

    dup = {}
    for n, en, ja in words:
        dup.setdefault(en.lower(), []).append(n)
    bad = {k: v for k, v in dup.items() if len(v) > 1}
    if bad:
        print("重複:", bad, file=sys.stderr)
        sys.exit(1)

    part_counts = [sum(per_unit[u] for u in range(a, b + 1)) for a, b in PARTS]
    print("語数:", per_unit, "部:", part_counts, "合計:", len(words))

    esc = lambda s: html.escape(s, quote=True)
    li = "\n".join(
        f'<li data-g="1" data-u="{n}" data-en="{esc(en)}" data-ja="{esc(ja)}"></li>'
        for n, en, ja in words
    )
    units_js = ",".join('"%s"' % t.replace('"', '\\"') for t in titles)
    parts_js = ",".join("[%d,%d]" % p for p in PARTS)
    part_names_js = ",".join('"%s"' % p for p in parts)

    tpl = (Path(__file__).resolve().parent / "gen-word-test.tpl.html").read_text(encoding="utf-8")
    out = (tpl.replace("<!--WORDS-->", li)
              .replace("/*UNITS*/", units_js)
              .replace("/*PARTS*/", parts_js)
              .replace("/*PARTNAMES*/", part_names_js)
              .replace("/*TOTAL*/", str(len(words))))
    (ROOT / "word-test.html").write_text(out, encoding="utf-8")
    print("word-test.html を書き出しました", (ROOT / "word-test.html").stat().st_size, "バイト")


if __name__ == "__main__":
    main()
