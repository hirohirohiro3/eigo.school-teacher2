# 制作の記録

> **2026-10-01（夜）にこのファイルを分割しました。** 09-30（昼）〜10-01（昼の枠のあとの対話）の記録（順2：中2 Unit 1、順3：中2 Unit 2、順4：中2 Unit 3、目次ページのヘッダーの帯化）は `STATUS-archive-2026-10-01.md` にそのまま入っています。それより前は `STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で改名し、この新しい `STATUS.md` を置いています。**アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブとこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-02（昼の枠／JST。開始 2026-10-02 06:08 UTC ＝ 15:08 JST）　順6：中2 Unit 5（There is / There are）

手順5の判定は**2番目で止まりました**。1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`"g2-N"` のキーで積む作り）は通過し、N=1〜4 は `python tools/check.py N --grade 2` がいずれも NG 0件、`g2/unit05_*.html` が無い N=5 で止まったので、**順6＝中2 Unit 5（There is / There are、スラッグ `there-is`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit05_there-is.html` | **新規**（47,698バイト） | g2 |
| `g2/vocab05_there-is.html` | **新規**（38,749バイト） | g2 |
| `g2/index.html` | 変更（16,173 → 16,217バイト）Unit 5 をリンクに（`li class="ready"`、単語帳は「36語」） | g2 |
| `tools/master-vocab.json` | 変更（5,754 → 6,122バイト）`"g2-5"` を追加 | tools |
| `STATUS.md` | 変更（この記録を上に追加） | ルート |

**`tools/check.py`・`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。** `IRREGULAR` に足す語もありませんでした（新出の動詞 `tell` `count` のうち、ワークブックに出る過去形は規則変化の `counted` だけで、`told` は単語帳のメモにしか書いていません）。

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「There is / There are は『〜がある・いる』」（図解・訳し方）→「be動詞はうしろの名詞で決まる」（今／過去の表、名詞が2つ並ぶときはすぐうしろの名詞、`There will be` も1文だけ）→「**There is のあとの名詞に the をつけない理由**」→「数えられない名詞と組む」→「否定文と疑問文」（`not any`／`no`、`Is there 〜?`／`Are there any 〜?`／`How many 〜 are there?` と答え方）→「場所を言う語句」→ 判定手順 → 境界事例 → 入試での出方 → よくある間違い → 例文、の順です。
- **`PLAN-g2g3.md` 3節 Unit 5 の4点はすべて入れました**：①**the がつかない理由**を独立した見出しで説明（`There is` は聞き手がまだ知らない物をはじめて出す形、`the` は中1 Unit 4 の「どれか分かっている」印なので両立しない、という理屈。`a / some / 数` と `the / my` を並べた表つき）。②**数えられない名詞**（量が多くても `is` ／ `was`、`a lot of people` と `a lot of snow` の対比）。③**`Is there 〜?` と答え方**（`Yes, there is.` ／ `No, there aren't.`、`it` で答えない誤りを A 4番で出題）。④**`My book is on the desk.` の境界事例**（境界事例の最初の見出し、B 5番で `there` を不要語にした並べ替え、E 4番で読解本文の `My new school is behind the park` を題材に出題）。
- **読解**：ミカがオーストラリアの友だちルーシーに送るメール（引っ越した町の紹介）。本文135語（めやす 100〜140語）。下線部①に `There are two ponds and a playground in the park.`（和訳）、下線部②に `My new school is behind the park`（There を使わない理由）を置きました。
- **単語帳**：新出語 **36語**（めやす 30〜40語）。熟語4（in front of 〜／post office／convenience store／a few 〜）・前置詞4（behind between along across）・名詞20（building bank corner bookstore cafeteria pool playground pond hill shrine village wall roof shelf refrigerator juice money paper person winter）・動詞2（tell count）・形容詞6（dear convenient comfortable peaceful narrow wide）。累計は中1 479語＋中2 181語＝**660語**。

### 検証結果

- **`check.py 5 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳5ページ）。
- **`LATER_GRAMMAR_G2` のうち first が6以上の形を、英文286本（ワークブックの `<span class="en">` と読解本文の文。誤答例の行とパートCは除く）に1文ずつ当てて0件**。正規表現に無い形も目で確かめて0件：`to` ＋ 原形の不定詞0件（`to` のうしろは `a` `the` `Japan` だけ）、`must` `should` `may` `shall` `have to` `than` `more` `most` `better` `best` `enough` `been` `ever` 0件、`-ing` は `swimming pool` の1語だけ（動名詞としてではなく名詞の前の語）。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`。`--index --grade 2`、`check.py 1`〜`4 --grade 2`、`16`（中1 Unit 16）も NG 0件。**作業前にも同じ検査を走らせて全部 NG 0件であることを確かめてから着手しています。**
- **`master-vocab.json` の中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-4"` は作業前と完全に一致**（復元直後の5,754バイトの写しとキーごとに突き合わせ。増えたのは `"g2-5"` の36語だけ）。
- **playwright（Chromium）**：`g2/unit05_there-is.html`・`g2/vocab05_there-is.html`・`g2/index.html`・`index.html`・`word-test.html`・`units/review01.html`・`units/review-final.html` の7本を375px幅で開き、**横スクロールなし（scrollWidth 375px）・JSエラー0件**（テストページは選択肢を選んでボタンを押したあとも0件）。加えて、新しい2本と `g2/index.html` で**画面の左右にはみ出している要素が0個**であることも確かめました（下の「自分で判断したこと」1）。
- **未定義クラス0件**（本文の `class="..."` をテンプレートの CSS と突き合わせ）。新しい2本と `g2/index.html` に `<script>` は0件。

### 自分で判断したこと

1. **図解のノードを3つから2つに減らしました。** 最初は `There is` ／ `a park` ／ `near here` の3ノードにしましたが、`scrollWidth` は375pxのままでも、**ノードが図解の枠の左右からはみ出していました**（スクリーンショットで確認）。`check.py` の横スクロール検査はこれを拾いません。`There is`（be動詞）＋`a park`（ある物＝主語）の2ノードにし、場所は図のキャプションで「場所はそのあと」と書きました。**ノードは2〜3語で2つまでが安全です。** 今回から、`getBoundingClientRect()` で左右にはみ出した要素を数える確認を足しています。
2. **`There is` の主語は be動詞のうしろの名詞、と言い切りました。** 名詞が2つ並ぶとき（`There are two ponds and a playground`）は「be動詞のすぐうしろの名詞に合わせる」と書き、入試で問われる形に絞りました。
3. **`There was / were` と `There will be` も扱いました。** `PLAN-g2g3.md` には書かれていませんが、過去形は中1 Unit 15、`will` は中2 Unit 2 で既習なので範囲内です。`There will be` は解説の1文だけにとどめ、出題はしていません（読解本文に入れていた `there will be a summer concert` の1文は、本文が146語でめやすを超えたので落としました）。
4. **`have` を使う書きかえ（`This town has a library.` ↔ `There is a library in this town.`）を境界事例と D 6番に入れました。** 入試の書きかえで頻出のためです。
5. **固有名詞の所有格を避けました。** `check.py` の語の網羅は、`Ken's` `Mika's` のような形を固有名詞として除外できず未収録に数えます（`proper` が `Ken` だけを拾い、`words_of` は `Ken's` を1語にするため）。解説の `Ken's` は `our` に、E 3番の `Mika's town` は `the new town` に書きかえました。**次の回も、英文で人名の `'s` は使わないでください。**
6. **`dear` を見出しに立てました。** 手紙の書き出し `Dear Lucy,` の `Dear` は文頭の大文字なので網羅の検査では数えられませんが、入試の手紙・メール文で必ず出る語なので立てる価値があると判断しました。`thank`（Thank you）も同じ理由で検査に掛かりませんが、中1の段階で使われてきた決まり文句なので立てていません。
7. **`tell` が中1の見出し語に無かったので、ここで立てました**（`I will tell you about it.`）。中2 Unit 8 の SVOO（`tell 人 物`）より前なので、`tell you about 〜` の形だけを使い、メモにも `tell 人 about 〜` だけを書いています。

### 気になった点（次の回への申し送り）

- **次は順7＝中2 Unit 6（助動詞 must / have to、スラッグ `must-have-to`）です。** `PLAN-g2g3.md` の要注意事項どおり、**must not（禁止）と don't have to（不要）の意味が逆であることを図解と誤文訂正の両方で**扱い、must に過去形が無いので had to、三単現の has to も入れてください。`IRREGULAR` に `had → have` はすでにあります。
- **`check.py` の横スクロール検査は、枠からはみ出したノードを拾いません。** 「自分で判断したこと」1 のとおり、`document.querySelectorAll('body *')` の `getBoundingClientRect()` で `right > 375` か `left < 0` の要素を数える確認を、納める前に足してください（今回の2本と目次は0個）。
- **人名の所有格（`Ken's` など）は語の網羅で NG になります**（「自分で判断したこと」5）。
- 前回の申し送りの **`g2/unit03_be-going-to.html` の未定義クラス `<span class="sub">`** は、1回1工程の決まりがあるので今回も直していません。
- **中3 Unit 9 の whose・関係副詞は、`UPDATE-PLAN-g2g3.md` でまだ「保留」です。**

### 飛ばした操作

- **なし。** ルート・units・tools・g2・g3 の5フォルダを一覧して同名の重複が無いことを確認したので、片付けは不要でした（`g3/` は空です）。

### Drive からの復元（今回も同じ方法で通りました）

`download_file_content` を**サブエージェントに呼ばせるだけ**にして（1体に4本、haiku で十分）、セッション記録から base64 を復号します。今回は60本（中1の37本＋`word-test.html`・`g2/` の9本・tools の5本・ルートの仕様ファイルなど）すべてで Drive の `fileSize` とローカルのバイト数が一致しました。サブエージェント15体、数分で済みます。

- 小さいファイル（おおむね30KB未満）は `subagents/*.jsonl` の `tool_result` に JSON（`{"content": "<base64>"}`）で入っています。
- 大きいファイルは「exceeds maximum allowed tokens」になり、中身は `~/.claude/projects/<作業ディレクトリ>/<セッションID>/tool-results/*.txt` に残ります。**`subagents/*.jsonl` と `tool-results/*.txt` の両方から base64 の連続を拾って復号し、長さが Drive の `fileSize` と一致したものだけ書き出します。** サブエージェントの「失敗」報告は無視してかまいません。
- サイズで突き合わせる方式なので、**同じバイト数のファイルが2本あると取り違えます。** 落とす前に一覧の `fileSize` で重複が無いことを確かめてください（今回の60本はすべて異なるサイズでした）。
- **`units/` にファイルが無いと `--index --grade 2` が NG になります。** 単元を作る回は中1の38本まで落とすのを既定にしてください。

### Drive へのアップロード

**`textContent` で上げ、Drive の `fileSize` とローカルのバイト数を照合してから、古い同名ファイルを `trash_file` に送ります**（`create_file` は同名でも上書きしないため）。**`textContent` は末尾の改行を1つ落とすことがあります。** 末尾が空行で終わるファイルは1バイト短く上がるので、照合して1バイト足りなければ改行を1つ足して上げ直してください。

---

## 2026-10-01（夜の枠／JST。開始 2026-10-01 16:13 UTC ＝ 10-02 01:13 JST）　順5：中2 Unit 4（接続詞 when / if / because / that）

手順5の判定は**2番目で止まりました**。1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り）は通過し、N=1・2・3 は `python tools/check.py N --grade 2` がいずれも NG 0件、`g2/unit04_*.html` が無い N=4 で止まったので、**順5＝中2 Unit 4（接続詞 when / if / because / that、スラッグ `conjunctions`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit04_conjunctions.html` | **新規**（51,490バイト） | g2 |
| `g2/vocab04_conjunctions.html` | **新規**（41,461バイト） | g2 |
| `g2/index.html` | 変更（16,121 → 16,173バイト）Unit 4 をリンクに | g2 |
| `tools/master-vocab.json` | 変更（5,396 → 5,754バイト）`"g2-4"` を追加 | tools |
| `STATUS.md` | **新規に立て直し**（旧 `STATUS.md` は `STATUS-archive-2026-10-01.md` に改名） | ルート |

**`tools/check.py`・`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート（`tpl-workbook.html` `tpl-vocab.html`）・計画書類は1バイトも変えていません。** 今回は `check.py` に足すものがありませんでした（`IRREGULAR` も `CONTRACTIONS` も触っていません。理由は「自分で判断したこと」6）。`index.html`（ルート）のヘッダーの「中2」は順2の回でリンクになっているので、今回は触っていません。

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「2つの文を1つにつなぐ語」（and / but / or との対比と、接続詞のうしろは「主語＋動詞」）→ when → **疑問詞の when と接続詞の when の表** → if → **when と if の中では未来を現在形で言う**（独立した節）→ because → that → 判定手順 → 境界事例 → 入試での出方 → よくある間違い → 例文、の順です。
- **`PLAN-g2g3.md` 3節 Unit 4 の4点はすべて入れました**：①**when / if の中では未来を現在形で言うことを独立した見出しで説明**（図解・3行の表・「なぜ現在形なのか」＝中心の文の `will` がすでに未来を示しているので条件の側では重ねない、という理屈・「現在形でも3人称単数の `-s` は落とさない」を別段落で）。あわせて `because` と `that` のうしろでは未来は `will` で言うことも明示しました。②**従属節が前に来るときのコンマ**（最初の節で「前に出すときだけコンマ」と決め、判定手順の4番目と「よくある間違い」の並べ替えの解説で繰り返し）。③**that の省略**（`that` の節の中に小見出しを立て、「動詞のうしろにいきなり主語＋動詞が続いていたら省かれた that がある」という読み方の手順を置き、D 5番で that を使わない英作文を出題）。④**中1 Unit 10 の疑問詞 when と接続詞 when を表で分けました**（働き・位置・うしろの形・文の終わりの4行）。
- **読解**：ユウタのスピーチ（川の清掃ボランティアと来月の種まき）。本文137語（めやす 100〜140語）。下線部①に `I noticed that 〜`（that の和訳）、下線部②に `If we throw away 〜`（if のうしろが現在形である理由）を置き、E 4番で②の `throw` に `-s` が無く `will` も無い理由を問いました。
- **単語帳**：新出語 **37語**（めやす 30〜40語）。接続詞1（if）・動詞10（think agree explain collect plant grow protect notice promise blow）・名詞14（volunteer garbage bottle plastic environment nature field seed reason event rule forest air spring）・形容詞6（important necessary afraid true local dry）・副詞1（almost）・前置詞1（without）・熟語4（clean up 〜／throw away 〜／for example／at first）。累計は中1 479語＋中2 145語＝**624語**。

### 検証結果

- **`check.py 4 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳6ページ）。
- **中2の `LATER_GRAMMAR_G2` のうち first が5以上の形を、ワークブックの英文（誤答例の行・パートCの誤文・打ち消し線を除く）と読解本文に当てて0件**。278本の英文を1文ずつ当てた結果です。**英文を全部つないだ1本の文字列に当てると `so 〜 that` が2件当たりますが、どちらも別々の `<span class="en">`（「so」と「that」を単独で示した箇所）が連結してできた断片で、文ではありません。** 前回の `not / to / be` と同じ性質なので、**1文ずつ当てる方式に変えました**（この方法のほうが断片を拾わないので、次の回もこちらを使うのがよいです）。
- 正規表現に入っていない形も目で確かめて0件：`to` ＋ 原形の不定詞0件（この単元では未来を `will` だけで書き、`be going to` ＋ 原形を使っていないので、前回の `going to visit` のような誤検出も出ません）、`there is`0件、`have to`0件、`must` `should` `may` `shall`0件、`than` `more` `most`0件（`almost` は `\bmost` の語境界に当たらないので安全）、現在完了0件。**仮定法との区別に注意が要ります**：この単元は `if` を扱うので、`If I were 〜` を1つも書かず、`if` のうしろは現在形だけにしてあります。**間接疑問も避けました**（`I know when 〜` の形を書かず、疑問詞 when は直接疑問文 `When does the volunteer event start?` だけで示しています）。
- **中1の既存の検査はすべて NG 0件**：`--index`（15項目）・`--word-test`（11項目）・`--review 1`〜`4`・`--review final`。`--index --grade 2`（15項目）、`check.py 1 --grade 2`・`2 --grade 2`・`3 --grade 2`・`16`（中1 Unit 16）も NG 0件。**作業前にも同じ13本を走らせて全部 NG 0件であることを確かめてから着手しています**（前後で壊れていないことの比較のため）。
- **`master-vocab.json` の中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-3"` は作業前と完全に一致**。Drive から復元した元ファイル（5,396バイト）をセッション記録から取り直して、キーごとに語のリストを突き合わせました（`"g2-4"` だけが増えています）。
- **playwright（Chromium）**：`g2/unit04_conjunctions.html`・`g2/vocab04_conjunctions.html`・`g2/index.html`・`index.html`・`word-test.html`・`units/review01.html`・`units/review-final.html` の7本を375px幅で開き、**横スクロールなし（scrollWidth 375px）・JSエラー0件**。テストページは選択肢を選んで採点ボタンを押したあとの状態でも0件でした。Google Fonts への接続はこの作業環境のプロキシが拒否しますが、教材側の問題ではありません。
- 新しい2本と `g2/index.html` に `<script>` は0件、外部読み込みは Google Fonts だけ、`<div class="sheet">` は各1個（二重になっていない）。

### 自分で判断したこと

1. **読解本文を一度書き直しました。** 最初に組んだ本文は186語で、めやす（100〜140語）を大きく超えていました。「ペットボトルと古い雑誌を見た」の一文と「晴れなら外で働く」の一文を本文から落とし（どちらも解説側の表に同じ文が残っています）、137語に収めました。あわせて**パートE 2番の選択肢3つを作り直しました**（落とした文を根拠にしていたため）。
2. **「疑問詞の when と接続詞の when」の表を3列のまま細くしました。** 最初は4行目に例文2本を入れていたため、表の幅が421pxになって375pxの検査で NG が出ました。例文を表の下の段落に移し、セルの文言を「文の先頭だけ／先頭と文の中」のように短くして375pxに収めています。**表の中に英文1文を丸ごと入れると、3列では横幅が足りません。次の回も、3列の表には短い語句だけを入れてください。**
3. **図解のノードも短くしました。** `we will read about the environment` をノードに入れると401pxになったので、`If it rains` ／ `we will read` の2ノードに縮め、間に `link`（コンマ）を挟む形にしました。**`node` の中は2〜3語までが安全です。**
4. **新出語を37語にしました**（めやす 30〜40語の範囲内）。はじめ36語で組みましたが、語の網羅チェックで `blowing`（解説の `the wind was blowing`）と `spring`（`in spring` と `Last spring`）が未収録になったので、`blow` と `spring` を見出しに足し、ワークブックに1文も出てこなくなっていた `save` を外しました。**`spring` が中1の見出し語に無いのは意外でしたが、`word-index.html` の479語にも入っていません。**季節の語として入試でも要るので、ここで立てる価値があると判断しました。
5. **接続詞のうち `if` だけを見出しに立てました。** `when`（中1 Unit 10 の疑問詞）・`because`（同 Unit 10）・`that`（中1 Unit 3 の指示代名詞）はすでに見出し語になっているので、単語帳の末尾の注でそのことを書き、重複して立てていません。`clean`（clean up 〜）・`throw`（throw away 〜）・`first`（at first）も語そのものは既出で、熟語としてだけ立てています。
6. **`check.py` に足すものはありませんでした。** `think` `grow` `blow` を新出語に立てたので不規則な過去形（`thought` `grew` `blew`）を `IRREGULAR` に足すかを検討しましたが、**この単元のワークブックにその3語が1つも出てこない**ことを確かめたうえで、足さずに済ませました（単語帳のメモには過去形を書いてあります）。**次に `thought` `grew` `blew` を本文で使う回で `IRREGULAR` に足してください**（`thought → think`・`grew → grow`・`blew → blow`）。
7. **`because` と `so` を重ねない形を独立して扱いました。** `PLAN-g2g3.md` の指示にはありませんが、中1 Unit 4 の `so` を学んだ生徒が `Because 〜, so 〜.` と書くのは入試でもよく見る誤りなので、前に来るもの・うしろに来るものを並べた表を置き、パートC 3番と「よくある間違い」でも扱いました。
8. **テンプレートに無いクラス名を使っていたので直しました。** 最初は接続詞を目立たせるために `<td class="conj-cell">` と `<span class="conj-w">` を書いていましたが、`tpl-workbook.html` の CSS に `conj-` で始まるクラスは1つもありません（あるのは `be-cell`・`be-w`・`gen-w`）。**テンプレートの CSS は触らない約束**なので、`<td><span class="en"><strong>when</strong></span></td>` と `<strong class="en">when</strong>` に書きかえました。`be-w`（青＝be動詞）や `gen-w`（橙＝一般動詞）を流用すると色の意味が崩れるので使っていません。**納める前に、本文で使っているクラス名がテンプレートの CSS に定義されているかを突き合わせる確認を足しました**（`class="..."` を全部集めて CSS 側の `.名前` と差を取るだけです）。新しい2本と `g2/index.html` は未定義クラス0件です。
9. **`afraid` の例文を長い文にしました。** `be afraid of 〜` を熟語として立てず形容詞 `afraid` 1語で立てたため、使い方の説明が要ります。例文は `I am not afraid of hard work now, because I know that it is necessary for our town.`（解説の because の表にある文）をそのまま使い、メモに `be afraid of 〜` の形を書きました。

### 気になった点（次の回への申し送り）

- **次は順6＝中2 Unit 5（There is / There are、スラッグ `there-is`）です。** `PLAN-g2g3.md` の要注意事項どおり、**There is / are のあとの名詞に the がつかない理由**を明示し、`My book is on the desk.` のように特定の名詞では There を使わないという境界事例を必ず置いてください。数えられない名詞との組み合わせ、`Is there 〜?` と答え方もセットです。Unit 4 の接続詞は主節・従属節の両方で使えます。
- **`LATER_GRAMMAR` の照合は1文ずつ当ててください。** 英文を全部つないでから正規表現を当てると、別々の `<span class="en">` が連結してできた断片（今回の `so 〜 that` 2件、前回の `not / to / be` 1件）を拾います。1文ずつ当てれば0件になり、判断に迷いません。
- **3列の表に英文を丸ごと入れると375pxに収まりません。**「自分で判断したこと」2・3のとおり、3列の表は短い語句だけ、図解の `node` は2〜3語までにしてください。
- **復元は今回も中1の38本まで落としました**（16単元×2＋総合テスト5＋`word-test.html`）。これに加えて `g2/` の Unit 1〜3 の6本・テンプレート2本・ルートと tools の仕様ファイル10本で、合計56本です。サブエージェント15体、復元は数分で済み、56本すべてで Drive の `fileSize` とローカルのバイト数が一致しました。
- **`g2/unit03_be-going-to.html` に未定義クラスが1つ残っています。** 上の確認を既存のファイルにも当てたところ、中2 Unit 3 のワークブックが `<span class="sub">` を使っていますが、`tpl-workbook.html` の CSS に `.sub` はありません（`tpl-vocab.html` にはあります）。**表示は崩れず、文字が小さくならないだけ**です。1回1工程の決まりがあるのでこの回では直していません。**次に Unit 3 を触る回か、手直しの回で `<span class="sub">` を外してください。**中1の16単元と中2 Unit 1・2、単語帳はすべて未定義クラス0件でした。
- **納める前にクラス名の突き合わせをしてください。**「自分で判断したこと」8 のとおり、`check.py` も playwright もクラス名の綴り間違いを見つけません（横スクロールもJSエラーも出ないため）。本文の `class="..."` を全部集めて、テンプレートの CSS に定義があるかを見るだけで防げます。
- **中3 Unit 9 の whose・関係副詞は、`UPDATE-PLAN-g2g3.md` でまだ「保留」です。** 順26〜40 で N=9 に当たる回までに決める必要があります（和歌山の過去問で出題の有無を確かめる、という条件）。

### 飛ばした操作

- **なし。** 承認待ちで止まった操作はありません。ルート・units・tools・g2・g3 の5フォルダを一覧して同名の重複が無いことを確認したので、片付けは不要でした（`g3/` は空です）。

### Drive からの復元（今回も同じ方法で通りました）

`download_file_content` を**サブエージェントに呼ばせるだけ**にして（1体に3〜4本、haiku で十分）、セッション記録から base64 を復号します。今回は56本すべてで Drive の `fileSize` とローカルのバイト数が一致しました。

- 小さいファイル（おおむね30KB未満）は `subagents/*.jsonl` の `tool_result` に JSON（`{"content": "<base64>"}`）で入っています。
- 大きいファイルは「exceeds maximum allowed tokens」になり、中身は `~/.claude/projects/<作業ディレクトリ>/<セッションID>/tool-results/*.txt` に残ります。**`subagents/*.jsonl` と `tool-results/*.txt` の両方から400文字以上の base64 の連続を正規表現で拾って復号し、長さが Drive の `fileSize` と一致したものだけ書き出します。** サブエージェントの「失敗」報告は無視してかまいません（今回も `STATUS.md` を FAIL と報告したサブエージェントがいましたが、記録側には完全な base64 が残っていました）。
- サイズで突き合わせる方式なので、**同じバイト数のファイルが2本あると取り違えます。** 落とす前に一覧の `fileSize` で重複が無いことを確かめ、復号後も「そのサイズの候補がちょうど1件か」を見てから書き出してください。今回の56本はすべて異なるサイズでした。
- **`units/` にファイルが無いと `--index --grade 2` が NG になります**（`grade_ready(1)` が「`units/` に `unit??_*.html` が1本以上あるか」で判定するため）。手順7の「中1の既存の検査が壊れていないこと」を確かめるなら、**単元を作る回は中1の38本まで落とす**のを既定にしてください。

### Drive へのアップロード

**`textContent` で上げ、Drive の `fileSize` とローカルのバイト数を照合してから、古い同名ファイルを `trash_file` に送ります**（`create_file` は同名でも上書きしないため）。**`textContent` は末尾の改行を1つ落とすことがあります。** ファイルの末尾が空行で終わる（改行が2つ続く）場合は1バイト短く上がるので、照合して1バイト足りなければ改行を1つ足して上げ直してください。末尾が `</html>\n` のように改行1つで終わる HTML・`.py`・`.json` はそのままで一致します。

### 所要時間

開始 2026-10-01 16:13（UTC）。復元（56本）・ワークブックと単語帳の作成・読解本文の書き直し・表と図解の幅の直し・検証（中1の既存の検査を含む）・アップロードと照合まで、作業環境の時計でおよそ50分でした。アップロードは、**上げたファイルを Drive から1本ずつ落とし直して、ローカルとバイト単位（md5）で一致することまで確かめています**（`fileSize` の一致だけでは、同じ長さの書き写し間違いを見逃します）。5本すべて md5 まで一致しました。

---
