#!/usr/bin/env python3
"""テンプレートと本文から単元HTML・総合テストHTMLを組み立てる。

CSS は tools/tpl-workbook.html / tools/tpl-vocab.html / tools/tpl-review.html に入っている。
制作するときは本文だけを書けばよく、CSS を触る必要はない。

使い方:
    python tools/build.py workbook 3 this-that-it "This / That / It と指示表現" body.html
    python tools/build.py vocab    3 this-that-it "This / That / It と指示表現" body.html
    python tools/build.py review   1 "第1部　be動詞と名詞" "Unit 1〜4"  body.html
    python tools/build.py review   final "中1の総まとめ"   "Unit 1〜16" body.html

学年を指定するときは --grade を足す（既定は1）。2 なら g2/、3 なら g3/ に出す。

    python tools/build.py --grade 2 workbook 1 past-progressive "過去進行形" body.html
    python tools/build.py --grade 2 vocab    1 past-progressive "過去進行形" body.html

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

# 学年ごとの置き場所（UPDATE-PLAN-g2g3.md「1. 決定したこと」）
GRADE_DIR = {1: "units", 2: "g2", 3: "g3"}

# 部の範囲。中1は UPDATE-PLAN.md「0. 全体方針」のまま、
# 中2・中3は PLAN-g2g3.md「1. 単元数と部の構成」
GRADE_PARTS = {
    1: [(1, 4), (5, 7), (8, 11), (12, 16)],
    2: [(1, 4), (5, 8), (9, 12), (13, 16)],
    3: [(1, 4), (5, 8), (9, 12), (13, 15)],
}
PARTS = GRADE_PARTS[1]


def out_dir(grade: int) -> Path:
    d = ROOT / GRADE_DIR[grade]
    d.mkdir(exist_ok=True)
    return d


def build_review(which: str, name: str, rng: str, body: str, grade: int = 1) -> Path:
    """which は "1"〜"4"（部ごと）か "final"（その学年の総まとめ）。"""
    tpl = (TOOLS / "tpl-review.html").read_text(encoding="utf-8")
    parts = GRADE_PARTS[grade]
    # 単語テストの引数。中1は従来どおり（part=1）、中2以降は学年を含む（part=2-1）
    # PLAN-g2g3.md 5.5：生徒に渡した中1の URL を切らないため
    tag = "" if grade == 1 else "%d-" % grade
    if which == "final":
        tid, wtq = "review-final", "grade=%d" % grade
        fname = "review-final.html"
    else:
        i = int(which)
        if not 1 <= i <= len(parts):
            raise SystemExit("部は 1〜%d か final" % len(parts))
        tid, wtq = "review%02d" % i, "part=%s%d" % (tag, i)
        fname = "review%02d.html" % i
    test = json.dumps({"id": tid, "name": name, "range": rng}, ensure_ascii=False)
    out = (tpl.replace("{{TITLE}}", "総合テスト " + name)
              .replace("{{NAME}}", name)
              .replace("{{RANGE}}", rng)
              .replace("{{WTQ}}", wtq)
              .replace("{{TEST}}", test)
              .replace("{{BODY}}", body))
    dest = out_dir(grade) / fname
    dest.write_text(out, encoding="utf-8")
    return dest


def build(kind: str, n: str, a3: str, a4: str, body_path: str, grade: int = 1) -> Path:
    body = Path(body_path).read_text(encoding="utf-8").strip()

    if kind == "review":
        return build_review(n, a3, a4, body, grade)

    slug, title = a3, a4
    num = int(n)

    if kind == "workbook":
        tpl = (TOOLS / "tpl-workbook.html").read_text(encoding="utf-8")
        out = tpl.replace("{{TITLE}}", f"Unit {num}　{title}").replace("{{BODY}}", body)
        dest = out_dir(grade) / f"unit{num:02d}_{slug}.html"

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
        dest = out_dir(grade) / f"vocab{num:02d}_{slug}.html"

    else:
        raise SystemExit("kind は workbook / vocab / review")

    dest.write_text(out, encoding="utf-8")
    return dest


if __name__ == "__main__":
    argv = sys.argv[1:]
    grade = 1
    if "--grade" in argv:
        i = argv.index("--grade")
        if i + 1 >= len(argv) or argv[i + 1] not in ("1", "2", "3"):
            raise SystemExit("--grade は 1・2・3 のどれか")
        grade = int(argv[i + 1])
        del argv[i:i + 2]
    if len(argv) != 5:
        print(__doc__)
        raise SystemExit(1)
    kind, n, a3, a4, body_path = argv
    p = build(kind, n, a3, a4, body_path, grade)
    print(f"{GRADE_DIR[grade]}/{p.name}  ({p.stat().st_size:,} バイト)")
