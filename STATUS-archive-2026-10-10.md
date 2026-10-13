# 制作の記録

> **2026-10-09（夜）にこのファイルを分割しました。** 新しい記録は上に足しています。 10-08（昼）の順18：単語テストに中2の語を足す、10-07（夜）の順17：中2 Unit 16 の記録は `STATUS-archive-2026-10-08.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-07.md`、`STATUS-archive-2026-10-06.md`、`STATUS-archive-2026-10-05.md`、`STATUS-archive-2026-10-03.md`、`STATUS-archive-2026-10-02.md`、`STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で改名し、この新しい `STATUS.md` を置いています。** アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブ（`STATUS-archive-2026-10-08.md`）とこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-09（夜の枠／JST。開始 2026-10-09 16:13 UTC ＝ 10-10 01:13 JST）　順21：中2の総合テスト 第2部

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り。中1 479語／中2 567語）。2番目は `g2/` に Unit 1〜16 の2本ずつが Drive にそろい、復元した Unit 5〜8 は `check.py 5`〜`8 --grade 2` が NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `--review` が `--grade 2` を受けつける（`GRADE_REVIEW_SPEC[2]` あり）。5番目で `g2/review01.html` はあり、`g2/review02.html` が無いので、**順21＝中2の総合テスト 第2部（Unit 5〜8）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/review02.html` | **新規**（65,274バイト）中2 第2部の総合テスト | g2 |
| `g2/index.html` | 変更（17,261 → 17,264バイト）第2部のまとめの「総合テスト　準備中」をリンクに | g2 |
| `STATUS.md` | 変更（この記録） | ルート |

ほかのファイル（`index.html`・`word-test.html`・`tools/check.py`・`tools/build.py`・`tools/tpl-review.html`・`tools/master-vocab.json`・`units/` の37本・`g2/` の単元ファイル・計画書類）は**1バイトも変えていません**（復元直後と作業後のバイト数を機械で突き合わせて確認。差分は上の2本だけでした）。**`check.py` は今回いっさい触っていません。**

### 中身（`g2/review02.html`）

`python tools/build.py --grade 2 review 2 "第2部　There is・助動詞・文型" "Unit 5〜8" body.html` で組みました。部の名前は `UPDATE-PLAN-g2g3.md`「部の名前」のとおりです。大問の構成・配点は `UPDATE-PLAN.md`「2. 総合テスト」と中1 review02・中2 review01 と同じ（全31問・100点）。

| 大問 | 配点 | 中身 | 出題の Unit |
|---|---|---|---|
| 1 文法 | 25（2×5＋3×5） | 4択5問（There are／don't have to／Shall I／made 〜 for me／had to）、語形変化（There was）、並べかえ2問（Shall we have lunch in the park? ／ My brother showed me the old photos.）、誤文訂正2問（have to → has to／There is many → are） | 5〜8 |
| 2 資料つきの読解 | 18（3×6） | 図書館「Midori Library」の階・部屋・開館時間・きまりの表と、ユキがエマに送るメッセージ **137語** | 5〜7 |
| 3 対話文の読解 | 21（3・4・4・3・4・3） | 体育館へ箱を運ぶケンと ALT のブラウン先生の対話 **135語** | 5〜8 |
| 4 条件英作文 | 10 | 転入してくる生徒のために学校を案内する（Plan A）か写真のアルバムを作る（Plan B）か。**30語以上・because を使う・There is / There are か助動詞を1回以上** | 5〜8 |
| 5 長文の読解 | 26（2×3・3×2・4・4・6） | 町の小さな花屋についてのメイのスピーチ **135語** | 5〜8 |

- 判断が要る問題は8問（英問英答5・下線部の日本語2・条件英作文1）。すべてに模範解答と採点の目安があります。
- **単元の要注意事項を出題に入れました**：Unit 6 の「must not（禁止）と don't have to（不要）は意味が逆」（大問1 問2・大問5 問4 の英問英答・大問2 の表と本文）、Unit 6 の「must に過去形が無いので had to」（大問1 問5）・「have to の三単現 has to」（誤文訂正）、Unit 5 の「うしろの名詞が単数か複数かで is / are」（大問1 問1・誤文訂正・英問英答2問）と「過去は There was」（語形変化）、Unit 7 の「Shall I 〜? / Shall we 〜? は決まった言い方」（大問1 問3・並べかえ・大問3 の ( A ) ( B )・大問5 問3）、Unit 8 の「SVOO の to と for の使い分け」（大問1 問4）と「give / show / send のうしろは人 → 物の順」（並べかえ・大問5 問5の英問英答）。
- **語彙**：中1の479語＋中2 Unit 1〜8 の語（累計1,051語）の範囲で書きました。`master-vocab.json` と機械で突き合わせ、範囲外だったのは `1F` などの階の表示とふりがな的な固有名詞（Midori・Mori）だけです。書くときに外した範囲外の語は `hall`（→ Library に変えた）・`center`・`top`（→ fourth floor）・`thing` / `things` / `anything` / `nothing`（中2 Unit 11）・`back`・`course`（→ Sure.）・`year`（単数形。`years` は中1にあり）・`fee`・`cart` です。

### 検証結果

- `check.py --review 2 --grade 2`：**24項目 NG 0件**（375px で横スクロールなし・印刷 A4 10ページを含む）。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`、`check.py 1`〜`16`。中2：`--index --grade 2`・`--review 1 --grade 2`・`check.py 5`〜`8 --grade 2`。**作業前に同じ検査で NG 0件のベースラインを取ってあります**（`--index --grade 2` は作業後、第2部の総合テストへのリンクを要求する検査に切り替わって OK）。
- `check.py 1`〜`4`・`9`〜`16 --grade 2` は「ファイルが見つかりません」で NG 1件になりますが、これは**今回の工程に要らないので復元していないだけ**です（Drive には32本そろっていて、1バイトも触っていません）。
- **playwright（Chromium・375px）**：`g2/review02.html`・`g2/review01.html`・`g2/index.html`・`index.html`・`units/review01`・`review04`・`review-final`・`word-test.html`（`?part=2-2`・`?unit=5`・`?grade=2`）の**10通り**で scrollWidth 375px・JS の例外0件。コンソールに出る `ERR_TUNNEL_CONNECTION_FAILED` は実行環境から Google Fonts に出られないためで、**何も変えていない中1のページでも同じように出ます**（JS の例外ではありません）。
- **満点の確認**：`g2/review02.html` に全31問の正解（記述は模範解答）を機械で入れて「採点する」を押し、**100点／大問ごとに 25・18・21・10・26 の満点**、結果画面の「Unit ごとの正答率」が Unit 5〜8 の4単元とも100%になることを確かめました。リンク先は `unit05_there-is.html`〜`unit08_svoo-svoc.html`、「目次」は `index.html`（中2の目次）、単語テストは `../word-test.html?part=2-2` です。**回帰として `g2/review01.html` と `units/review02.html` でも同じ満点テストを通しました**（どちらも100点・JS の例外0件）。

### 自分で判断したこと

1. **`check.py` を直さずに本文を書きかえました。** 最初の版で「不定詞（Unit 9 で扱う）：to get、to do」が NG 1件になりました。中身は `have to get up`（大問1 問9）と `have to do`（大問3 問5）で、**どちらも Unit 6 の have to** です。`LATER_GRAMMAR_G2` の不定詞は `(?<!going )\bto\s+(go|be|do|get|…)` なので、`have to` のうしろがこの動詞リストに当たると誤検出します。前の回の `going to` と同じように `have / has / had` の除外を足す手もありますが、**この誤検出が起きるのは「不定詞の first=9 が範囲の外」になる第2部だけ**で、第3部以降（Unit 9〜12・13〜16・総まとめ）と中3では不定詞が範囲内に入るので検査が走りません。道具を弱めるより本文側を直すほうが安全だと判断し、`have to get up` → `have to clean her room`、`have to do` → `must move`（Unit 6 の助動詞のまま）に書きかえました。**`check.py` は1バイトも変えていません。**
2. **大問4の条件に「There is / There are か助動詞（must・have to・should・may）のどれかを1回以上使う」を足しました。** 中2 review01 の条件は「未来のことは will か be going to で書く」でした。第2部の文法（There is・助動詞・文型）を使わせるために、同じ形で第2部の中心の形に置きかえています。模範解答は Plan A（39語）・Plan B（40語）の両方を載せました。
3. **資料つきの読解（大問2）の建物の名前を「Midori Library」にしました。** 最初は「Midori Hall」にしましたが、`hall` が中1＋中2 Unit 1〜8 の範囲外（`center` も範囲外）だったためです。図書館に学習室・音楽室・食堂・庭がある造りは中学生にも想像でき、`library`・`floor`・`study room`・`music room`・`cafeteria`・`garden`・`gate`・`until` はすべて範囲内です。
4. **大問5の下線部の記述（4点）を「2つ書きなさい」の形にしました。** 中1・中2 review01 の記述は要点1〜2個でしたが、ここは店員の発言が2文あり、片方だけでも成り立ってしまうので、設問で明示して採点の目安に「どちらか1つだけなら半分の点」と書いています。
5. 読解3本はいずれも137語・135語・135語で、`PLAN-g2g3.md` 2節の第2部の目安（100〜140語）に入れました。最初の版は149語・141語で NG だったので、対話の「but we are only five students」と「so I know the place for the chairs」、スピーチの「and the colors were very beautiful」を削って収めています。

### 気になった点（次の回への申し送り）

- **次は順22＝中2の総合テスト 第3部（`g2/review03.html`、Unit 9〜12）です。** 要るもの：`tools/tpl-review.html`、`units/review03.html`（見本）、`g2/unit09`〜`unit12` と `g2/vocab09`〜`vocab12`、`g2/index.html`。**読解は120〜160語に上がり**（`GRADE_REVIEW_SPEC[2][3]`）、条件英作文は30語以上のままです。
- **第3部では不定詞（Unit 9〜11）・動名詞（Unit 12）が範囲内に入るので、上の判断1の誤検出は起きません。** 代わりに `stop to 〜` と `stop 〜ing`、`前置詞のうしろは動名詞`（`good at playing`）が出題の勘所です（`PLAN-g2g3.md` 3節 Unit 12）。比較（Unit 13〜）・受動態（Unit 15〜）はまだ使えないので、`than`・`better`・`best`・`more 〜`・`the 〜est`・`as 〜 as`・`be 〜ed by` は書かないでください。
- **語彙の範囲外でつまずきやすい語**（中1＋中2 Unit 1〜8 で確認したもの）：`thing` / `things` / `anything` / `nothing` / `everything`（`something` だけ中1にある）・`hall`・`center`・`top`・`back`・`course`・`year`（単数形）。第3部で範囲が広がっても `thing` は中2 Unit 11 なので、第3部からは使えます。
- 総合テストの本文を書くときは、**`master-vocab.json` の該当キー（`"1"`〜`"16"` ＋ `"g2-1"`〜その部の最後）と機械で突き合わせる**のが早いです。語形（複数・過去・-ing）と固有名詞・数詞を除いて照合すると、中2 review01・review02 とも範囲外は固有名詞だけに収まりました。
- `g2/vocab12_gerund.html` の `take part in 〜` の重複、`IRREGULAR` に無い過去分詞・`worse`／`worst`／`could`、中3 Unit 9 の whose・関係副詞の保留、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート26本、`units/` 37本、`tools/` 11本、`g2/` 33本、`g3/` は空）。復元は計画書類6本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の4本・`units/` の37本・`g2/` の22本（`index`・`review01`・Unit 5〜8 のワークブック4本・単語帳16本）の **72本**で、すべて Drive の `fileSize` とバイト数が一致しました（`g2/unit05_there-is.html` は1回目の復号で取りこぼし、同じ方法でもう1度落として一致）。

---

## 2026-10-09（昼の枠／JST。開始 2026-10-09 06:08 UTC ＝ 15:08 JST）　順20：中2の総合テスト 第1部

手順5の判定：1番目は通過（`g2/index.html` あり・`--grade` あり・`"g2-N"` のキー）。2番目は `g2/` に Unit 1〜16 の2本ずつがそろい、`check.py 1`〜`16 --grade 2` がすべて NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `--review` が `--grade 2` を受けつける（`GRADE_REVIEW_SPEC[2]` あり）。5番目で `g2/review01.html` が無いので、**順20＝中2の総合テスト 第1部（Unit 1〜4）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/review01.html` | **新規**（64,614バイト）中2 第1部の総合テスト | g2 |
| `g2/index.html` | 変更（17,215 → 17,261バイト）第1部のまとめの「総合テスト　準備中」をリンクに。冒頭の説明文を直した | g2 |
| `tools/check.py` | 変更（74,777 → 74,928バイト）中2の「不定詞」の検査が be going to の to を拾わないようにした（判断1） | tools |
| `STATUS.md` | 変更（この記録） | ルート |

ほかのファイル（`index.html`・`word-test.html`・`tools/build.py`・`tools/tpl-review.html`・`tools/master-vocab.json`・`units/` の37本・`g2/` の単元32本・計画書類）は**1バイトも変えていません**（復元直後と作業後のバイト数を突き合わせて確認）。

### 中身（`g2/review01.html`）

`python tools/build.py --grade 2 review 1 "第1部　過去進行形・未来・接続詞" "Unit 1〜4" body.html` で組みました。名前は `UPDATE-PLAN-g2g3.md`「部の名前」のとおりです。大問の構成・配点は `UPDATE-PLAN.md`「2. 総合テスト」と中1 review01 と同じ（全31問・100点）。

| 大問 | 配点 | 中身 | 出題の Unit |
|---|---|---|---|
| 1 文法 | 25（2×5＋3×5） | 4択5問（過去進行形の were／will be／It is going to rain／if＋現在形 2問）、語形変化（was cooking）、並べかえ2問（What are you going to do next Sunday? ／ I think that his idea is interesting.）、誤文訂正2問（Will 〜 comes → come／was watch → was watching） | 1〜4 |
| 2 資料つきの読解 | 18（3×6） | 林間学校の予定表（Green Island・3日間・雨の日の予定）とユキのメッセージ **124語** | 1〜4 |
| 3 対話文の読解 | 21（3・4・4・3・4・3） | 嵐の夜に停電したケンと ALT のブラウン先生の対話 **132語** | 1〜4 |
| 4 条件英作文 | 10 | 海辺の清掃（Plan A）と博物館（Plan B）のどちらを選ぶか。**30語以上・because を使う**。`data-avoid` に will goes／will is／if it will など | 2〜4 |
| 5 長文の読解 | 26（2×3・3×2・4・4・6） | 川の清掃ボランティアについてのリナのスピーチ **120語** | 1〜4 |

- 判断が要る問題は8問（英問英答5・下線部の日本語2・条件英作文1）。すべてに模範解答と採点の目安があります。
- **単元の要注意事項を出題に入れました**：Unit 4 の「if のあとの未来は現在形」（大問1 問5・条件英作文の誤りの形）、Unit 3 の「証拠があっての予測は be going to」（大問1 問3）、Unit 2 の「will のうしろは原形」（誤文訂正）、Unit 1 の「was＋-ing」（語形変化・誤文訂正・英問英答）。
- **語彙**：中1の479語＋中2 Unit 1〜4 の語の範囲で書きました。機械で突き合わせて、範囲外だった `noon`（中2 Unit 16）・`thing`（Unit 11）・`fish`・`luck`・`camp` を書きかえています（`twelve`・`photos`・`animals`・`See you after school.`・`Our Trip to Green Island`）。

### 検証結果

- `check.py --review 1 --grade 2`：**24項目 NG 0件**（375px で横スクロールなし・印刷 A4 10ページを含む）。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`、`check.py 1`〜`16`。中2：`--index --grade 2`・`check.py 1`〜`16 --grade 2`。**作業前にも同じ検査で NG 0件のベースラインを取ってあります**（`--index --grade 2` は作業後、第1部の総合テストへのリンクを要求する検査に切り替わって OK）。
- **playwright（Chromium・375px）**：`word-test.html`（`?unit=5`・`?part=2-1`・`?grade=2`）・`units/review01`・`review04`・`review-final`・`index.html`・`g2/index.html`・`g2/review01.html` の**9通り**で scrollWidth 375px・JS の例外0件。`g2/review01.html` は**全問に正解（記述は模範解答）を入れて「採点する」を押し、100点／大問ごとに 25・18・21・10・26 の満点**になることを確かめました。結果画面の「Unit ごとの正答率」は中2の4単元で、リンク先は `unit01_past-progressive.html`〜`unit04_conjunctions.html`、「目次」は `index.html`（中2の目次）です。

### 自分で判断したこと

1. **`check.py` の中2の「不定詞」の検査を直しました（1行）。** `LATER_GRAMMAR_G2` の不定詞（Unit 9）は `to + 動詞の原形` を拾うので、**be going to（Unit 3）の `going to do`・`going to study`・`going to walk` まで「不定詞（Unit 9 で扱う）」として NG** になっていました（直す前の `check.py` で実際に NG 1件「to do、to go、to study、to walk」を確認）。中2の第1部で be going to を出さないわけにはいかないので、正規表現の頭に `(?<!going )` を付けて **going to のうしろだけを外しました**。`I want to go`・`to the park to play` は今までどおり拾います（確認済み）。be going to 自体は Unit 3 の検査が別にあるので、Unit 1・2 で be going to を使えば今までどおり NG になります。中1の表（`LATER_GRAMMAR`）は触っていません。中2の単元16本の検査も直したあとで NG 0件です。
2. **大問4は「I will choose Plan A（または Plan B）」で書き始め、because を必ず使う条件にしました。** 中1 review01 が「〜 is good for your sister.」で書き始め・good を使う、だったのと同じ作りで、第1部の文法（will／be going to／接続詞）を使わせるためです。模範解答は A・B の両方を30語以上で載せています（A 40語・B 37語）。
3. **`g2/index.html` の冒頭の説明「これから1単元ずつ足していきます。」を「16単元がそろいました。部ごとの総合テストを順に足していきます。」に直しました**（前の回からの申し送り）。
4. 大問2・3・5 の読解は中1 review01 と同じく3本とも語数の目安（100〜140語）に入れています。

### 気になった点（次の回への申し送り）

- **次は順21＝中2の総合テスト 第2部（`g2/review02.html`、Unit 5〜8）です。** 要るもの：`tools/tpl-review.html`、`units/review02.html`（見本）、`g2/unit05`〜`unit08` と `g2/vocab05`〜`vocab08`、`g2/index.html`。読解は100〜140語・条件英作文は30語以上。
- **第2部では There is（Unit 5）が使えるようになります。** `may` は月名の May と綴りが同じなので、`in May` は書かないでください（「May 3」の形だけ検査が外します）。SVOO（Unit 8）の検査は `give me a` などの形を見ます。
- 総合テストの本文を書くときは、**中1＋その学年のその部までの単元の語**で書けているかを `master-vocab.json` と機械で突き合わせると早いです（今回は名前・数・基本語を除いて範囲外が5語見つかりました）。
- `g2/vocab12_gerund.html` の `take part in 〜` の重複、`IRREGULAR` に無い過去分詞・`worse`／`worst`・`could`、中3 Unit 9 の whose・関係副詞の保留、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート25本、`units/` 37本、`tools/` 11本、`g2/` 33本、`g3/` は空）。復元は計画書類5本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の5本・`units/` の37本・`g2/` の33本の **83本**で、すべて Drive の `fileSize` とバイト数が一致しました。

---

## 2026-10-09（夜の枠／JST。開始 2026-10-08 16:13 UTC ＝ 10-09 01:13 JST）　順19：中2の総合テストの道具

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り。中1 479語／中2 567語）。2番目は Drive の `g2/` に Unit 1〜16 の2本ずつがそろい、復元して `check.py 1`〜`16 --grade 2` がすべて NG 0件。3番目は `word-test.html` に `data-g="2"` の語が入っていて `--word-test` が NG 0件。4番目で `check.py --review` が `--grade 2` を受けつけない（`REVIEW_SPEC` が中1の分しかない）ので、**順19＝中2の総合テストの道具**です。教材は作らない回です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `tools/check.py` | 変更（68,053 → 74,777バイト）`--review` の学年対応・`GRADE_REVIEW_SPEC`・新しい検査4つ | tools |
| `tools/build.py` | 変更（5,512 → 7,827バイト）`build_review` の `{{HOME}}`・`{{UNITS}}` 対応 | tools |
| `tools/tpl-review.html` | 変更（36,631 → 35,856バイト）目次リンクと単元名の表を差しかえ可能にした | tools |
| `STATUS.md` | 変更（この記録） | ルート |

**`g2/review01.html`〜`review04.html`・`review-final.html` は作っていません**（順20〜24）。`index.html`・`g2/index.html`・`word-test.html`・`tools/master-vocab.json`・`tools/tpl-workbook.html`・`tools/tpl-vocab.html`・`tools/gen-word-test.py`・`units/` の中1のファイル37本・`g2/` の単元ファイル32本・計画書類は**1バイトも変えていません**（復元直後のバイト数と作業後を突き合わせて確認。`master-vocab.json` 10,439／`index.html` 17,197／`g2/index.html` 17,215／`word-test.html` 105,856／`units/review01` 61,463・`02` 62,744・`03` 64,392・`04` 64,819・`final` 65,480）。

### 中身

- **`GRADE_REVIEW_SPEC`**（`REVIEW_SPEC` を学年別に持ち直した）。中1は従来の値をそのまま。中2は `PLAN-g2g3.md` 5.6 と2節のとおり：

  | 中2 | Unit の範囲 | 読解本文の語数 | 条件英作文の語数下限 |
  |---|---|---|---|
  | 第1部 | 1〜4 | 100〜140語 | 30語以上 |
  | 第2部 | 5〜8 | 100〜140語 | 30語以上 |
  | 第3部 | 9〜12 | 120〜160語 | 30語以上 |
  | 第4部 | 13〜16 | 120〜160語 | 30語以上 |
  | 総まとめ | 1〜16 | 120〜160語 | 30語以上 |

  部の区切りは `GRADE_PARTS[2]`（4部）と同じです。大問の構成と配点（文法25／資料つき読解18／対話文21／条件英作文10／長文26、合計100点）は `UPDATE-PLAN.md`「2. 総合テスト」のまま、学年で変えていません。
- **後で扱う文法の検査が学年別の表を引くようになりました。** これまで `check_review` は中1の表（`GRADE_LATER_GRAMMAR[1]`）を直接見ていました。中2の総合テストでは `LATER_GRAMMAR_G2` を引くので、たとえば第1部（Unit 1〜4）に不定詞が混ざれば「不定詞（Unit 9 で扱う）」と出ます（検証で実際に効くことを確かめました）。「中1では扱わない」の文言も学年名で出ます。
- **`tpl-review.html` を2か所だけ差しかえ可能にしました（CSS と JS の働きは変えていません）。**
  1. `<a href="../index.html">目次</a>` → `<a href="{{HOME}}">目次</a>`。中1の総合テストは `units/` にあって目次がルートなので `../index.html`、中2以降は目次が同じフォルダなので `index.html`（`build.py` の `review_home()`）。**これを直さないと、中2の総合テストの「目次」が中1の目次に飛びます。**
  2. 結果画面の「Unit ごとの正答率」で使う `const UNITS = [...]`（中1の16単元が直書きされていた）→ `const UNITS = {{UNITS}};`。`build.py` の `unit_table(grade)` が**その学年の目次の単元カードから機械で**（`u-title` と「ワークブック」のリンク先の slug）作ります。手で二重に持たないので、目次が正ならこの表も正になります。
- **`check.py` に足した検査4つ**（中1・中2どちらにも効きます）：①目次へ戻るリンクが学年どおり ②単語テストへのリンクの引数が学年どおり（中1は `?part=1`・`?grade=1`、中2は `?part=2-1`・`?grade=2`。`build.py` の既存の決まりと同じ）③結果画面の単元名の表が学年の単元数だけあり、**slug が目次と一致**（slug は「ワークブック →」のリンク先になるので不一致は NG。表示名のちがいは［参考］）④**設問が `<ol class="q">` の直下にある**（下の判断3）。
- `--review` に `--grade 3` を渡すと「中3 の総合テストの仕様はまだありません（順42 で足します）」で止まります（順25 では中3の `LATER_GRAMMAR` と `g3/index.html` を足すだけなので、総合テストの仕様は順42です）。

### 検証結果

- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`（7本）、`check.py 1`〜`16`（16本）。**作業前に同じ23本で NG 0件のベースラインを取ってあります。** `--review` は検査項目が18項目から**23項目**に増えて、増えた分もすべて OK です。
- **中2**：`--index --grade 2`・`check.py 1`〜`16 --grade 2`（17本）すべて NG 0件。合計**40本で NG 0件**です。
- **`--review 1 --grade 2` は「g2/review01.html が無い」の1件だけ NG**。これは正しい動きです（総合テストは順20〜24で作ります）。
- **中2の総合テストを実際に組んで通しました（使い捨て。Drive には上げていません）。** 作業ディレクトリの写しに、大問5つ・配点100点・Unit 1〜4 の出題・読解本文118語・条件英作文30語の仮の1本を書いて `python tools/build.py --grade 2 review 1 ...` で組み、`check.py --review 1 --grade 2` が**22項目 NG 0件**になることを確かめました。出力先が `g2/review01.html` になること、「目次」が `index.html`、単語テストが `?part=2-1`、`const UNITS` が中2の16単元になることも確認しました。**この仮のファイルは検証後に消しています。**
- **`build.py` の後戻りの確認**：中1の既存の review 5本から本文・名前・範囲を取り出して新しい `build.py` で組み直し、**`const UNITS` の表示名4件を除いて1バイトも変わらない**ことを確かめました（判断2）。
- **playwright（Chromium・375px）**：`word-test.html`（`?unit=5`・`?part=2-1`・`?grade=2`）・`units/review01`・`review04`・`review-final`・`index.html`・`g2/index.html`・上の中2 review01 の**10通り**で、**scrollWidth 375px（横スクロールなし）・JS の例外0件**。中1 review01 と中2 review01 は選択肢と記述欄を埋めて「採点する」まで動かし、結果画面の「Unit ごとの正答率」が出ること（中1は 8点・4単元、中2は 5点・4単元）、**中2の行が中2の単元名とリンク（`unit02_will.html` など）になる**ことを確認しました。

### 自分で判断したこと

1. **中2の条件英作文の語数下限は5本すべて30語にしました。** `PLAN-g2g3.md` 5.6 は「中2で30語以上、中3で35語以上」と**学年にひとつの数**を書いていて、部ごとの段をつける指示はありません。中1は 10→15→20→25→25 と上げていますが、これは中1が0から始まるためで、中2の生徒は中1の総まとめで25語を書き終えています。入試の条件英作文が30語程度なので、**中2は最初から30語でそろえる**のが素直だと考えました。段をつけたい場合は `GRADE_REVIEW_SPEC[2]` の3つめの数だけを直せば済みます。
2. **結果画面の単元名は「目次から機械で作る」ほうを選び、中1の既存5本は作り直していません。** 組み直しの確認で、中1の review に直書きされている表が目次と**4件ちがう**ことが分かりました（Unit 8「代名詞」／目次「代名詞（主格・所有格・目的格・所有代名詞）」、Unit 9「三人称単数現在」／目次「三人称単数現在（-s / does / doesn't）」、Unit 10「疑問詞」／目次「疑問詞（what / who / where など8語）」、Unit 15「be動詞の過去形」／目次「be動詞の過去形（was / were）」）。結果画面は狭い一覧なので、短い名前は意図的に手で縮めたものだと思われます。**生徒に渡している中1のページを表示名だけのために差しかえるのは割に合わない**ので、検査は **slug の一致だけを NG にし、表示名のちがいは［参考］で出す**ようにしました（中1は4件、中2は0件）。中1の表示名を目次にそろえるかどうかは**人が判断してください**（そろえる場合は中1の review 5本を組み直して上げ直すだけで、内容は変わりません）。
3. **`<ol class="q">` の検査を足しました（検証中に自分で踏んだため）。** 仮の中2の総合テストを最初 `<ol>`（class なし）で書いたところ、`check.py` は通るのに**ブラウザでの採点が0点**になりました。採点の JS が `#paper ol.q > li` で設問を集めるためです。`check.py` 側は `data-type` を持つ `<li>` を見ていたので気づけませんでした。**検査が通るのに動かない形が残るのは危ない**ので、設問が `<ol class="q">` の直下にあることを数で見る検査を足しました（ol は入れ子になる（設問の中に `ol.choices`・`ol.seq` が入る）ので、開き ol の class を積んで直近の ol だけを見ています）。中1の既存5本はいずれも 31問/31問 などで通ります。**順20〜24で総合テストを書くときは、設問を必ず `<ol class="q">` の直下に置いてください。**
4. **`--grade 3` の案内先を順25から順42に直しました。** 元の文言は「順19・順25 で足します」でしたが、順25（中3の道具の準備）で足すのは `g3/index.html` と中3の `LATER_GRAMMAR` で、総合テストの仕様は順42〜46の回です。
5. **`tpl-review.html` の CSS は触っていません。** 「テンプレートの CSS は触らない」の決まりは `tpl-workbook.html`・`tpl-vocab.html` についてのものですが、`tpl-review.html` でも CSS と JS の働きは変えず、差しかえの穴を2つ開けただけです（差分は目次リンク1行と、直書きの単元表18行を `{{UNITS}}` の1行に替えた分だけ。だからサイズが775バイト減っています）。

### 気になった点（次の回への申し送り）

- **次は順20＝中2の総合テスト 第1部（`g2/review01.html`、Unit 1〜4）です。** 要るもの：`tools/tpl-review.html`、`units/review01.html`（見本）、`g2/unit01`〜`unit04` と `g2/vocab01`〜`vocab04`、`g2/index.html`。大問の構成・配点・採点方法は `UPDATE-PLAN.md`「2. 総合テスト」、語数は上の表（読解100〜140語・条件英作文30語以上）。できたら `g2/index.html` の第1部のまとめの「総合テスト」を「準備中」からリンクに差しかえます（`check.py --index --grade 2` が自動でリンクを要求する検査に切り替わります）。
- **設問は `<ol class="q">` の直下に書いてください**（判断3）。`data-unit` は範囲の Unit をすべて1回以上使う必要があります（`check.py` が抜けを見ます）。
- **`g2/index.html` の冒頭の説明「これから1単元ずつ足していきます。」は、16単元そろったので古いままです。** 前の回からの申し送りで、総合テストの回でまとめて直すとよいと思います（今回は道具の回なので触っていません）。
- **`g2/vocab12_gerund.html` の `take part in 〜` の重複**（中2 Unit 2 で既出）は前の回からの申し送りのままです。**人が判断してください。**
- **`IRREGULAR` に入っていない過去分詞**（`gone`・`begun`・`drawn`・`kept`・`stood`・`rebuilt`・`worn`・`thrown` など）、`worse`／`worst`、`could` は引き続きそのままです（中3 Unit 1 の現在完了の表で要ります）。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です（順34以降）。**まだ先なので今回は通知していません。**
- `tools/gen-word-test.tpl.html` は前の回から使われなくなっています（消すかどうかは人の判断）。

### 飛ばした操作

- **なし。** 5フォルダ（ルート・units・tools・g2・g3）を一覧し、**同名ファイルの重複が無いことを確認しました**（ルート25本、`units/` 37本、`tools/` 11本、`g2/` 33本、`g3/` は空）。復元は計画書類5本・`index.html`・`word-test.html`・`tools/` の4本・`units/` の37本（単元32本＋review 5本）・`g2/` の33本の**81本**で、**すべて Drive の `fileSize` とバイト数が一致**しました。
- **検証の途中で `units/review01`〜`04`・`review-final` を一度ローカルで上書きしました**（`build.py` の後戻り確認で `build_review()` がそのまま書き出すため）。すぐ Drive から**同じ5本を落とし直してバイト数の一致を確かめて**から検査をやり直しています。**Drive 側は触っていません。** 次に同じ確認をするときは、作業ディレクトリの写しの上でやってください。

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
