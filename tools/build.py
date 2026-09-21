#!/usr/bin/env python3
"""テンプレートと本文から単元HTMLを組み立てる。

CSS は tools/tpl-workbook.html / tools/tpl-vocab.html に入っている。
制作するときは本文だけを書けばよく、CSS を触る必要はない。

使い方:
    python tools/build.py workbook 3 this-that-it "This / That / It と指示表現" body.html
    python tools/build.py vocab    3 this-that-it "This / That / It と指示表現" body.html

body.html には <div class="sheet"> の中身だけを書く。
ワークブックは nav とヘッダーも含める。
単語帳は nav とヘッダーを書いたあと、単語リスト（ol.vocab）を続ける。
品詞ガイドと画面下の常駐バーはテンプレート側が自動で入れる。
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
UNITS = ROOT / "units"


def build(kind: str, n: int, slug: str, title: str, body_path: str) -> Path:
    body = Path(body_path).read_text(encoding="utf-8").strip()

    if kind == "workbook":
        tpl = (TOOLS / "tpl-workbook.html").read_text(encoding="utf-8")
        out = tpl.replace("{{TITLE}}", f"Unit {n}　{title}").replace("{{BODY}}", body)
        dest = UNITS / f"unit{n:02d}_{slug}.html"

    elif kind == "vocab":
        tpl = (TOOLS / "tpl-vocab.html").read_text(encoding="utf-8")
        # 本文を「ヘッダー部」と「単語リスト部」に割る。
        # 品詞ガイドはその境目にテンプレートが差し込む。
        marker = '<h2><span>この単元の新出語'
        if marker not in body:
            raise SystemExit(f"本文に「{marker}…」の見出しが見つかりません")
        i = body.index(marker)
        out = (tpl.replace("{{TITLE}}", f"単語帳 Unit {n}　{title}")
                  .replace("{{HEADER}}", body[:i].rstrip())
                  .replace("{{BODY}}", body[i:]))
        dest = UNITS / f"vocab{n:02d}_{slug}.html"

    else:
        raise SystemExit("kind は workbook か vocab")

    dest.write_text(out, encoding="utf-8")
    return dest


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(__doc__)
        raise SystemExit(1)
    kind, n, slug, title, body_path = sys.argv[1:]
    p = build(kind, int(n), slug, title, body_path)
    print(f"{p}  ({p.stat().st_size:,} バイト)")
