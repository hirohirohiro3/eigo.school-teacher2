# 制作の記録

> **2026-09-30（昼）にこのファイルを分割しました。** 09-28（夜）〜09-29（夜）の記録（工程9：中2・中3の設計 `PLAN-g2g3.md`、順1：道具の改造）は `STATUS-archive-2026-09-30.md` にそのまま入っています。それより前は `STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で改名し、この新しい `STATUS.md` を置いています。**アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブとこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下の最新の節に書き写してあります。

---

## 2026-10-01（昼の枠／JST。開始 2026-10-01 06:08 UTC ＝ 15:08 JST）　順4：中2 Unit 3（未来を表す be going to）

手順5の判定は**2番目で止まりました**。1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り）は通過し、N=1・2 は `python tools/check.py N --grade 2` がどちらも NG 0件、`g2/unit03_*.html` が無い N=3 で止まったので、**順4＝中2 Unit 3（未来を表す be going to、スラッグ `be-going-to`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit03_be-going-to.html` | **新規**（48,574バイト） | g2 |
| `g2/vocab03_be-going-to.html` | **新規**（38,037バイト） | g2 |
| `g2/index.html` | 変更（15,872 → 15,922バイト）Unit 3 をリンクに | g2 |
| `tools/check.py` | 変更（61,170 → 61,265バイト）`IRREGULAR` に `built` `sold` `spent` を追加 | tools |
| `tools/master-vocab.json` | 変更（5,020 → 5,396バイト）`"g2-3"` を追加 | tools |
| `STATUS.md` | 変更（この節を追記） | ルート |

**`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート（`tpl-workbook.html` `tpl-vocab.html`）・`build.py`・計画書類は1バイトも変えていません。**

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「be going to ＋ 原形」→ なぜ be動詞が変わるか・なぜ原形か → 主語別の表 → 短縮形・`is going to be` → **will と be going to の使い分け表** → 否定文・疑問文 → 疑問詞と be going to → 判定手順 → 境界事例 → 入試での出方 → よくある間違い → 例文、の順です。
- **`PLAN-g2g3.md` 3節 Unit 3 の3点はすべて入れました**：①使い分け表（前から決めていた予定＝be going to ○／will △、その場で決めた＝be going to ×／will ○、予測＝どちらも○）。Unit 2 の「意志／予測」の2分を受けて「ちがいが出るのは意志のほう」と書き、`probably`／`maybe` の段階づけはそのまま残しています。②be going to のうしろは原形で、be動詞は主語に合わせる（主語別の表・判定手順・誤文訂正・よくある間違い）。③**`going to go` の重複**：境界事例に「`I'm going to go to Kyoto` は正しい、話しことばでは `I'm going to Kyoto` とも言う、ただし `go shopping` のように場所が来ない形は省けない」と書き、あわせて「`to` のうしろが原形なら be going to、場所なら go の進行形」を見分け方として置きました。
- **入試の書きかえ（will ＝ be going to）**も1段落と D 5番で扱いました。
- **読解**：ミカとトムの対話（休みの北海道旅行の予定）。本文130語（話者名を含む `check.py` の数え方で140語。めやす 100〜140語）。前から決めた予定はすべて be going to、かさを借りたその場の決定だけ `I'll buy a gift for you` にして、E 4番でその理由を問いました。
- **単語帳**：新出語 **36語**（めやす 30〜40語）。熟語の中心1（be going to 〜）・動詞9（travel return sell build pack celebrate spend perform sound）・名詞13（airport plane hotel island castle fireworks grandparents gift contest stage photo suitcase cloud）・形容詞5（special traditional wonderful crowded lucky）・副詞3（abroad later finally）・前置詞2（until around）・熟語3（stay with 〜／go shopping／at the end of 〜）。累計は中1 479語＋中2 108語＝**587語**。

### 検証結果

- **`check.py 3 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・375px 横スクロールなし・印刷 A4 ワークブック17ページ／単語帳5ページ）。
- **中2の `LATER_GRAMMAR_G2` のうち first が4以上の形を、ワークブックの英文（誤答例の行・パートCの誤文・打ち消し線を除く）と読解本文に当てて実質0件**。不定詞の正規表現は `going to visit` の `to visit` を拾うので、直前が `going` のものは外して数えました（残った1件は解説の `<span class="en">` を連結したときにできた断片「not / to / be」で、文ではありません）。接続詞の `when` `if` `because` `that`、`there is`、`must` `have to`、`want to` `like to`、`than` は目でも確かめて0件（`that` は `That sounds great.` の指示代名詞だけ）。SVOO になりやすい `give you one` `tell us` は避け、`buy a gift for you`・`talk about` にしています。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`（479語）・`--review 1`〜`4`・`--review final`。`--index --grade 2`、`check.py 1 --grade 2`・`2 --grade 2`・`16`（中1 Unit 16）も NG 0件。
- **`master-vocab.json` の中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`・`"g2-2"` は作業前と完全に一致**（`"g2-3"` を除いて書き出すと元の 5,020バイトに戻ることも確認）。
- **playwright（Chromium）**：`g2/index.html`・`index.html`・`g2/unit03_be-going-to.html`・`g2/vocab03_be-going-to.html`・`word-test.html`・`units/review01.html`・`units/review-final.html` を375px幅で開き、**横スクロールなし・JSエラー0件**（テストページは選択して採点ボタンを押したあとも0件）。Google Fonts への接続はこの作業環境のプロキシが拒否しますが、教材側の問題ではありません。
- 新しい2本と `g2/index.html` に `<script>` は0件。`<div class="sheet">` は各1個（二重になっていない）。

### 自分で判断したこと

1. **`check.py` の `IRREGULAR` に `built → build`・`sold → sell`・`spent → spend` を足しました**。`build` を新出語に立て、パートAの選択肢に `built` を置いたため（前回の `won` `lost` `became` と同じ扱い）。`sold` `spent` は今回のワークブックには出ませんが、同じ単元で立てた語の過去形なので一緒に入れました。
2. **人名の所有格と未出の語を避けました**。`Mika's plane` は `kenta's` と同じ理由で `The plane` に、`OK.` は未収録になるので既出の `All right.` に、`tell us about` は `tell` が未出で SVOO（Unit 8）にも近いので `talk about` に替えました。
3. **パートA 4番は「その場で決めた → will」を選ばせる問題にしました**。選択肢は `will answer`／`am going to answer`／`answered`／`was answering`。入試の書きかえでは両者を同じ意味として扱うことを解説に明記したうえで、使い分けを問うのはこの1問と読解の E 4番だけに絞っています。
4. **「be going to 〜」を熟語の見出しで1つだけ立て、単語帳の先頭に置きました**（Unit 2 で助動詞 `will` を先頭にしたのと同じ並べ方）。`going` は `go` の -ing形なので単独では立てていません。
5. **`parents` は見出しに立てませんでした**。最初は37語で組みましたが、中1 Unit 8 に `parent` が立っていることにアップロード前の見直しで気づき、外して36語にしました（`check.py` の見出し語の重複検査は単元の中だけを見るので、前の単元の見出しの複数形は NG になりません）。単語帳の末尾の注に「`parents` の `parent` は既出」と書いています。
6. **`sound`（〜に聞こえる）を新出語に足しました**。対話の `That sounds great.` が未収録になるためで、入試の対話文でよく出る言い方なので立てる価値があると判断しました。

### 気になった点（次の回への申し送り）

- **次は順5＝中2 Unit 4（接続詞 when / if / because / that）です。** `PLAN-g2g3.md` の要注意事項どおり、`if`／`when` の中は未来でも現在形（`If it is sunny tomorrow, I will 〜`）を独立して説明し、中1 Unit 10 の疑問詞 when と接続詞 when を表で分けます。Unit 2・3 の `will`／`be going to` を主節に使えます。
- **`check.py` の語の網羅は、文頭で大文字になっている語を人名・地名として外します**（`proper` の判定）。新出語が文頭にしか出てこないと「未収録」にならずに抜けるので、今回は大文字で始まる語のうち既出語にも見出し語にも当たらないものを別に取り出して確かめました（残ったのは人名・地名・曜日と `Hi` `Oh` `Thank(s)` だけ。`Thank you` は Unit 2 にも出ている扱いです）。次の回も同じ確認をすると安全です。
- **新出語を立てるときは、前の単元の見出し語の単数形・原形と重ならないかを確かめてください。** 今回、全学年の見出しを `lemma()` で突き合わせる短いスクリプトで確かめました（中2 Unit 1 の `news`→`new`、Unit 2 の `excited`→`exciting` が当たりますが、どちらも別の語なので問題ありません）。
- **復元は今回も中1の38本まで落としました**（前回の申し送りどおり）。サブエージェント15体、合わせて数分で済みました。
- **中3 Unit 9 の whose・関係副詞は、`UPDATE-PLAN-g2g3.md` でまだ「保留」です。**

### 飛ばした操作

- **なし。** 承認待ちで止まった操作はありません。5フォルダを一覧して同名の重複が無いことを確認したので、片付けは不要でした（`g3/` は空）。

### Drive からの復元（今回も同じ方法で通りました）

`download_file_content` を**サブエージェントに呼ばせるだけ**にして（1体に2〜4本、haiku で十分）、セッション記録から base64 を復号します。今回は55本すべてで Drive の `fileSize` とローカルのバイト数が一致しました。

- 小さいファイル（おおむね30KB未満）は `subagents/*.jsonl` の `tool_result` に JSON（`{"content": "<base64>"}`）で入っています。
- 大きいファイルは「exceeds maximum allowed tokens」になり、中身は `~/.claude/projects/<作業ディレクトリ>/<セッションID>/tool-results/*.txt` に残ります（中身の JSON に `id` が入っているので fileId でも照合できます）。**`subagents/*.jsonl` と `tool-results/*.txt` の両方から200文字以上の base64 の連続を正規表現で拾って復号し、長さが Drive の `fileSize` と一致したものだけ書き出します。** サブエージェントの「失敗」報告は無視してかまいません。
- サイズで突き合わせる方式なので、**同じバイト数のファイルが2本あると取り違えます。** 書き出す前に重複サイズが無いことを確かめてください。

### Drive へのアップロード

**`textContent` で上げ、Drive の `fileSize` とローカルのバイト数を照合してから、古い同名ファイルを `trash_file` に送ります**（`create_file` は同名でも上書きしないため）。**`textContent` は末尾の改行を1つ落とすことがあります。** ファイルの末尾が空行で終わる（改行が2つ続く）場合は1バイト短く上がるので、照合して1バイト足りなければ改行を1つ足して上げ直してください。

### 所要時間

開始 2026-10-01 06:08（UTC）。復元（55本）・ワークブックと単語帳の作成・道具の手直し・検証（中1の既存の検査を含む）・アップロードと照合まで、作業環境の時計でおよそ30分でした。

---

## 2026-10-01（夜の枠／JST。開始 2026-09-30 16:13 UTC ＝ 10-01 01:13 JST）　順3：中2 Unit 2（未来を表す will）

手順5の判定は**2番目で止まりました**。1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-1"` のキーで積む作り）は通過し、N=1 は `python tools/check.py 1 --grade 2` が NG 0件だったので、`g2/unit02_*.html` が無い N=2 で止まり、**順3＝中2 Unit 2（未来を表す will、スラッグ `will`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit02_will.html` | **新規**（47,518バイト） | g2 |
| `g2/vocab02_will.html` | **新規**（37,481バイト） | g2 |
| `g2/index.html` | 変更（15,836 → 15,872バイト）Unit 2 をリンクに | g2 |
| `tools/check.py` | 変更（60,482 → 61,170バイト）`CONTRACTIONS` と `IRREGULAR` に追加 | tools |
| `tools/master-vocab.json` | 変更（4,685 → 5,020バイト）`"g2-2"` を追加 | tools |
| `STATUS.md` | 変更（この節を追記） | ルート |

**`units/` の中1のファイル・`word-test.html`・`index.html`・テンプレート（`tpl-workbook.html` `tpl-vocab.html`）・`build.py`・計画書類は1バイトも変えていません。** `index.html` のヘッダーの「中2」は前の回（09-30 昼）でリンクになっているので、今回は触っていません。

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「will ＋ 動詞の原形」→ なぜ原形なのか（中1 Unit 13 の can と同じ理屈）→ be動詞は原形 be → **意志と予測の2つの使い方** → 短縮形の表 → 否定文・疑問文 → 疑問詞と will → 未来を表す語句 → 判定手順 → 境界事例 → 入試での出方 → よくある間違い → 例文、の順です。
- **`PLAN-g2g3.md` 3節 Unit 2 の3点はすべて入れました**：①will のうしろは原形（図解・判定手順・誤文訂正・よくある間違いの4か所で扱い、be動詞は原形 `be` を独立して説明）、②短縮形（`I'll`〜`they'll` と `won't` の8×2の表。`willn't` と書かないことを打ち消し線つきで明示。D の条件英作文で `won't` が1語であることを語数で体感させる）、③**「意志」と「予測」を表で分け、見分け方は主語（自分で決められることか）だと書きました**。Unit 3（be going to）の使い分けの土台になるよう、予測の確かさを `probably`（高い）と `maybe`（低い）で段階づけています。
- **読解**：ケンタのスピーチ（来週の科学館見学と天気予報）。125語（めやす 100〜140語）。
- **単語帳**：新出語 **36語**（めやす 30〜40語）。助動詞1（will）・動詞8（leave win lose hope become move believe change）・名詞12（future forecast afternoon coat plan dream holiday match prize pilot typhoon result）・形容詞5（excited glad fine cool clear）・副詞5（soon tonight someday maybe probably）・前置詞1（near）・熟語4（next week／wake up／take part in 〜／in the future）。累計は中1 479語＋中2 72語＝**551語**。

### 検証結果

- **`check.py 2 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・375px 横スクロールなし・印刷 A4 ワークブック15ページ／単語帳5ページ）。
- **中2の `LATER_GRAMMAR_G2` のうち first が3以上の形を、ワークブックと単語帳の英文に当てて0件**（誤答例の行を除く）。正規表現に入っていない形（接続詞の that・when、SVOC、It is 〜 to、感嘆文）は英文だけを取り出して目で確かめ、`when` は中1 Unit 10 の疑問詞の1件のみ、`to` はすべて前置詞（`come to the party`・`move to Tokyo`）でした。`because`・`if`・`going to`・`there is`・`must`・`should`・`may`・`have to`・`than`・動名詞・`shall` はいずれも0件です。**読解本文も同じ制約で書いています**（中1の文法＋過去進行形＋will だけ）。
- **中1の既存の検査はすべて NG 0件**：`--index`（15項目）・`--word-test`（11項目）・`--review 1`〜`4`・`--review final`（各18項目）。念のため `check.py 16`（中1 Unit 16）も 17項目 NG 0件。
- **`check.py` の変更が中1の語彙抽出を動かしていないことを確認**：変更後に中1の16単元を再検査しても `master-vocab.json` の中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`（36語）が1バイトも変わらないことを突き合わせました。
- **playwright（Chromium）**：`g2/index.html`・`index.html`・`g2/unit02_will.html`・`g2/vocab02_will.html`・`word-test.html`・`units/review01.html`・`units/review-final.html` の7本を375px幅で開き、**横スクロールなし・JSエラー0件**。テストページは選択肢を選んで採点ボタンを押したあとの状態でも0件でした（フォントの読み込み失敗はこの作業環境のプロキシが Google Fonts を通さないためで、教材側の問題ではありません）。
- `g2/unit02_will.html`・`g2/vocab02_will.html`・`g2/index.html` に `<script>` は0件、外部読み込みは Google Fonts だけです。

### 自分で判断したこと

1. **`check.py` の `CONTRACTIONS` に will の短縮形を足しました**（`won't` → will + not、`I'll`〜`they'll` → 代名詞 + will）。`PLAN-g2g3.md` が Unit 2 で短縮形を扱うよう指示しているのに、`won't` と `I'll` が語の網羅チェックで「未収録」になってしまうためです。中1では `wasn't` `weren't` `didn't` などが同じ仕組みで入っていたので、その並びに足しただけです。
2. **`check.py` の `IRREGULAR` に `won → win`・`lost → lose`・`became → become` を足しました**。`win` `lose` `become` を新出語に立てたので、その不規則な過去形を見出し語に寄せる必要があります。中1の `went → go`・`made → make` と同じ扱いです。
3. **`willn't` と `wills` の書き方**。`willn't` は「この綴りにはならない」と示す価値があるので、`<span class="strike">` で包んで誤答例として検査から外しました（`class="en strike"` では検査の除外に当たらないので、`strike` を外側の span にしています）。A 2番の選択肢にあった `wills` は存在しない語なので、**過去形の `was`** に差し替えました（未来と過去の区別を問う選択肢になり、かえって設問がよくなりました）。
4. **`Will you 〜?` は「〜しますか」の意味だけで扱いました**。依頼の言い方（`Will you help me?`）は `PLAN-g2g3.md` 3節で Unit 7 に別枠で置くと決まっているので、この単元の例文・設問には依頼に読める文を入れていません。
5. **読解の空所補充で人名の所有格を避けました**。`Kenta's class will 〜` と書くと `kenta's` が語の網羅チェックで未収録になるため、`Kenta and his classmates will 〜` に変えました。
6. **`build.py` に渡す本文に `<div class="sheet">` を書かないようにしました。** 最初に書いた本文は、中1・中2 Unit 1 の**完成ファイル**から本文を切り出すときに誤ってテンプレート側の `<div class="sheet">` まで拾ってしまい、`sheet` の div が二重になっていました（開き閉じの数は合うので `check.py` も playwright も通り、見た目も崩れません）。**`tpl-workbook.html` は `<div class="sheet">{{BODY}}</div>` の形で開き閉じの両方を、`tpl-vocab.html` は `<div class="sheet">{{HEADER}}…{{BODY}}</div>` の形でやはり両方を持っています。本文に書くのは `<nav class="topnav">` から始まる中身だけです。** 気づいた時点で本文から外して作り直し、中1 Unit 1 とタグの並びが一致することを確かめました。最初に上げてしまった2本（47,545バイト・37,508バイト）はゴミ箱に送り、正しい 47,518バイト・37,481バイト を上げ直しています。**次の回は、見本にする単元の本文を切り出すときに先頭の `<div class="sheet">` を必ず落としてください。**
7. **副詞に `maybe` と `probably` の両方を立てました**。意味が重なりますが、予測の確かさを段階で示せるので、Unit 3 の使い分けに向けて両方を入れる価値があると判断しました。単語帳のメモで互いを参照させています。

### 気になった点（次の回への申し送り）

- **`check.py` の学年切り替えの検査は、`units/` にファイルが無いと `--index --grade 2` が NG になります。** `grade_ready(1)` が「`units/` に `unit??_*.html` が1本以上あるか」で判定するためです。バグではなく、**復元の範囲が足りないときの症状**です。この回は最初 g2 の分だけ復元して NG を1件出し、中1の38本（16単元×2＋総合テスト5＋`word-test.html`）を追加で復元したら消えました。**次の回も、手順7の「中1の既存の検査が壊れていないこと」を確かめるなら、中1の38本の復元が必要です。**「その工程に要るものだけ落とす」と手順7が要求するものがここで食い違うので、**単元を作る回は中1の38本まで落とす**のを既定にしたほうが迷いません（今回の実測で、復元は2分ほど・サブエージェント15体で足りました）。
- **中2 Unit 3（be going to）では、Unit 2 で作った意志・予測の枠をそのまま引き継いでください。** 「前から決めていた予定＝be going to、その場で決めた＝will、予測はどちらも可」という `PLAN-g2g3.md` の使い分け表が、Unit 2 の「意志／予測」の2分と噛み合うように書いてあります。`probably` と `maybe` も Unit 2 で立てた語なので、使い分け表の中で使えます。
- **中3 Unit 9 の whose・関係副詞は、`UPDATE-PLAN-g2g3.md` でまだ「保留」です。** 順26〜40 で N=9 に当たる回までに決める必要があります（和歌山の過去問で出題の有無を確かめる、という条件です）。

### 飛ばした操作

- **なし。** 承認待ちで止まった操作はありません。Drive の重複ファイルも、ルート・units・tools・g2・g3 の5フォルダを一覧して同名の重複が無いことを確認したので、片付けは不要でした（`g3/` は空です）。

### Drive からの復元（今回も同じ方法で通りました）

`download_file_content` を**サブエージェントに呼ばせるだけ**にして（1体に3〜4本、haiku で十分）、セッション記録から base64 を復号します。今回は52本すべてで Drive の `fileSize` とローカルのバイト数が一致しました。

- 小さいファイル（おおむね30KB未満）は `subagents/*.jsonl` の `tool_result` に JSON（`{"content": "<base64>"}`）で入っています。
- 大きいファイルは「exceeds maximum allowed tokens」になり、中身は `~/.claude/projects/<作業ディレクトリ>/<セッションID>/tool-results/*.txt` に残ります。**fileId が書かれていないので、`subagents/*.jsonl` と `tool-results/*.txt` の両方から200文字以上の base64 の連続を正規表現で拾って復号し、長さが Drive の `fileSize` と一致したものだけ書き出します。** サブエージェントの「失敗」報告は無視してかまいません。
- サイズで突き合わせる方式なので、**同じバイト数のファイルが2本あると取り違えます。** 今回の52本はすべて異なるサイズでした（書き出す前に「そのサイズの候補がちょうど1件か」を確かめています）。

### Drive へのアップロード

前回までと同じく **`textContent` で上げ、Drive の `fileSize` とローカルのバイト数を照合してから、古い同名ファイルを `trash_file` に送りました**（`create_file` は同名でも上書きしないため）。

- **`textContent` は末尾の改行を1つ落とします。** ファイルの末尾が空行で終わる（改行が2つ続く）場合、そのまま渡すと **1バイト短く**上がります。`STATUS.md`（末尾が `---\n\n`）で実際に 25,994バイトになり、**改行を1つ余分に足して渡し直して** 25,995バイトになりました。末尾が `</html>\n` のように改行1つで終わる HTML・`.py`・`.json` はそのままで一致します。**上げたあとに必ず `fileSize` を突き合わせ、1バイト足りなければ改行を1つ足して上げ直してください。**

### 所要時間

開始 2026-09-30 16:13（UTC）、終了 16:4x（UTC）。復元（52本）・ワークブックと単語帳の作成・道具の手直し・検証（中1の既存の検査を含む）・アップロードと照合まで、作業環境の時計でおよそ35分でした。

---

## 2026-09-30（昼の枠／JST。開始 2026-09-30 06:08 UTC）　順2：中2 Unit 1（過去進行形）

手順5の判定は**2番目で止まりました**。1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`vocab_key()` が中2を `"g2-N"` で積む作り）は通過し、`g2/` に `unit01_*.html` が無かったので**順2＝中2 Unit 1（過去進行形、スラッグ `past-progressive`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit01_past-progressive.html` | **新規**（47,475バイト） | g2 |
| `g2/vocab01_past-progressive.html` | **新規**（37,305バイト） | g2 |
| `g2/index.html` | 変更（15,782 → 15,836バイト）Unit 1 をリンクに | g2 |
| `index.html` | 変更（17,007 → 16,998バイト）ヘッダーの「中2」をリンクに | ルート |
| `tools/master-vocab.json` | 変更（4,330 → 4,685バイト）`"g2-1"` を追加 | tools |
| `tools/check.py` | 変更（58,708 → 60,482バイト） | tools |
| `README.md` | 変更（8,274 → 9,205バイト）フォルダ構成と `--grade` の使い方 | ルート |
| `STATUS.md` | **新規に立て直し**（旧 `STATUS.md` は `STATUS-archive-2026-09-30.md` に改名） | ルート |

**`units/` の中1のファイル・`word-test.html`・テンプレート（`tpl-workbook.html` `tpl-vocab.html`）・計画書類は1バイトも変えていません。**

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「was / were ＋ -ing形」→ -ing形の作り方（中1 Unit 14 の表）→ 過去形と過去進行形のちがい → 否定文・疑問文 → 疑問詞（What were you doing? と Who が主語の形）→ 判定手順 → 境界事例 → 入試での出方 → よくある間違い → 例文、の順です。
- **`PLAN-g2g3.md` 3節 Unit 1 の3点はすべて入れました**：①中1 Unit 14（現在進行形）＋ Unit 15（be動詞の過去形）の合成であることを `.transform`（`I am reading` → `I was reading`）と図解で示した、②**「-ing形になった動詞は動詞そのものとしては働かないので be動詞と組む」を中1 Unit 14 の言い回しのまま使った**（解説とまとめの2か所）、③進行形にしない動詞 have（持っている）・know・like・want を境界事例に置いた（have＝食べる は進行形にできる例も併記。誤文訂正とパートAでも1問ずつ出題）。
- **読解**：ハルカの日記（嵐で停電した夜）。115語（めやす 100〜140語）。
- **単語帳**：新出語 **36語**（めやす 30〜40語）。動詞8（ring knock shout prepare relax remember feed chat）・名詞12（storm wind noise candle neighbor living room bedroom street floor magazine radio news）・形容詞4・副詞4（suddenly still quietly loudly）・前置詞2（during into）・代名詞2（someone something）・熟語4（go out／turn on 〜／look out of 〜／call 〜 back）。累計は中1 479語＋中2 36語＝**515語**。

### 検証結果

- **`check.py 1 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳5ページ）。
- **中2の `LATER_GRAMMAR`（first が2以上の形）をワークブックと単語帳の英文に当てて0件**（誤答例の行を除く）。`check.py` は単元の検査で `LATER_GRAMMAR` を使わないので、同じ表を取り出して手で走らせました。加えて接続詞の when / if / because / that、to 不定詞、will、than も目で見て0件（`that` は `at that time` だけ）。**読解本文も同じ制約で書いています**（「〜したとき」は接続詞の when を使わず、`at seven` `then` `at that time` で時点を示した）。
- **中1の既存の検査は全部通ります（NG 0件）**：`--index` 15項目／`--word-test` 11項目／`--review 1`・`2`・`3`・`4`・`final` すべて16項目（`--no-render`）。照合のため `units/` の単語帳16本・総合テスト5本・`word-test.html` を Drive から復元して実データで走らせました。
- **`--index --grade 2`：15項目 NG 0件。**
- **`master-vocab.json`**：中1の16キー（479語）は中身も順序も元と一致（元ファイルの末尾 `}}` を除いた部分が新ファイルの先頭と1文字も違わないことを確認）。`"g2-1"` 36語が末尾に1つ増えただけです。`check.py 1 --grade 2` を2回走らせても md5 は同じ（冪等）。
- **playwright（chromium）で 320 / 375 / 414px**：`index.html`・`g2/index.html`・`g2/unit01`・`g2/vocab01`・`word-test.html`・`units/review01.html`・`units/review-final.html` の**21通りすべて横スクロールなし・`pageerror` 0件**。図解3つ（`.transform` と `.diagram` 2つ）を375pxで撮って、はみ出しが無いことを目で確認しました。
- `g2/` の3本と `index.html` の相対リンクはすべて実在します（`basic-words.html`・`word-index.html` は今回復元していないだけで Drive にあります）。

### 自分で判断したこと

1. **中2の単元カードの「単語テスト」ボタンは「準備中」にしました。** 順1で入れた `--index` の検査は、単語帳が1本でもあると `../word-test.html?unit=2-1` へのリンクを要求する作りでした。しかし `word-test.html` に中2の語が入るのは順18で、今リンクを張ると**語の入っていない単語テストに飛ばす**ことになります（順1の判断4「中1の単語テストを中2の単語テストとして出すのは嘘になる」と同じ理由）。そこで `check.py` に `wt_ready(grade)`（`word-test.html` に `data-g="2"` があるか）を足し、それが偽のあいだは**単元カードの3つ目・部のまとめ・中2のまとめ・共通リンクの先頭を「準備中」で正**としました。**順18で語を足すと、自動でリンクを要求する検査に切り替わります。** 中1には影響しません（`wt_ready(1)` は常に真）。
2. **`check.py` が `master-vocab.json` を `indent=1` で書き直していたので、元と同じ詰めた1行（末尾改行つき）で書くように直しました。** そのままだと中1の479語の行がすべて差分に出て、「中1のキーを変えていない」ことが差分で確かめられなくなるためです。中身は変わりません。
3. **`g2/index.html` の共通リンク先頭の説明文**を「単元が完成した回から順に足していきます」から「**中2の16単元がそろったあとに足します**」に直しました。制作順序（順18）と合わせるためです。
4. **`README.md` のフォルダ構成に `g2/` `g3/` を足し、`--grade` の使い方と中2の `nav.topnav` の書き方を1段落足しました。** 前回の申し送り（「中2 Unit 1 の回に合わせてどうぞ」）に従いました。難度基準と技術的な約束の節は触っていません。
5. **新出語に熟語 `call 〜 back` と `look out of 〜` を立てました。** `back` と `out` は中1の既出語に無く、`back` は `came back`（読解）にも出るため、単独語ではなく入試で頻出の熟語で覆う形にしました。`news` と `living room` は綴りの上では既出語（new・live）に寄ってしまい網羅の検査では拾われませんが、意味が別なので見出し語に立てています。
6. **不規則動詞は中1 Unit 16 の一覧にある語だけを使いました**（新しい過去形は `went out` の went だけで、これも既出）。`rang` `fed` は単語帳のメモで形だけ示しています。

### 気になった点（申し送り）

- **次は順3＝中2 Unit 2（未来を表す will、スラッグ `will`）です。** 要注意事項は `PLAN-g2g3.md` 3節 Unit 2（will のうしろは原形／I'll・won't／**will を「意志」と「予測」に分けて説明する**）。見本は `g2/unit01_past-progressive.html` と `g2/vocab01_past-progressive.html`。`index.html` の「中2」はリンクになったので、今後は `g2/index.html` の該当単元だけ差し替えれば足ります。**単語テストのボタンは順18までは「準備中」のまま**です（上の判断1）。
- **読解本文で接続詞 when / if / because / that を使わない制約は Unit 3 まで続きます**（Unit 4 が接続詞）。`check.py` の `LATER_GRAMMAR_G2` は when・that を入れていない（綴りで区別できないため）ので、人の目で確かめてください。今回は上の検証で使った「中2の表を単元の本文に当てるスクリプト」を毎回走らせると安全です（`GRADE_LATER_GRAMMAR[2]` の first が N より大きいものを本文に当てるだけ。十数行）。`check.py` の単元の検査に組み込むかどうかは未決定です。
- **`may` の目安は「in May」を誤検出します**（前回からの申し送り。中2 Unit 1〜6 の読解で月名の May を避ける）。
- 前回までの申し送り（review02 の大問5の空所の順、フッターの「各30問」表記、`REVISION-PLAN.md` 冒頭、`tpl-vocab.html` の `table.rule`（**15回目**）、単語テストの別解4組、判断が要る問題の要点表示の別属性化、語彙照合スクリプトの `check.py` 入り）は**未対応**のままです。
- **`whose` と関係副詞の判断**は中3 Unit 9（順34）の手前までに要ります。`UPDATE-PLAN-g2g3.md` では「保留」のままです。
- リポジトリへの反映は 09-15 以降止まったままです。**今回反映が要るのは** `g2/unit01_past-progressive.html`・`g2/vocab01_past-progressive.html`（新規）、`g2/index.html`・`index.html`・`tools/check.py`・`tools/master-vocab.json`・`README.md`・`STATUS.md`（差し替え）と、改名した `STATUS-archive-2026-09-30.md`（旧 `STATUS.md` そのもの）です。**生徒の見え方の変化**：`index.html` のヘッダーの「中2」が押せるようになり、中2の目次で Unit 1 のワークブックと単語帳が開けます。前回までの分（順1の `g2/index.html`・`tools/build.py` など、`PLAN-g2g3.md`、中1の総合テスト5本ほか）がまだなら一緒に。

### 飛ばした操作

- **`STATUS.md` を分割しました。** 今回の節を足すと 45,599バイトになり、約45KBの目安を超えるためです。旧 `STATUS.md`（32,820バイト）は `update_file` で `STATUS-archive-2026-09-30.md` に改名しただけで、中身は1バイトも触っていません。
- **重複ファイルの片付けは不要でした。** ルート19件（フォルダ4件を含む）・`tools/` 11件・`units/` 37件・`g2/` 1件・`g3/` 0件を一覧し、同名の重複はありませんでした。
- **`units/unit01`〜`unit15`（ワークブック15本）・`basic-words.html`・`word-index.html`・`tools/ref-*.html`・`tools/tpl-review.html`・`tools/gen-word-test.*`・`UPDATE-PLAN.md`・`REVISION-PLAN.md`・過去の `STATUS-archive-*.md` は落としていません。** 順2に要らないためです（`unit16` と `vocab16` は書きぶりの見本として落としました）。
- **承認待ちで止まった操作はありません。**

### Drive からの復元（今回も同じ方法で通りました）

`download_file_content` を**サブエージェントに呼ばせるだけ**にして（1体に3本まで、haiku で十分）、セッション記録から base64 を復号します。今回は36本すべてで Drive の `fileSize` とローカルのバイト数が一致しました。

- 小さいファイル（おおむね30KB未満）は `subagents/*.jsonl` の `tool_result` に JSON（`{"content": "<base64>"}`）で入っています。`tool_use` の `input.fileId` と `tool_use_id` で突き合わせれば、どのファイルか特定できます。
- 大きいファイルは「exceeds maximum allowed tokens」になり、中身は `~/.claude/projects/<作業ディレクトリ>/<セッションID>/tool-results/*.txt` に残ります。**fileId が書かれていないので、2,000文字以上の base64 の連続を正規表現で拾って復号し、長さが Drive の `fileSize` と一致したものだけ書き出します。** サブエージェントの「失敗」報告は無視してかまいません。

### Drive へのアップロード

前回までと同じく **`textContent` で上げ、落とし直して md5 とバイト数を照合してから、古い同名ファイルを `trash_file` に送りました**（`create_file` は同名でも上書きしないため）。

### 所要時間

開始 2026-09-30 06:08（UTC）、終了 06:27（UTC）。復元（36本）・ワークブックと単語帳の作成・道具の手直し・検証・アップロードと照合まで、作業環境の時計でおよそ20分でした。

---


