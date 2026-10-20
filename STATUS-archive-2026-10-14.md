# 制作の記録

> **2026-10-13（昼）にこのファイルを分割しました。** 新しい記録は上に足しています（最新は 2026-10-14（昼）の順30：中3 Unit 5）。2026-10-13（夜）の順27：中3 Unit 2、10-12（昼）の順26：中3 Unit 1、10-12（夜）の順25：中3の道具の準備の記録は `STATUS-archive-2026-10-13.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-11.md`、`STATUS-archive-2026-10-10.md`、`STATUS-archive-2026-10-08.md`、`STATUS-archive-2026-10-07.md`、`STATUS-archive-2026-10-06.md`、`STATUS-archive-2026-10-05.md`、`STATUS-archive-2026-10-03.md`、`STATUS-archive-2026-10-02.md`、`STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で `STATUS-archive-2026-10-13.md` に改名し、この新しい `STATUS.md` を置いています。** アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブとこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-14（昼の枠／JST。開始 2026-10-14 06:08 UTC ＝ 15:08 JST）　順30：中3 Unit 5「It is 〜 (for 人) to …」

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"`／`"g3-N"` のキーで積む作り）。2番目は `g2/` に Unit 1〜16 の2本ずつが Drive にそろい、復元した Unit 1 は `--grade 2` で NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `GRADE_REVIEW_SPEC[2]` あり。5・6番目は `g2/review01`〜`04`・`review-final` が NG 0件。7番目は `g3/index.html` あり・`LATER_GRAMMAR_G3` あり。8番目で N=1〜4 は2本ずつそろって NG 0件、**N=5 で `g3/unit05_*.html` が無い**ので、**順30＝中3 Unit 5** です。N=9 ではないので whose・関係副詞の判断は要りませんでした。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g3/unit05_it-to.html` | **新規**（49,353バイト）ワークブック。31問（A6・B6・C5・D7・E5・F2） | **g3** |
| `g3/vocab05_it-to.html` | **新規**（35,809バイト）単語帳。見出し語32語 | **g3** |
| `g3/index.html` | 変更（16,035 → 16,059バイト）Unit 5 のワークブック・単語帳をリンクに（単語テストは順41まで準備中） | g3 |
| `tools/master-vocab.json` | 変更（11,897 → 12,244バイト）`"g3-5"` に32語を追加。中1・中2・`"g3-1"`〜`"g3-4"` のキーは1語も変えていない（前後で機械で突き合わせ、差分は `g3-5` の追加だけ） | tools |
| `STATUS.md` | 変更（この記録を上に追記） | ルート |

ほかの復元ファイル（計画書類4本・`index.html`・`word-test.html`・`tools/` の6本・`units/` の22本・`g2/` の23本・`g3/` の8本）は**1バイトも変えていません**（復元直後の md5・バイト数と突き合わせ）。**`check.py`・`build.py` は今回触っていません**（`hide` の過去形 `hid` は `IRREGULAR` に無いので、本文では使わずに書きました）。

### 中身

- **新出語32語**（めやす30〜40語）。動詞 `escape`・`hide`・`warn`・`contact`・`push`、形容詞 `impossible`・`calm`・`elderly`・`natural`・`whole`、副詞 `safely`、代名詞 `anyone`、名詞 `disaster`・`earthquake`・`tsunami`・`drill`・`siren`・`announcement`・`instruction`・`emergency`・`flashlight`・`battery`・`blanket`・`shelter`・`route`・`ground`・`prefecture`・`head`、熟語 `at least`・`in case of 〜`・`right away`・`get ready for 〜`。累計は中1 479語＋中2 567語＋中3 171語＝1,217語。
- **読解本文は全校集会のスピーチ「防災訓練で学んだこと」177語**（めやす130〜180語。表示は「およそ175語」）。学校の防災訓練と、歩くのが速くない祖母と避難所までの道順を確かめた話で、`It is important for us to 〜`・`It is not easy for her to 〜`・`It is impossible to 〜`・`it is possible for everyone to 〜`・`It is necessary for each family to 〜`（下線部）を本文に置きました。不安をあおる書き方はせず、「そなえればできること」で結んでいます。
- 解説：`To play tennis is fun.` → `It is fun to play tennis.` の書き換え（`transform`）→ 用語枠「形式主語の it」→ **it は主語の位置をうめるだけで中身はうしろの to 〜 にある**図解 → なぜ主語をうしろに回すか（短い結論を先に、長い中身をあとに）→ **「それ」を指す it と何も指さない it の表**（手がかりは文のうしろの to ＋ 原形）→ **for ＋ 人の位置の図解と代名詞の形の表**（中1 Unit 8 の目的格につなぐ。for のうしろの人が to 以下の動作をする）→ よく使う形容詞の表 → 否定文・疑問文と答え方（`Yes, it is.`）→ 手順4段 → 境界（動名詞の主語との書き換え〔中2 Unit 12〕、人を主語にしない `I am difficult to 〜`、`It is a good idea to 〜`、`It is kind of you to 〜` の of）→ 入試での出方 → よくある間違い4件 → まとめ。**中2 Unit 9（不定詞の名詞的用法）は冒頭・手順・D22 の3か所で参照**しています。

### 検証結果

- **`check.py 5 --grade 3`：17項目 NG 0件**（語の網羅 未収録0語・例文の一致 不一致0件・375px で横スクロールなし・A4 ワークブック15ページ／単語帳4ページ）。最初の組み立てでは for ＋ 人の図解（3つの箱を横に並べたもの）が 477px にはみ出したので、2段の図解に分けて直しました。
- **`LATER_GRAMMAR_G3` で first が6以上の形を、ワークブックの全文（設問・解答・読解を含む）に機械でかけて0件**。`help`・`were`・`would`・`could`・`wish`・`enough`・`too`・`who`・`which`・`let`・`make`・`told`・`asked`・`want` は英文に0件、`that` は「`this` や `that` は使いません」の語の名前としての1件だけ、`so` は接続詞の2件（読解）だけであることも確かめました。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 1`。**中2もすべて NG 0件**：`--index --grade 2`・`--review 1`〜`4 --grade 2`・`--review final --grade 2`・`check.py 1 --grade 2`。**中3**は `--index --grade 3`・`check.py 1`〜`5 --grade 3` が NG 0件（計21通り）。
- **playwright（Chromium・375px、Google Fonts は空の CSS に差し替え、`details` をすべて展開）**：`g3/unit05`・`g3/vocab05`・`g3/unit04`・`g3/index.html`・`g2/index.html`・`index.html`・`units/review01.html`・`units/review-final.html`・`g2/review01.html`・`g2/review-final.html`・`word-test.html`（`?g=1`・`?g=2`・`?unit=5`・`?unit=2-5`・`?part=2-1`）の**15通り**で scrollWidth 375px・JS の例外0件・console エラー0件。
- 新しい2本は `<script>` 0件、外部読み込みは Google Fonts だけ。

### 自分で判断したこと

1. **題材を「防災」にしました。** 候補だった海岸清掃・環境の語（`beach`・`trash`・`plastic`・`environment` など）は中2までにほぼ既出で、新出語が集まらないためです。防災は和歌山の生徒に身近で、`It is important to 〜`・`It is necessary for 人 to 〜` が自然に何度も出る題材です。
2. **`It is kind of you to 〜`（of ＋ 人）は解説の境界事例に1段落だけ置き、出題はしていません。** 「この単元の問題では for の形だけを扱います」と解説に書いてあります。人の性質を言う語の of は入試でも出ますが、この単元の焦点（形式主語と for ＋ 人）をぼかさないためです。
3. **`hide` の過去形 `hid` は使いませんでした。** `IRREGULAR` に無く、`check.py` を変えずに済むよう、読解は `We got under our desks` と書き、`hide` は解説の `It is important to hide under a desk during an earthquake.` で立てました。単語帳の注に過去形 `hid`・過去分詞 `hidden` を書いてあります。**`hid`・`hidden` を `IRREGULAR` に足すかは、使う単元が出たときに判断してください。**
4. **`alone`・曜日名（`Sunday`）は未収録なので本文から外しました。** A2 は最初 `on Sunday` でしたが `every morning` に、読解の「祖母は一人で住んでいる」は書かずに「速く歩くのは簡単ではない」だけにしました。
5. **`principal`（校長）は見出し語に立てませんでした**（使う文が作れなかったため）。読解の形式は `PLAN-g2g3.md` 2節の「スピーチ」です。
6. **読解の英問英答（E28）は `What did the writer put in the emergency bag?` とし、`The writer put 〜 in it.` を解答にしました**（固有名詞の所有格を避ける Unit 2〜4 の扱いを継続）。
7. **中3 第2部の名前は前の回のとおり「不定詞の発展・原形不定詞」のままです**（`g3/index.html` の見出しは触っていません）。単語テストのボタンは「準備中」のままです（順41まで）。

### 気になった点（次の回への申し送り）

- **次は順31＝中3 Unit 6（`too 〜 to …` / `〜 enough to …` / `so 〜 that …`。スラッグ `too-enough`）です。** 要るもの：このワークブックと単語帳（`g3/unit05_it-to.html`・`g3/vocab05_it-to.html`。書きぶりの見本）、`tools/tpl-workbook.html`・`tools/tpl-vocab.html`。新出語は累計との差分で、`"g3-6"` のキーに積みます。Unit 6 は「too 〜 to が否定語なしで否定の意味になる」「so 〜 that ～ can't への書き換え」「enough は形容詞のうしろ、名詞の前では前（enough time）」（`PLAN-g2g3.md` 4節）です。**`enough` は `master-vocab.json` にも `BASIC` にも無いことを確かめました**（未収録）。Unit 6 で見出し語に立てることになります。
- **`whose`・関係副詞は `UPDATE-PLAN-g2g3.md` で「保留」のままです。** 判断が要るのは中3 Unit 9（順34）の前、つまり**あと4工程先**です。最優先の `UPDATE-PLAN-g2g3.md` は保留なので、**和歌山の過去問での出題の有無を人が確かめて決める必要があります。**
- **今回あらたに `alone`・`side`・`usual`・`means` が未収録であることが分かりました**（どれも本文では避けました）。曜日名・月名・`worker`・`through`・単独の `after`／`next`・`feel`／`felt`・`nothing`、`IRREGULAR` に無い `worse`／`worst`／`could`・`kept`・`begun`・`thought`・`hid`、`g2/vocab12_gerund.html` の `take part in 〜` の重複、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。
- ［参考］の「解説に出ていない出題語」が18語（`after`・`behind`・`grandmother`・`soccer`・`writer` など）あります。どれも既出語で NG ではありません。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート28本、`units/` 37本、`tools/` 11本、`g2/` 38本、`g3/` 9本）。復元は計画書類4本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の6本・`units/` の22本・`g2/` の23本・`g3/` の9本の **67本**で、すべて Drive の `fileSize` とバイト数が一致しました。大きいファイルは `tool-results/*.txt` に残っていたので復号できました（下の節の要点どおり）。

---

## 2026-10-14（夜の枠／JST。開始 2026-10-13 16:14 UTC ＝ 2026-10-14 01:14 JST）　順29：中3 Unit 4「現在完了と過去形の使い分け」

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"`／`"g3-N"` のキーで積む作り）。2番目は `g2/` に Unit 1〜16 の2本ずつが Drive にそろい、復元した Unit 1 は `--grade 2` で NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `GRADE_REVIEW_SPEC[2]` あり。5・6番目は `g2/review01`〜`04`・`review-final` が NG 0件。7番目は `g3/index.html` あり・`LATER_GRAMMAR_G3` あり。8番目で N=1〜3 は2本ずつそろって NG 0件、**N=4 で `g3/unit04_*.html` が無い**ので、**順29＝中3 Unit 4** です。N=9 ではないので whose・関係副詞の判断は要りませんでした。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g3/unit04_perfect-vs-past.html` | **新規**（47,901バイト）ワークブック。31問（A6・B6・C5・D7・E5・F2） | **g3** |
| `g3/vocab04_perfect-vs-past.html` | **新規**（38,481バイト）単語帳。見出し語34語 | **g3** |
| `g3/index.html` | 変更（15,991 → 16,035バイト）Unit 4 のワークブック・単語帳をリンクに（単語テストは順41まで準備中） | g3 |
| `tools/master-vocab.json` | 変更（11,523 → 11,897バイト）`"g3-4"` に34語を追加。中1・中2・`"g3-1"`〜`"g3-3"` のキーは1語も変えていない（前後で機械で突き合わせ、差分は `g3-4` の追加だけ） | tools |
| `STATUS.md` | 変更（この記録を上に追記） | ルート |

ほかの復元ファイル（計画書類4本・`index.html`・`word-test.html`・`tools/` の6本・`units/` の22本・`g2/` の23本・`g3/` の4本）は**1バイトも変えていません**（復元直後と作業後の md5 を機械で突き合わせ）。**`check.py` は今回触っていません**（`IRREGULAR` などに足す語が出なかったため。使った不規則動詞の過去形・過去分詞はすべて既存の `IRREGULAR` か既出の見出し語でまかなえました）。

### 中身

- **新出語34語**（めやす30〜40語）。動詞 `appear`・`disappear`・`remain`・`receive`・`attend`・`complete`・`graduate`・`damage`、形容詞 `annual`・`main`・`huge`・`colorful`・`historical`、代名詞 `nobody`、名詞 `tradition`・`generation`・`parade`・`dancer`・`performance`・`period`・`crowd`・`square`・`lantern`・`rhythm`・`mayor`・`citizen`・`community`・`relative`、熟語 `so far`・`up to now`・`in those days`・`ever since 〜`・`several times`・`pass down 〜`。累計は中1 479語＋中2 567語＋中3 139語＝1,185語。
- **読解本文は地元の新聞記事「百年続く町の祭り」133語**（めやす130〜180語。表示は「およそ135語」）。1925年に始まったできごとを過去形で、百年続いていることを現在完了で書き分けた記事で、`in those days`（過去形と組む）と `up to now`・`ever since`（現在完了と組む）を本文の中で対比させています。
- 解説：過去形は「点」・現在完了は「過去から今まで」の二段の図解 → **なぜ時を表す語で決まるか**（今とつながる形に、今と切れた語は置けない）→ **過去の一時点を指す語の表**（`yesterday`・`last 〜`・〜 `ago`・`When 〜?`・`in` ＋ 年・`just now`・`then`／`at that time`）→ **現在完了と使える語の表**（Unit 1〜3 の目じるし語を用法ごとに整理）→ **3つの使い方を日本語で見分ける表**（〜したことがある／もう〜した／〜してしまった／ずっと〜している。用法名は覚えさせない）→ 手順4段 → 境界（`When` には必ず過去形、`have been to` と `went to`、`today`・`this morning` は両方に使える、過去形と現在完了を続けて使う）→ 入試での出方 → よくある間違い4件 → まとめ。

### 検証結果

- **`check.py 4 --grade 3`：17項目 NG 0件**（語の網羅 未収録0語・例文の一致 不一致0件・375px で横スクロールなし・A4 ワークブック15ページ／単語帳5ページ）。
- **`LATER_GRAMMAR_G3` で first が5以上の形を、ワークブックと単語帳の全文（設問・解答・読解を含む）に機械でかけて0件**。機械で見分けられない関係代名詞の that も、英文中の `that` が `at that time` の4件だけであることを確かめました。`help`・`wish`・`were`・`enough` は英文に0件です。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 1`。**中2もすべて NG 0件**：`--index --grade 2`・`--review 1`〜`4 --grade 2`・`--review final --grade 2`・`check.py 1 --grade 2`。**中3**は `--index --grade 3`・`check.py 1`〜`4 --grade 3` が NG 0件。
- **playwright（Chromium・375px、Google Fonts は空の CSS に差し替え、`details` をすべて展開）**：`g3/unit04`・`g3/vocab04`・`g3/unit03`・`g3/index.html`・`g2/index.html`・`index.html`・`units/review01.html`・`units/review-final.html`・`g2/review01.html`・`g2/review-final.html`・`word-test.html`（`?g=1`・`?g=2`・`?unit=5`・`?unit=2-5`・`?part=2-1`）の**15通り**で scrollWidth 375px・JS の例外0件・console エラー0件。
- 新しい2本は `<script>` 0件、外部読み込みは Google Fonts だけ。

### 自分で判断したこと

1. **曜日名・月名は今回も使いませんでした。** 前の回の申し送りどおり、`Sunday`〜`Saturday`・`January`〜`December` は `master-vocab.json` にも `BASIC` にも無い語です。Unit 4 は「過去の一時点を指す語」を扱うので `last Sunday` が欲しくなる単元ですが、**`yesterday`・`last week`・`last year`・`last spring`・〜 `ago`・`in` ＋ 年（数字）で十分に代表できる**と判断し、曜日名・月名を新出語に立てずに書きました。年は数字で書けば `check.py` の語の網羅にかからないので、`in 1925`・`in 1961`・`in 2023` を使っています。**曜日名・月名をいつ・どこで立てるかは引き続き人の判断が要ります**（この単元でも必須ではありませんでした）。
2. **`nobody` を見出し語に立てました。** 読解の下線部と解説で「だれも〜ない」を使いたかったためです。`nothing`・`somebody` は立てていません（この単元で使っていないので）。
3. **`worker` は使わず `citizen` に置きかえました。** 最初は「作業員が新しいホールを完成させた」と書いていましたが、`workers` は `work` が既出でも `worker` の寄せ先が無いため語の網羅で未収録になりました。`worker` を新出語に立てるか置きかえるかの選択で、この単元の主題（祭りと地域）に近い `citizen` に寄せるほうが語の配分がよいと判断しました。**`worker` が未収録のままであることは申し送りに残します。**
4. **`reporter`・`once`・`so far` などは「既出に寄る語」と「熟語として立てる語」に分けました。** `reporter` は `report` に寄るので見出し語に立てず、本文でだけ使いました。`once` も `once a week`（既出の熟語）に寄るので立てていません。いっぽう `so far`・`up to now`・`in those days`・`ever since 〜`・`several times`・`pass down 〜` は、構成語がすべて既出でも**この単元の主題そのもの**（過去形と現在完了のどちらと組むか）なので、熟語として6本立てました。
5. **`live` の扱いは Unit 3 の決定を引き継ぎました**（`have lived` で書く）。D24 の解答も `has lived` です。
6. **3用法の識別は用法名を問いませんでした**（`PLAN-g2g3.md` 4節どおり）。A・B・C・D は「適切な語・形を選ぶ」、E25 は「日本語に直す」形にしてあり、「経験・完了・継続のどれか」を答えさせる設問は1問も置いていません。
7. **読解の設問で固有名詞の所有格を避けました**（Unit 2・3 と同じ扱い）。記事の書き手を名前で出さず、`Our town`・`my grandfather` で書いています。
8. **単語テストのボタンは「準備中」のままです**（順41まで）。

### 気になった点（次の回への申し送り）

- **次は順30＝中3 Unit 5（`It is 〜 (for 人) to …`。スラッグ `it-to`）です。** 要るもの：このワークブックと単語帳（`g3/unit04_perfect-vs-past.html`・`g3/vocab04_perfect-vs-past.html`。書きぶりの見本）、`tools/tpl-workbook.html`・`tools/tpl-vocab.html`。新出語は累計との差分で、`"g3-5"` のキーに積みます。Unit 5 は「形式主語の it を図解で示す」「`for 人` の位置」「**中2 Unit 9（不定詞の名詞的用法）を必ず参照する**」（`PLAN-g2g3.md` 4節）です。`check.py` の `LATER_GRAMMAR_G3` では `It is 〜 to` が first=5 なので、Unit 5 からは使えるようになります。
- **第1部（Unit 1〜4）が完成しました。** 中3の総合テスト（順42〜46）は Unit 15 まで作ったあとの工程ですが、第1部の範囲はこれで出題材料がそろっています。
- **`worker` が `master-vocab.json` にも `BASIC` にも無く、`work`（既出）からは寄せられません**（`lemma` は `-er` を落とすので単数の `worker` は通りますが、複数の `workers` は通りません）。`singer`・`player`・`dancer` のように「する人」を表す語は単元ごとに立ててきているので、`worker` も必要になった単元で立てるのが筋だと思います。
- **`whose`・関係副詞は `UPDATE-PLAN-g2g3.md` で「保留」のままです。** 判断が要るのは中3 Unit 9（順34）の前、つまり**あと5工程先**です。`PLAN-g2g3.md` 4節の Unit 12 には「whose は扱わない」とありますが、最優先の `UPDATE-PLAN-g2g3.md` は保留なので、**和歌山の過去問での出題の有無を人が確かめて決める必要があります。**
- ［参考］の「解説に出ていない出題語」が6語（`because`・`countryside`・`going`・`grandfather`・`spring`・`traditional`）あります。どれも既出語で NG ではありません。
- `g2/vocab12_gerund.html` の `take part in 〜` の重複、`IRREGULAR` に無い `worse`／`worst`／`could`・`kept`・`begun`、過去分詞一覧に無い `thought`・`began`・`kept`・`became`、`video`・`hi`・`through`・`after`（単独）・`next`（単独）が `master-vocab.json` にも `BASIC` にも無いこと、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。**今回あらたに `through`・単独の `after`・単独の `next`・`feel`／`felt`・`nothing` が未収録であることが分かり、読解本文で避けました。**

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート28本、`units/` 37本、`tools/` 11本、`g2/` 38本、`g3/` 7本）。復元は計画書類4本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の6本（`build.py`・`check.py`・`master-vocab.json`・`tpl-workbook.html`・`tpl-vocab.html`・`tpl-review.html`）・`units/` の22本（単語帳16本・`review01`〜`04`・`review-final`・`unit01`）・`g2/` の23本（`index`・単語帳16本・`review01`〜`04`・`review-final`・`unit01`）・`g3/` の7本（`index`・`unit01`・`vocab01`・`unit02`・`vocab02`・`unit03`・`vocab03`）の **65本**で、すべて Drive の `fileSize` とバイト数が一致しました。大きいファイルはサブエージェントが「大きすぎて返せなかった」と報告しましたが、`tool-results/*.txt` に残っていたので復号できました（下の節の要点どおり）。**ファイルIDに `__` を含むもの（`10a3lqdTl25sUKbwukzB1dXzhiaWs76__`・`19YfsGWlFC__BWWHORv_MqLddtEyG0ao8`）は `id__title` 形式の中間ファイル名を分割すると取り違えるので、タイトルの末尾一致で拾い直しました。**
- `g2/unit16` と `g2/unit02`〜`unit15` のワークブックは、この工程に要らないので復元していません。そのため `check.py 16 --grade 2` は「ファイルが見つかりません」で NG になりますが、**ファイルの欠落ではなく復元していないだけ**です（Drive には 38本そろっています）。

---

## 2026-10-13（昼の枠／JST。開始 2026-10-13 06:08 UTC ＝ 15:08 JST）　順28：中3 Unit 3「現在完了（継続）と現在完了進行形」

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"`／`"g3-N"` のキーで積む作り）。2番目は `g2/` に Unit 1〜16 の2本ずつが Drive にそろい、復元した Unit 1・16 は `--grade 2` で NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `GRADE_REVIEW_SPEC[2]` あり。5・6番目は `g2/review01`〜`04`・`review-final` が NG 0件。7番目は `g3/index.html` あり・`LATER_GRAMMAR_G3` あり。8番目で N=1・2 は2本ずつそろって NG 0件、**N=3 で `g3/unit03_*.html` が無い**ので、**順28＝中3 Unit 3** です。N=9 ではないので whose・関係副詞の判断は要りませんでした。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g3/unit03_perfect-continue.html` | **新規**（51,646バイト）ワークブック。31問（A6・B6・C5・D7・E5・F2） | **g3** |
| `g3/vocab03_perfect-continue.html` | **新規**（39,658バイト）単語帳。見出し語37語 | **g3** |
| `g3/index.html` | 変更（15,931 → 15,991バイト）Unit 3 のワークブック・単語帳をリンクに（単語テストは順41まで準備中） | g3 |
| `tools/master-vocab.json` | 変更（11,134 → 11,523バイト）`"g3-3"` に37語を追加。中1・中2・`"g3-1"`・`"g3-2"` のキーは1語も変えていない（前後で機械で一致を確認） | tools |
| `STATUS.md` | 新しく立て直し（この記録）。古い版は `STATUS-archive-2026-10-13.md` に改名 | ルート |
| `STATUS-archive-2026-10-13.md` | 改名のみ（中身は前の `STATUS.md` のまま。35,904バイト） | ルート |

ほかの復元ファイル（`index.html`・`g2/index.html`・`word-test.html`・`build.py`・`check.py`・テンプレート2本・`units/` の22本・`g2/` の23本・`g3/` の4本・計画書類4本）は**1バイトも変えていません**（復元直後と作業後の md5 を機械で突き合わせ、差分は上の表の4本＋新規2本だけ）。**`check.py` は今回触っていません**（`IRREGULAR` などに足す語が出なかったため）。

### 中身

- **新出語37語**（めやす30〜40語）。動詞 `trust`・`hurt`・`jog`・`smell`、副詞 `recently`、前置詞 `since`（接続詞の用法は「別の品詞」バッジで注記）、形容詞 `married`・`regular`、名詞 `husband`・`wife`・`teammate`・`coach`・`friendship`・`childhood`・`kindergarten`・`decade`・`apartment`・`neighborhood`・`smartphone`・`puppy`・`hamster`・`chess`・`violin`・`calligraphy`・`marathon`・`leg`・`cough`・`bakery`・`customer`・`flour`・`dough`・`oven`・`loaf`、熟語 `how long 〜?`・`for a long time`・`since then`・`belong to 〜`。累計は中1 479語＋中2 567語＋中3 105語。
- **読解本文はスピーチ「駅前のパン屋」154語**（めやす130〜180語。表示は「およそ155語」）。祖母のパン屋が「いつから」「どのくらいの間」続いているかを読み取る内容で、継続の現在完了・現在完了進行形と中2までの文法（`how to` は中2 Unit 11）だけで書きました。
- 解説：現在形との対比（`I live in Wakayama.` ↔ `I have lived in Wakayama for ten years.`）と「始まり →ずっと→ 今」の図解 → **なぜ現在完了か**（Unit 1 は回数、Unit 2 は終わり、Unit 3 は長さ）→ **`since`（時点）と `for`（長さ）の使い分け表** → `since` のうしろに過去形の文 → いろいろな場面の例文（3段落） → **`How long 〜?` の問いと答え方の表** → 「ずっと〜していない」 → **現在完了進行形（`transform` の図解。`been` が入る理由を中1 Unit 14 の言い回し「-ing形は動詞そのものとしては働かないので be動詞と組む」で説明）** → **状態の動詞（know・want・have・be）は現在完了で継続を表す境界事例の表** → 手順 → 境界（「3年前から」は for、since と from、現在形では言えない、since then と過去の時の語）→ 入試での出方 → よくある間違い4件 → まとめ。

### 検証結果

- **`check.py 3 --grade 3`：17項目 NG 0件**（語の網羅 未収録0語・例文の一致 不一致0件・375px で横スクロールなし・A4 ワークブック16ページ／単語帳5ページ）。
- **`LATER_GRAMMAR_G3` で first が4以上の形を、ワークブックと単語帳の全文（設問・解答・読解を含む）に機械でかけて0件**。機械で見分けられない関係代名詞の that・`help 人 to` も、英文に `that`・`help 〜 to` が1つも無いことを確かめました。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 1`。**中2もすべて NG 0件**：`--index --grade 2`・`--review 1`〜`4 --grade 2`・`--review final --grade 2`・`check.py 1 --grade 2`・`check.py 16 --grade 2`。**中3**は `--index --grade 3`・`check.py 1`〜`3 --grade 3` が NG 0件。**作業前（復元直後）にも同じ19通りで NG 0件のベースラインを取ってあります。**
- **playwright（Chromium・375px、Google Fonts は空の CSS に差し替え、`details` をすべて展開）**：`g3/unit03`・`g3/vocab03`・`g3/unit02`・`g3/index.html`・`g2/index.html`・`index.html`・`units/review01.html`・`units/review-final.html`・`g2/review01.html`・`g2/review-final.html`・`word-test.html`（`?g=1`・`?g=2`・`?unit=5`・`?unit=2-5`・`?part=2-1`）の**15通り**で scrollWidth 375px・JS の例外0件・console エラー0件。
- 新しい2本は `<script>` 0件、外部読み込みは Google Fonts だけ。

### 自分で判断したこと

1. **`live` は「この教材では `have lived` で書く」と明記しました。** `PLAN-g2g3.md` 4節は「状態の動詞（know / live / want）は現在完了で継続を表す」としていますが、`live` は `have been living` も実際に使われる語です。誤りと教えるのは正確でないので、「`have been living` も使われるが、入試でよく出る `have lived` で書く」とし、設問でも `have been living` を誤りにする問題は置いていません。状態の動詞の代表は `know`（誤文訂正 C15・選択 A5）で問いました。
2. **曜日名（Monday など）・`April`・`seventy` は使いませんでした。** 書いている途中で、曜日名・月名が `master-vocab.json` にも `BASIC` にも無いことに気づいたためです（中1から入っていない語）。この単元で新出語に立てると継続の文法とは関係の薄い語で枠を使うので、`since last week`・`from 2015 to 2020` などに言いかえました。**曜日名・月名をいつ・どこで立てるかは人の判断が要ります**（下の申し送り）。
3. **`belong` は熟語 `belong to 〜` として立て、動詞の見出しは立てませんでした。** 中学では `belong to` の形でしか使わないためです。
4. **読解の設問で `Yui's grandmother` を使わず `her grandmother` にしました。** `Yui's` のような固有名詞の所有格は `check.py` の語の網羅が人名と見分けられず NG になるためです（中3 Unit 2 の並べ替えで固有名詞を避けたのと同じ扱い）。
5. **`all day` は見出し語に立てていません**（既出のため。重複を作らない）。`bake`・`customer` の判定では `bake` が既出、`customer` は未収録だったので `customer` を立てました。
6. **「3年前から」＝ `for three years` を境界事例として独立させました。** 日本語の「から」に引かれて `since three years` と書く誤りが多いので、境界の節・よくある間違い・誤文訂正 C13 の3か所で扱いました。
7. **単語テストのボタンは「準備中」のままです**（順41まで）。

### 気になった点（次の回への申し送り）

- **次は順29＝中3 Unit 4（現在完了と過去形の使い分け。スラッグ `perfect-vs-past`）です。** 要るもの：このワークブックと単語帳（`g3/unit03_perfect-continue.html`・`g3/vocab03_perfect-continue.html`。書きぶりの見本）、`tools/tpl-workbook.html`・`tools/tpl-vocab.html`。新出語は累計との差分で、`"g3-4"` のキーに積みます。Unit 4 は「3用法の識別は用法名を答えさせず、日本語に直す・語を選ぶ形で問う」（`PLAN-g2g3.md` 4節）です。
- **曜日名（Sunday〜Saturday）・月名（January〜December）が `master-vocab.json` にも `BASIC` にも無いことが分かりました**（中1 Unit 11「時刻・日付・数」にも見出し語として無い）。今まで中2・中3の各単元はこれらを避けて書いてきたと思われます。中3 Unit 4 は「過去の一時点を指す語（yesterday / last 〜 / 〜 ago / When 〜?）」を扱うので、`last Sunday` のような語が欲しくなる単元です。**中3 Unit 4 で立てるか、基本語リストに足すか、引き続き避けるかは人の判断が要ります**（この回では避けました）。
- **`whose`・関係副詞は `UPDATE-PLAN-g2g3.md` で「保留」のままです。** 判断が要るのは中3 Unit 9（順34）の前です。`PLAN-g2g3.md` 4節の Unit 12 には「whose は扱わない」とありますが、最優先の `UPDATE-PLAN-g2g3.md` は保留なので、**和歌山の過去問での出題の有無を人が確かめて決める必要があります。**
- ［参考］の「解説に出ていない出題語」が12語あります（`boys`・`gym`・`station`・`tennis` など）。どれも既出語で NG ではありません。
- `g2/vocab12_gerund.html` の `take part in 〜` の重複、`IRREGULAR` に無い `worse`／`worst`／`could`・`kept`、過去分詞一覧に無い `thought`・`began`・`kept`・`became`、`video`・`hi` が `master-vocab.json` にも `BASIC` にも無いこと、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート28本、`units/` 37本、`tools/` 11本、`g2/` 37本、`g3/` 5本）。復元は計画書類4本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の5本（`build.py`・`check.py`・`master-vocab.json`・`tpl-workbook.html`・`tpl-vocab.html`）・`units/` の22本（単語帳16本・`review01`〜`04`・`review-final`・`unit01`）・`g2/` の23本（`index`・単語帳16本・`review01`〜`04`・`review-final`・`unit01`・`unit16`）・`g3/` の5本（`index`・`unit01`・`vocab01`・`unit02`・`vocab02`）の **62本**で、すべて Drive の `fileSize` とバイト数が一致しました。大きいファイルはサブエージェントが「大きすぎて返せなかった」と報告しましたが、`tool-results/*.txt` に残っていたので復号できました（下の節の要点どおり）。

---

## Drive からの復元（毎回この方法で通っています）

- サブエージェントに `download_file_content` だけを呼ばせ（1体に3〜4本。モデルは haiku で足ります）、`~/.claude/projects/<作業ディレクトリ>/<セッションID>/subagents/**/*.jsonl` と `tool-results/*.txt` から長い base64 の連なりを正規表現（`[A-Za-z0-9+/]{2000,}={0,2}`）で拾って復号。**復号した長さが Drive の `fileSize` と一致したものだけ書き出す。**
- **サブエージェントが「大きすぎて返せなかった」と報告しても、記録側（`tool-results/*.txt`）には残っています。** 失敗扱いにせず、復号を試してください。親セッションで直接 `download_file_content` を呼んでも、大きいファイルは `tool-results/*.txt` に保存されるので同じ方法で復号できます。
- **ファイルの対応づけは「復号後のバイト数」で行うのが確実です**（タイトルは `index.html` がルートと g2 で重複し、ファイルIDは `__` を含むものがある）。落とす前に `search_files` で全件のサイズを控えておき、サイズが重複しないことを確かめてから落とします。
- `search_files` は1ページ5件ほどしか返さないので `nextPageToken` で全件を取る（`units` は8ページ）。一覧だけをサブエージェントに取らせ、「タイトル／ファイルID／サイズ」のタブ区切りで返させると速いです。

## Drive へのアップロード

- アップロードは `create_file` の `textContent` を使う（`base64Content` は長いと崩れる）。`disableConversionToGoogleType: true` と、`contentMimeType`（`text/html`・`text/x-python`・`application/json`・`text/markdown`）を付ける。
- アップロード後、Drive の `fileSize` とローカルのバイト数が一致することを確かめてから、同名の古いファイルを `trash_file` でゴミ箱に移す。
- STATUS.md が約45KBを超えそうなときは、古い版を `update_file` で `STATUS-archive-日付.md` に改名し、新しい STATUS.md を立てる（この2節を書き写す）。
