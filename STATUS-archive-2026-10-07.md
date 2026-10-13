# 制作の記録

> **2026-10-06（夜）にこのファイルを分割しました。** 10-06（昼）の順14：中2 Unit 13、10-05（夜）の順13：中2 Unit 12 の記録は `STATUS-archive-2026-10-06.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-05.md`、`STATUS-archive-2026-10-03.md`、`STATUS-archive-2026-10-02.md`、`STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で改名し、この新しい `STATUS.md` を置いています。** アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブ（`STATUS-archive-2026-10-06.md`）とこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-07（昼の枠／JST。開始 2026-10-07 06:08 UTC ＝ 15:08 JST）　順16：中2 Unit 15（受動態（肯定・否定・疑問））

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`"g2-N"` のキー）。Drive の `g2/` に Unit 1〜14 の2本ずつがそろい、復元して `check.py 1`〜`14 --grade 2` がすべて NG 0件。`g2/unit15_*.html` が無い N=15 で止まったので、**順16＝中2 Unit 15（スラッグ `passive`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit15_passive.html` | **新規**（52,885バイト） | g2 |
| `g2/vocab15_passive.html` | **新規**（34,964バイト） | g2 |
| `g2/index.html` | 変更（16,707 → 16,749バイト）Unit 15 をリンクに（`li class="ready"`、単語帳は「32語」） | g2 |
| `tools/master-vocab.json` | 変更（9,589 → 9,999バイト）`"g2-15"` を追加 | tools |
| `tools/check.py` | 変更（62,843 → 63,452バイト）`IRREGULAR` に過去分詞など18語を追加 | tools |
| `STATUS.md` | 変更（追記） | ルート |

**`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。**

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「受動態は be動詞 ＋ 過去分詞」（`Many people visit this temple.` → `This temple is visited by many people.` の `transform` と `diagram`、なぜ受動態を使うか＝主語に話題の中心を置く、**過去分詞は be動詞と組まないと動詞として働かない**＝中1 Unit 14 の「-ing形は動詞そのものとしては働かないので be動詞と組む」の言い回しをそのまま引いた）→ be動詞は主語と時で決まる（4行の表）→ **過去分詞の一覧表**（規則動詞8語／不規則・過去形と同じ形13語／不規則・過去形とちがう形12語。中1 Unit 16 の不規則変化の語に、中2で増えた `build`・`sell`・`tell`・`send` と、この単元の `hold`・`break` などを足した）→ **`was cleaned` と `was clean` を分ける**（`diagram` と4行の対応表。`was opened` ／ `was open` も並べた）→ `by 〜` は省略できる（省略した理由つきの表4行と、残すときの例）→ 否定文と疑問文は be動詞の文と同じ（答え方・疑問詞の疑問文も）→ 判定手順4段 → 境界事例3つ（助動詞のあとは `be` ＋ 過去分詞／目的語をとらない動詞は受動態にならない／`broken` が形容詞にもなる）→ 入試での出方 → よくある間違い4つ → まとめ → 例文、の順です。
- `PLAN-g2g3.md` 3節 Unit 15 の3点はすべて入れました：①**過去分詞の一覧表を解説に置いてから出題**（上の3つの表。出題はすべて表の語）②**`was cleaned`（受動態）と `was clean`（形容詞）を並べて図解で分けた**（独立した見出し・図解・対応表）③**`by 〜` を省略できることを明示**（独立した見出し。F30 は `by` を使わない受動態を書かせる）。
- **読解**：リクの発表「町を案内した日」（オーストラリアの生徒たちを寺・町役場・店に案内する）。本文159語（めやす 120〜160語）。下線部①が `It was made by a famous artist from our town, and it is loved by the children.`（和訳）、②が `It was written in Japanese!`（だれが何語で書いたかの選択）。`by` のある受動態と無い受動態の両方を入れ、否定の受動態（`Oranges are not grown in my city.`）も入れました。
- **単語帳**：新出語 **32語**（めやす30〜40語）。動詞7（break deliver destroy discover invent produce repair）・名詞17（century ceremony graduation company product fire guide hall invention leader mail package stadium statue stone telephone fruit）・形容詞2（ancient wooden）・熟語6（be ＋ 過去分詞／be ＋ 過去分詞 ＋ by 〜／be ＋ not ＋ 過去分詞／will be ＋ 過去分詞／can be ＋ 過去分詞／all over 〜）。累計は中1 479語＋中2 532語＝**1,011語**。

### 検証結果

- **`check.py 15 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・見出し語32語・重複なし・375px 横スクロールなし・印刷 A4 ワークブック18ページ／単語帳4ページ）。
- **後続文法の検査**（`LATER_GRAMMAR_G2` のうち first が16以上の形と中3分（99）を、誤答例の行を除いたワークブック本文に1文ずつ当てる）：**当たり0件**。あわせて Unit 16 の内容（`be interested in`・`be known to`・`be covered with`・`be made of`／`from`）と `could`・`was born` が本文に無いことを文字列で確かめました（0件）。
- **既存の検査はすべて NG 0件**：中1 `check.py 1`〜`16`・`--index`・`--word-test`・`--review 1`〜`4`・`--review final`（23本）、中2 `check.py 1`〜`14 --grade 2`・`--index --grade 2`（15本）。Unit 15 を足した計39本で NG 0件です。**`check.py` を変える前にも中1の `--index`・`--word-test`・`--review 1`〜`4`・`final` を走らせて NG 0件を確かめてあります。**
- **`master-vocab.json`**：中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-14"` は復元直後の写しとキーごとに突き合わせて**完全に一致**（変更された既存キー0件）。増えたのは `"g2-15"` の32語だけです。
- **playwright（Chromium）**：`g2/unit15`・`g2/vocab15`・`g2/index.html`・`index.html`・`word-test.html`・`units/review01`・`review04`・`review-final` の8本を375px幅で開き、**scrollWidth 375px・はみ出した要素0個・JS の例外0件**（テストページは選択肢・ボタンを操作したあとも0件）。新しい2本に `<script>` は0件、外部読み込みは Google Fonts だけ。**未定義クラス0件**（最初 `diagram is-be` と書いたところ `is-be` がテンプレートに無かったので、中1 Unit 15 と同じ `class="diagram"`（be動詞の青）にしました。CSS は触っていません）。

### 自分で判断したこと

1. **`check.py` の `IRREGULAR` に18語を足しました**（`seen`・`eaten`・`taken`・`written`・`given`・`sung`・`spoke`・`spoken`・`knew`・`known`・`grew`・`grown`・`broke`・`broken`・`chose`・`chosen`・`held`・`done`）。前回の申し送りどおり、過去分詞の一覧表がこの単元の中心なので「語を避ける」対処は取らず、寄せ先の原形（`see`・`write`・`speak` など既出語、`break` はこの単元の見出し語）に寄せる行を足しました。**足したのは追加前に未収録だった語だけ**なので、既存の検査を NG にする向きには働きません（上の39本で確認）。`left`（`leave` の過去分詞）・`found` など、すでに別の語として収録されている形は足していません。
2. **過去分詞そのものは見出し語に立てませんでした。** `written` などは原形がすでに既出語なので、単語帳では新出の動詞（`break` など）のメモに「原形 ― 過去形 ― 過去分詞」を書き、一覧はワークブックの表に任せました。
3. **受動態の形を熟語として6つ立てました**（Unit 14 で `as 〜 as …` などを熟語に立てたのと同じ扱い）。新出の単語が26語で、形の熟語を足して32語です。
4. **`hold`（開く・行う）は見出し語に立て直しませんでした。** `hold` は既出語です。`be held` の意味は `ceremony`・`stadium` のメモと例文で示しました（Unit 14 の `more` と同じく、重複を増やさない判断）。
5. **一覧表に `go` ― `went` ― `gone` を入れませんでした。** `go` は目的語をとらず受動態にならないので、この単元の表には要りません（中3 Unit 1 の現在完了の表で足してください）。代わりに境界事例で「目的語をとらない動詞は受動態にならない」を説明しています。
6. **`was cleaned` の見分けは「be動詞のうしろが `-ed` のついた動詞の形か、`by 〜` があるか」で書きました。** 過去形と過去分詞が同じ形の語の見分け（be動詞の有無）は一覧表の下に短く書くだけにし、詳しい識別は Unit 16（受動態の発展・過去形との識別）に残しています。
7. **`by` のうしろの代名詞（`by him`）は1行で触れるだけにしました。** 能動態との書きかえでの格の変化は Unit 16 の「必ずやること」なので、ここでは書きかえ問題を出していません。
8. **数字は算用数字で書きました**（`about 400 years ago`）。語としての数は増やしていません。`blue`・`fish`・`ground`・`tools`・`being` が既出語に無かったので本文側を書きかえました（`being` は選択肢から外し `are` に）。

### 気になった点（次の回への申し送り）

- **次は順17＝中2 Unit 16（受動態の発展、スラッグ `passive-advanced`）です。** `PLAN-g2g3.md` の要注意事項どおり、`be interested in`／`be known to`／`be covered with`／`be made of`／`be made from` を表で置き、**能動態との書きかえで目的語が主語に上がるときの代名詞の格の変化（him → he）を、中1 Unit 8 の4格表を再掲して扱い**、`be made of` と `be made from` の違いを境界事例に置いてください。今回の Unit 15 では、これらは1文も使っていません（`interested`・`covered`・`made of` などは0件）。
- **Unit 16 の「過去形との識別」は、今回の過去分詞の一覧表（2つめの表＝過去形と同じ形の13語）が土台になります。** 表は `g2/unit15_passive.html` の「過去分詞の一覧表」にあります。
- **`IRREGULAR` に入っていない過去分詞**：`gone`・`begun`・`drawn`・`kept`・`stood`・`rebuilt` などはまだ入っていません。使うときは行を足してください（中3 Unit 1 の現在完了の表でも要ります）。
- `worse` ／ `worst` は引き続き `IRREGULAR` にありません。`could` は引き続き使えません（中3 Unit 13 まで）。
- `word-test.html` の中2の語（順18）は中2 Unit 16 まで作ってからです。今回までで中2は532語（Unit 1〜15）。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です。

### 飛ばした操作

- **なし。** 5フォルダ（ルート・units・tools・g2・g3）を一覧し、同名ファイルの重複が無いことを確認しました（`g3/` は空、ルートはファイル24本、`units/` は37本、`tools/` は11本、`g2/` は作業前29本）。回帰検査のため `units/` の37本・`word-test.html`・`tools/tpl-review.html`・`g2/` の Unit 1〜13 の26本を復元し、すべて Drive の `fileSize` と一致しました。

---

## 2026-10-06（夜の枠／JST。開始 2026-10-06 16:13 UTC ＝ 10-07 01:13 JST）　順15：中2 Unit 14（more / most と as 〜 as）

手順5の判定：1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り）は通過。N=1〜13 は Drive に `g2/unit*_*.html`・`vocab*_*.html` がそろい、復元して `python tools/check.py N --grade 2` を走らせ、1〜13 すべて NG 0件。`g2/unit14_*.html` が無い N=14 で止まったので、**順15＝中2 Unit 14（スラッグ `comparative-more`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit14_comparative-more.html` | **新規**（53,757バイト） | g2 |
| `g2/vocab14_comparative-more.html` | **新規**（38,424バイト） | g2 |
| `g2/index.html` | 変更（16,647 → 16,707バイト）Unit 14 をリンクに（`li class="ready"`、単語帳は「36語」） | g2 |
| `tools/master-vocab.json` | 変更（9,156 → 9,589バイト）`"g2-14"` を追加 | tools |
| `STATUS.md` | 変更（追記） | ルート |

**`tools/check.py`・`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。** 今回は道具に手を入れずに済みました（Unit 13 で `lemma()` に `-er`／`-est` の処理が入っているため、`thicker`・`thinner`・`rarer` などはそのまま既出語でカバーされます）。

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「長い語は `more` ／ `most` を前に置く」（`This book is interesting.` → `This book is more interesting than that one.` の `transform` と `diagram`、もとの文との対応表、なぜ `more` を使うか＝`interestinger` が言いにくいから）→ **`more` ／ `most` を使う語の見分け方の表5行**（短い語／`y` で終わる音のかたまり2つの語／`-ful`・`-ous`・`-ing`・`-ed`・`-ive`・`-ern` で終わる語／音のかたまりが3つ以上の長い語／`-ly` で終わる副詞。迷ったら声に出して `-er` をつけてみる、という決め方も書いた）→「`the most` ＋ もとの形で最上級」（名詞を説明するときは名詞の前にまとめて置く）→「`as 〜 as` で『同じくらい』」（`transform`・`diagram`、**2つの `as` の間は必ずもとの形（原級）**、`as` のうしろの代名詞は Unit 13 の `than` と同じ）→ **「`not as 〜 as` と比較級の書きかえ」（`Ken is taller than Tom.` ↔ `Tom is not as tall as Ken.` の `transform` と3行の対応表。主語を動かさずに `not` をつけると意味が逆になることを明記し、書きかえの手順を2段で示した）** → 判定手順4段 → 境界事例4つ（`as 〜 as possible`／`twice as 〜 as`／`much more`／`-er` と `more` を重ねない）→ 入試での出方 → よくある間違い4つ → まとめ → 例文、の順です。
- `PLAN-g2g3.md` 3節 Unit 14 の3点はすべて入れました：①**`more` ／ `most` をつける語の見分け方**（上の5行の表）②**`as 〜 as` の中は原級、`not as 〜 as` が比較級の書きかえになること**（独立した見出しで扱い、対応表と手順を置いた）③**書きかえで主語が入れかわることを誤文訂正で1問出した**（C15。`Ken is not as tall as Tom.` を「ケンのほうが背が高い」という意図で示し、`Tom is not as tall as Ken.` に直させる。`span.hint` で意図する内容を添えた）。
- **読解**：ミキのスピーチ「私の町とおばの町」（田舎の小さな町と大阪をくらべる）。本文154語（めやす 120〜160語）。下線部①が `The air is fresher, and the view from my window is more beautiful than the view from my aunt's window.`（和訳）、②が `I don't think one place is better than the other place.`（内容の選択）。E27 は `The streets in Osaka are (　) crowded than the streets in the countryside.` に `more` を入れる空所補充です。
- **単語帳**：新出語 **36語**（めやす30〜40語）。長い形容詞5（modern common valuable helpful possible）・短い形容詞3（rare thick thin）・名詞16（countryside view population area traffic market factory height weight length distance speed graph average percent total）・動詞6（compare cost increase measure weigh rise）・熟語6（as 〜 as …／not as 〜 as …／more ＋ 長い形容詞 ＋ than／the most ＋ 長い形容詞／as 〜 as possible／twice as 〜 as …）。累計は中1 479語＋中2 500語＝**979語**。

### 検証結果

- **`check.py 14 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・見出し語36語・重複なし・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳5ページ）。
- **後続文法の検査**（`LATER_GRAMMAR_G2` のうち first が15以上の形と中3分（99）を、誤答例の行・選択肢・パートCの問題文を除いた英文398本に1文ずつ当てる）：**当たり0件**。受動態・現在完了・`too 〜 to`／`so 〜 that`・人 ＋ to・人 ＋ 原形・間接疑問・関係代名詞・仮定法・付加疑問はすべて0件。`as 〜 as`（first=14）と比較級・最上級（first=13）はこの単元から範囲内です。
- **既存の検査はすべて NG 0件**：中1 `check.py 1`〜`16`・`--index`・`--word-test`・`--review 1`〜`4`・`--review final`（23本）、中2 `check.py 1`〜`13 --grade 2`・`--index --grade 2`（15本）。Unit 14 を足した計38本で NG 0件です。**今回は `check.py` を1バイトも変えていないので、変更前後の `diff` は不要でした。**
- **`master-vocab.json`**：中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-13"` は復元直後の写し（9,156バイト）とキーごとに突き合わせて**完全に一致**（変更された既存キー0件）。増えたのは `"g2-14"` の36語だけです。中1・中2の全38本の検査を走らせたあとも内容が変わらないことを確かめました。
- **playwright（Chromium）**：`g2/unit14`・`g2/vocab14`・`g2/index.html`・`g2/unit13`・`index.html`・`word-test.html`・`units/review01`・`review04`・`review-final` の9本を375px幅で開き、**scrollWidth 375px・はみ出した要素0個・JS の例外0件**（テストページは選択肢・ボタン・入力欄を操作したあとも0件）。新しい2本と `g2/index.html` に `<script>` は0件、外部読み込みは Google Fonts だけ。**未定義クラス0件**。

### 自分で判断したこと

1. **`more` ／ `most` を使う語の見分け方は「音節」ではなく「音のかたまり」と書きました。** 「音節」は中学の英語の教材では使わない用語なので、「音のかたまりが1つ／2つ／3つ以上」という言い方にそろえました。あわせて「迷ったら声に出して `-er` をつけてみる（`beautifuler` は言えない）」という決め方を添えています。規則を覚えきれない生徒でも判断できるようにするためです。
2. **見分け方の表の語の一覧は `<br>` で短く折り返しました。** 最初はコンマ区切りの1行で書いたところ、表の幅が781pxになり、375px幅で表の中の19要素がはみ出しました（ページ全体の横スクロールは出ませんが、Unit 13 の綴りルール表は0件です）。Unit 13 と同じく1行2〜3語で折る形にそろえ、はみ出し0件にしました。**CSS は触っていません。**
3. **`more` ／ `most` は見出し語に立て直しませんでした。** Unit 13 で `many` ／ `much` の比較級・最上級（形容詞）として立てています。`README.md` は「別の単元で別の品詞として出てきたら改めて立てる」としていますが、今回の `more` ＋ 形容詞は品詞が変わったのではなく「比較級を作る語」としての使い方なので、単語の重複を増やさず、熟語の見出し（`more ＋ 長い形容詞 ＋ than`・`the most ＋ 長い形容詞`）として立てました。Unit 13 の申し送りの「もう一度立てて構わない」とは別の選び方をしています。
4. **`bad` ／ `worse` ／ `worst` は使いませんでした。** `bad` は既出語になく、`worse` ／ `worst` も `IRREGULAR` に入っていません。この単元の中心は `more` ／ `most` と `as 〜 as` で、不規則変化は Unit 13 で `good` ／ `well` ／ `many` ／ `much` を扱っているため、道具（`IRREGULAR`）を触らずに済ませる判断をしました。**使うときは `bad` を見出し語に立て、`IRREGULAR` に `worse`／`worst → bad` を足してください。**
5. **固有名詞の所有格（`Ken's`・`Miki's`）を避けました。** 語の網羅の検査は、人名そのもの（`Ken`）は固有名詞として除きますが、`Ken's` という形は別の語として数えるため未収録になります。例文を `the distance from his house` に、パートEの設問を `Which is more convenient, the city or the countryside?` ／ `the streets in the countryside` に書きかえました。`my aunt's window` のような一般名詞の所有格は `aunt` に寄るので問題ありません。
6. **`pretty`・`brown`・`stone`・`just`・`chose`・`point` を使いませんでした。** いずれも既出語になく、この単元の内容に要る語でもないため、見出し語を増やさずに本文側を書きかえました（`pretty` を見分け方の表から外す、`brown` → `white`、`stone` → `box`、`just` → `only`、`chose` → `like`、`good points` → `good things`）。
7. **数は20までにしました**（`About twenty percent of the students like spring.`・`The total of the votes was twenty.`）。中1 Unit 11 の数の表現の既出が `twenty` までのため、Unit 13 と同じ判断です。
8. **D21〜D23 の語数を3問すべて8語にそろえました。** `than that one` と `than that question`、`as yours` と `as your bag` のどちらでも正しいため、語数を指定しないと採点がぶれます。解答の解説に「9語になる書き方」も書いてあります。
9. **パートCに `span.hint` で意図する内容を添えました（C15）。** 主語の入れかわりを問う誤文訂正は、直す前の文だけでは「どちらが背が高いのか」が決まらないため、`span.hint` に「ケンのほうが背が高い」と置きました。パートCは和訳を出さないパートなので `class="q-ja"` は使っていません（検査でも和訳なしと判定されています）。
10. **第4部の名前は `UPDATE-PLAN-g2g3.md` の「比較・受動態」のままにしました**（`g2/index.html` は変更していません）。目次で折り返していないため、短くする必要はありませんでした。

### 気になった点（次の回への申し送り）

- **次は順16＝中2 Unit 15（受動態（肯定・否定・疑問）、スラッグ `passive`）です。** `PLAN-g2g3.md` の要注意事項どおり、**be動詞 ＋ 過去分詞で、過去分詞の一覧表を解説に置いてから出題**し（中1 Unit 16 の不規則変化14語に、中2で増えた語の過去分詞を足した形）、**中1 Unit 15 の be動詞の過去形と混ざるので `was cleaned`（受動態）と `was clean`（形容詞）を並べて図解で分け**、`by 〜` は省略できることを明記してください。
- **Unit 15 で受動態（`be` ＋ 過去分詞 ＋ `by`）が使えるようになります。** 今回までの単元では1文も使っていません。`LATER_GRAMMAR_G2` の受動態の正規表現は `\b(am|is|are|was|were)\s+\w+(ed|en)\s+by\b` で、`by` が無い受動態は拾いません。**Unit 15 の回は、`by` の無い受動態も自分で見つける必要があります**（`is made of` などは Unit 16 の内容です）。
- **過去分詞の網羅に注意してください。** `lemma()` は `-ed` を落とす規則を持っていますが、不規則変化の過去分詞（`made`・`written`・`spoken`・`taken`・`known`・`built`・`sold`・`told`・`sent`・`seen`・`eaten`・`given`・`broken` など）は `IRREGULAR` にあるものと無いものが混ざっています。現在 `IRREGULAR` に入っているのは `went/had/did/said/got/saw/ate/made/won/lost/became/built/sold/spent/told/sent/began/used/using/better/best` です。**`written`・`spoken`・`taken`・`known`・`seen`・`eaten`・`given`・`broken` は入っていないので、一覧表に載せるなら `IRREGULAR` に行を足すか、既出語になっているかを確かめてください。** 過去分詞の一覧表そのものが Unit 15 の中心なので、今回のように「語を避ける」対処は取りにくいはずです。
- `worse` ／ `worst` は引き続き `IRREGULAR` にありません（上の判断4）。
- `could` は引き続き使えません（中3 Unit 13 まで）。
- `word-test.html` の中2の語（順18）は中2 Unit 16 まで作ってからです。今回までで中2は500語（Unit 1〜14）。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です。中3 第3部（順34以降）に入る前に、和歌山の過去問で出題の有無を確かめる必要があります。
- **`STATUS.md` をこの回で分割しました。** 追記すると44,668バイトになり、45KB のめやすに届くためです。10-06（昼）より前の記録は `STATUS-archive-2026-10-06.md` に入っています（`update_file` で改名しただけで、中身は1バイトも触っていません）。**リポジトリに反映するときは、改名されたアーカイブとこの新しい `STATUS.md` の両方を置いてください。**

### 飛ばした操作

- **なし。** アップロードした `g2/unit14`・`g2/vocab14`・`g2/index.html`・`tools/master-vocab.json` は Drive の `fileSize` とローカルのバイト数を突き合わせて一致を確認しました。5フォルダ（ルート・units・tools・g2・g3）を一覧し、同名ファイルの重複が無いことを確認しました（`g3/` は空、ルートは23本、`units/` は37本、`tools/` は11本、`g2/` は作業前27本）。回帰検査のため `units/` の37本・`word-test.html`・`tools/tpl-review.html`・`g2/` の Unit 1〜12 の24本を復元し（計63本）、すべて Drive の `fileSize` と一致しました。サブエージェントが「大きすぎて返せなかった」と報告した分も、記録側（`tool-results/*.txt`）から復号して全数そろいました。

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
