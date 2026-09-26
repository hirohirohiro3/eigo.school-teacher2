#!/usr/bin/env python3
"""テンプレートと本文から単元HTML・総合テストHTMLを組み立てる。

CSS は tools/tpl-workbook.html / tools/tpl-vocab.html / tools/tpl-review.html に入っている。
制作するときは本文だけを書けばよく、CSS を触る必要はない。

使い方:
    python tools/build.py workbook 3 this-that-it "This / That / It と指示表現" body.html
    python tools/build.py vocab    3 this-that-it "This / That / It と指示表現" body.html
    python tools/build.py review   1 "第1部　be動詞と名詞" "Unit 1〜4"  body.html
    python tools/build.py review   final "中1の総まとめ"   "Unit 1〜16" body.html

body.html には <div class="sheet"> の中身だけを書く。
ワークブックは nav とヘッダーも含める。
単語帳は nav とヘッダーを書いたあと、単語リスト（ol.vocab）を続ける。
品詞ガイドと画面下の常駐バーはテンプレート側が自動で入れる。

総合テスト（review）の本文は <section class="big"> だけを並べる。
nav・ヘッダー・提出バー・結果画面・共有のモーダル・JS はテンプレート側が入れる。
設問の属性の書き方は tools/tpl-review.html の冒頭のコメントにある。
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
UNITS = ROOT / "units"

# 部の範囲。UPDATE-PLAN.md「0. 全体方針」の4部のまま
PARTS = [(1, 4), (5, 7), (8, 11), (12, 16)]


def build_review(which: str, name: str, rng: str, body: str) -> Path:
    """which は "1"〜"4"（部ごと）か "final"（中1の総まとめ）。"""
    tpl = (TOOLS / "tpl-review.html").read_text(encoding="utf-8")
    if which == "final":
        tid, wtq = "review-final", "grade=1"
        fname = "review-final.html"
    else:
        i = int(which)
        if not 1 <= i <= len(PARTS):
            raise SystemExit("部は 1〜%d か final" % len(PARTS))
        tid, wtq = "review%02d" % i, "part=%d" % i
        fname = "review%02d.html" % i
    test = json.dumps({"id": tid, "name": name, "range": rng}, ensure_ascii=False)
    out = (tpl.replace("{{TITLE}}", "総合テスト " + name)
              .replace("{{NAME}}", name)
              .replace("{{RANGE}}", rng)
              .replace("{{WTQ}}", wtq)
              .replace("{{TEST}}", test)
              .replace("{{BODY}}", body))
    dest = UNITS / fname
    dest.write_text(out, encoding="utf-8")
    return dest


def build(kind: str, n: str, a3: str, a4: str, body_path: str) -> Path:
    body = Path(body_path).read_text(encoding="utf-8").strip()

    if kind == "review":
        return build_review(n, a3, a4, body)

    slug, title = a3, a4
    num = int(n)

    if kind == "workbook":
        tpl = (TOOLS / "tpl-workbook.html").read_text(encoding="utf-8")
        out = tpl.replace("{{TITLE}}", f"Unit {num}　{title}").replace("{{BODY}}", body)
        dest = UNITS / f"unit{num:02d}_{slug}.html"

    elif kind == "vocab":
        tpl = (TOOLS / "tpl-vocab.html").read_text(encoding="utf-8")
        # 本文を「ヘッダー部」と「単語リスト部」に割る。
        # 品詞ガイドはその境目にテンプレートが差し込む。
        marker = '<h2><span>この単元の新出語'
        if marker not in body:
            raise SystemExit(f"本文に「{marker}…」の見出しが見つかりません")
        i = body.index(marker)
        out = (tpl.replace("{{TITLE}}", f"単語帳 Unit {num}　{title}")
                  .replace("{{HEADER}}", body[:i].rstrip())
                  .replace("{{BODY}}", body[i:]))
        dest = UNITS / f"vocab{num:02d}_{slug}.html"

    else:
        raise SystemExit("kind は workbook / vocab / review")

    dest.write_text(out, encoding="utf-8")
    return dest


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(__doc__)
        raise SystemExit(1)
    kind, n, a3, a4, body_path = sys.argv[1:]
    p = build(kind, n, a3, a4, body_path)
    print(f"{p}  ({p.stat().st_size:,} バイト)")
