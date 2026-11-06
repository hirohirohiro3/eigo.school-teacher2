#!/usr/bin/env python3
"""学年ごとの「不規則動詞の表」（units/verb-forms.html・g2/verb-forms.html・g3/verb-forms.html）を
ワークブック本文から機械で作る。2026-11-06 ひろの依頼で新設。

- 載せるのは不規則動詞だけ（規則動詞 play → played は載せない。ひろの判断）。
- その学年のワークブック（unitNN_*.html）に、過去形か過去分詞（原形とちがう形）が1回でも
  出てきた動詞を拾う。「初めて出た単元」は、その形が最初に出た単元。
- 中1は 原形・過去形 の2列、中2・中3は 原形・過去形・過去分詞 の3列（ひろの判断）。
- 原形・過去形・過去分詞が同じ形の語（read・let など）は本文からは区別できないので、
  SAME_FORM に単元を手で書く。逆に、動詞でない同じ綴り（left＝左 など）は NOT_VERB で外す。
- JavaScript は使わない。CSS はワークブックの table.rule と同じ。

使い方：python tools/gen-verb-forms.py   （3学年分を書き出す）
"""
import re, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRADES = {1: ("units", "中1", "../index.html"), 2: ("g2", "中2", "index.html"), 3: ("g3", "中3", "index.html")}

# 原形|過去形（／で複数）|過去分詞|意味
IRR = """
be|was/were|been|〜である・いる
have|had|had|持っている・食べる
do|did|done|する
go|went|gone|行く
come|came|come|来る
become|became|become|〜になる
get|got|got/gotten|手に入れる・〜になる
give|gave|given|あたえる
take|took|taken|取る・（乗り物に）乗る
make|made|made|作る
see|saw|seen|見る・会う
eat|ate|eaten|食べる
drink|drank|drunk|飲む
write|wrote|written|書く
read|read|read|読む
speak|spoke|spoken|話す
say|said|said|言う
tell|told|told|伝える・言う
know|knew|known|知っている
think|thought|thought|思う・考える
buy|bought|bought|買う
bring|brought|brought|持ってくる
catch|caught|caught|捕まえる
teach|taught|taught|教える
fight|fought|fought|戦う
meet|met|met|会う
run|ran|run|走る
find|found|found|見つける
hear|heard|heard|聞こえる・聞く
sleep|slept|slept|眠る
sing|sang|sung|歌う
swim|swam|swum|泳ぐ
begin|began|begun|始める・始まる
ring|rang|rung|鳴る
leave|left|left|出発する・去る・置いていく
feel|felt|felt|感じる
keep|kept|kept|保つ・続ける
spend|spent|spent|（時間・お金を）使う・過ごす
send|sent|sent|送る
lend|lent|lent|貸す
build|built|built|建てる
lose|lost|lost|失う・なくす
win|won|won|勝つ
sit|sat|sat|座る
stand|stood|stood|立つ
understand|understood|understood|理解する
grow|grew|grown|育つ・育てる
throw|threw|thrown|投げる
draw|drew|drawn|（線で絵を）かく
fly|flew|flown|飛ぶ
show|showed|shown|見せる
break|broke|broken|こわす
choose|chose|chosen|選ぶ
forget|forgot|forgotten|忘れる
steal|stole|stolen|盗む
wear|wore|worn|着ている
wake|woke|woken|目を覚ます
drive|drove|driven|運転する
ride|rode|ridden|乗る
rise|rose|risen|のぼる
fall|fell|fallen|落ちる
hide|hid|hidden|かくす
bite|bit|bitten|かむ
shake|shook|shaken|ふる
sell|sold|sold|売る
pay|paid|paid|払う
lay|laid|laid|置く・横たえる
lie|lay|lain|横になる
mean|meant|meant|意味する
hold|held|held|持つ・開く（会を）
lead|led|led|導く
feed|fed|fed|えさをやる
hang|hung|hung|かける・つるす
dig|dug|dug|掘る
shoot|shot|shot|撃つ・シュートする
light|lit|lit|火をつける・照らす
put|put|put|置く
cut|cut|cut|切る
let|let|let|〜させる
set|set|set|置く・設定する
hit|hit|hit|打つ
cost|cost|cost|（費用が）かかる
hurt|hurt|hurt|傷つける・痛む
shut|shut|shut|閉める
spread|spread|spread|広げる・広がる
quit|quit|quit|やめる
forgive|forgave|forgiven|許す
"""
VERBS = []
for _l in IRR.strip().splitlines():
    _b, _p, _pp, _ja = _l.split("|")
    VERBS.append(dict(base=_b, past=_p.split("/"), pp=_pp.split("/"), ja=_ja))

# 形が変わらない語：本文では原形と区別できないので、過去形・過去分詞として出てくる単元を手で書く
# （中1 Unit 16・中2 Unit 15・中3 Unit 1 の不規則動詞の一覧表に read read（read）がある。
#   let は中3 Unit 8 で「let は過去形も let」と解説し、My father let me cook alone last 〜 の例文がある）
SAME_FORM = {1: {"read": 16}, 2: {"read": 15}, 3: {"read": 1, "let": 8}}

# 動詞ではない同じ綴り（数えない）：(学年, 単元, 語)
NOT_VERB = {
    (2, 11, "left"),   # turn left（左へ）
    (3, 9, "left"),    # the left page（左の）
    (3, 14, "left"),   # turn left（左へ）
    (3, 13, "flew"),   # × could flew の誤文の例
}


def text(p: Path) -> str:
    s = p.read_text(encoding="utf-8")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return html.unescape(s)


def collect(g: int):
    d = ROOT / GRADES[g][0]
    first = {}
    for p in sorted(d.glob("unit*_*.html")):
        u = int(re.search(r"unit(\d+)", p.name).group(1))
        low = [t.lower() for t in re.findall(r"[A-Za-z]+", text(p))]
        for v in VERBS:
            forms = [f for f in v["past"] + v["pp"] if f != v["base"]]
            if any(f in low and (g, u, f) not in NOT_VERB for f in forms):
                first.setdefault(v["base"], u)
    for b, u in SAME_FORM.get(g, {}).items():
        first[b] = min(first.get(b, u), u)
    rows = [v for v in VERBS if v["base"] in first]
    rows.sort(key=lambda v: v["base"])
    return rows, first


def en(s):
    return f'<span class="en">{html.escape(s)}</span>'


def unit_files(g):
    d = ROOT / GRADES[g][0]
    return {int(re.search(r"unit(\d+)", p.name).group(1)): p.name for p in d.glob("unit*_*.html")}


CSS = """:root{
  --ink:#20242F;--ink-2:#5A6273;--ink-3:#858B99;--paper:#FFFEFB;--panel:#F5F5F0;--rule:#D5D3CA;
  --be:#2A5C93;--gen:#9C540F;--hi-be:#CFE4F5;--hi-gen:#F7DFC2;
  --hand:255px 12px 225px 15px/15px 225px 15px 255px;
}
*{box-sizing:border-box;}
html{color-scheme:light;-webkit-text-size-adjust:100%;}
body{margin:0;background:var(--paper);color:var(--ink);
  font-family:"Hiragino Kaku Gothic ProN","Hiragino Sans","Noto Sans JP","Yu Gothic Medium","Meiryo",sans-serif;
  font-size:16px;line-height:1.75;font-feature-settings:"palt" 1;}
.sheet{max-width:34rem;margin:0 auto;padding:1.5rem 1.25rem 2.5rem;}
.en{font-family:Georgia,"Times New Roman","Noto Serif JP",serif;}
.topnav{display:flex;gap:.5rem;flex-wrap:wrap;margin:0 0 1.2rem;padding:0;}
.topnav a{text-decoration:none;font-family:"Klee One",sans-serif;font-size:.82rem;font-weight:600;line-height:1.6;
  padding:.22rem .7rem;border:1.5px solid var(--rule);border-radius:var(--hand);color:var(--ink-2);background:var(--panel);}
.unit-head{border-bottom:3px solid var(--ink);border-radius:0 0 12px 3px;padding-bottom:.9rem;margin-bottom:1.4rem;}
.unit-no{display:inline-block;font-family:"Klee One",Georgia,serif;font-size:.9rem;font-weight:600;
  background:var(--hi-be);padding:.05rem .7rem;border-radius:var(--hand);transform:rotate(-1.5deg);margin:0 0 .5rem;}
.unit-title{font-family:"Klee One","Hiragino Kaku Gothic ProN",sans-serif;font-size:1.45rem;line-height:1.45;font-weight:600;margin:0 0 .4rem;}
.unit-lead{margin:0;font-size:.92rem;color:var(--ink-2);line-height:1.75;}
p.note{font-size:.88rem;color:var(--ink-2);margin:0 0 1rem;}
.table-wrap{margin:0 0 1.1rem;}
table.rule{width:100%;border-collapse:collapse;font-size:.9rem;line-height:1.55;}
table.rule th,table.rule td{border:1px solid var(--rule);padding:.45rem .45rem;text-align:left;vertical-align:top;}
table.rule th{background:var(--panel);font-family:"Klee One",sans-serif;font-weight:600;font-size:.8rem;color:var(--ink-2);white-space:nowrap;}
table.rule td.f{white-space:nowrap;}
table.rule td.f .en{font-size:1.02rem;}
.gen-w{color:var(--gen);font-weight:700;}
.pp-w{color:var(--be);font-weight:700;}
table.rule td.m{font-size:.84rem;}
table.rule td.m a{display:block;font-size:.74rem;color:var(--ink-3);text-decoration:none;margin-top:.1rem;}
@media (max-width:420px){table.rule{font-size:.85rem;}table.rule th,table.rule td{padding:.4rem .3rem;}table.rule td.f .en{font-size:.95rem;}}
@media print{@page{size:A4 portrait;margin:15mm 14mm;}body{font-size:10.5pt;}.sheet{max-width:none;padding:0;}
  .topnav{display:none;}.unit-no{transform:none;}tr{break-inside:avoid;}}"""


def page(g):
    folder, gname, home = GRADES[g]
    rows, first = collect(g)
    files = unit_files(g)
    pp = g >= 2
    title = "不規則動詞の原形・過去形・過去分詞" if pp else "不規則動詞の原形と過去形"
    if pp:
        lead = (f"{gname}のワークブックに、過去形か過去分詞で出てくる不規則動詞 {len(rows)}語です。"
                "アルファベット順に並べ、意味の下に、その形が初めて出てくる単元を書いてあります。"
                "過去分詞は、受け身（中2 Unit 15）と現在完了（中3 Unit 1）で使う形です。")
    else:
        lead = (f"中1のワークブックに、過去形で出てくる不規則動詞 {len(rows)}語です。"
                "アルファベット順に並べ、意味の下に、その形が初めて出てくる単元を書いてあります。"
                "play → played のように -ed をつける動詞（規則動詞）は、この表には入れていません。")
    head = "<tr><th>原形</th><th>過去形</th>" + ("<th>過去分詞</th>" if pp else "") + "<th>意味</th></tr>"
    trs = []
    for v in rows:
        u = first[v["base"]]
        link = f'<a href="{files[u]}">Unit {u}</a>' if u in files else f"Unit {u}"
        past = " ／ ".join(f'<span class="en gen-w">{html.escape(x)}</span>' for x in v["past"])
        cells = f'<td class="f">{en(v["base"])}</td><td class="f">{past}</td>'
        if pp:
            cells += '<td class="f">' + " ／ ".join(f'<span class="en pp-w">{html.escape(x)}</span>' for x in v["pp"]) + "</td>"
        cells += f'<td class="m">{html.escape(v["ja"])}{link}</td>'
        trs.append(f"<tr>{cells}</tr>")
    same = [v["base"] for v in rows if all(f == v["base"] for f in v["past"] + (v["pp"] if pp else []))]
    note = ""
    if same:
        note = ('<p class="note">' + "・".join(en(b) for b in same) +
                " は形が変わらない動詞です。" + ("read の過去形・過去分詞は、読み方だけ［レッド］にかわります。" if "read" in same else "") + "</p>\n")
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{gname}　{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Klee+One:wght@400;600&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>
<div class="sheet">
<nav class="topnav"><a href="{home}">← 目次</a></nav>

<header class="unit-head">
<p class="unit-no">{gname}</p>
<h1 class="unit-title">{title}</h1>
<p class="unit-lead">{lead}</p>
</header>

<div class="table-wrap">
<table class="rule">
{head}
{chr(10).join(trs)}
</table>
</div>
{note}</div>
</body>
</html>
""", rows


def main():
    for g in GRADES:
        src, rows = page(g)
        out = ROOT / GRADES[g][0] / "verb-forms.html"
        out.write_text(src, encoding="utf-8")
        print(f"{GRADES[g][1]}: {len(rows)}語 → {out.relative_to(ROOT)}  ({out.stat().st_size} バイト)")


if __name__ == "__main__":
    main()
