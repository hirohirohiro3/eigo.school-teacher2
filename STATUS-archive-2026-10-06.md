# 制作の記録

> **2026-10-05（夜）にこのファイルを分割しました。** 10-04（昼）の順10：中2 Unit 9、10-04（夜）の順11：中2 Unit 10、10-05（昼）の順12：中2 Unit 11 の記録は `STATUS-archive-2026-10-05.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-03.md`、`STATUS-archive-2026-10-02.md`、`STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で改名し、この新しい `STATUS.md` を置いています。** アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブ（`STATUS-archive-2026-10-05.md`）とこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-06（昼の枠／JST。開始 2026-10-06 06:08 UTC ＝ 15:08 JST）　順14：中2 Unit 13（比較級・最上級 -er / -est）

手順5の判定：1番目（道具の改造）は通過。N=1〜11 は Drive に `g2/unit*`・`vocab*` がそろい、前回の記録で NG 0件（今回も復元して `check.py N --grade 2` を走らせ、1〜12 すべて NG 0件）。`g2/unit13_*.html` が無い N=13 で止まったので、**順14＝中2 Unit 13（スラッグ `comparative-er`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit13_comparative-er.html` | **新規**（51,934バイト） | g2 |
| `g2/vocab13_comparative-er.html` | **新規**（34,822バイト） | g2 |
| `g2/index.html` | 変更（16,591 → 16,647バイト）Unit 13 をリンクに（`li class="ready"`、単語帳は「31語」） | g2 |
| `tools/check.py` | 変更（61,958 → 62,843バイト）`lemma()` に比較級・最上級の語尾の処理、`IRREGULAR` に `better`／`best → good`（※下の「気になった点」の空行1行の件も参照） | tools |
| `tools/master-vocab.json` | 変更（8,829 → 9,156バイト）`"g2-13"` を追加 | tools |
| `STATUS.md` | 変更（追記） | ルート |

**`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。**

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「2つをくらべる：比較級 ＋ than」（`Ken is tall.` → `Ken is taller than Taro.` の `transform` と `diagram`、もとの文との対応表、なぜ than が要るか）→「3つ以上の中でいちばん：the ＋ 最上級」（`transform`・`diagram`、なぜ the がつくか＝中1 Unit 4 の「1つに決まるものには the」）→ **in と of の使い分け表** →「-er / -est の作り方」（**綴りルール表4行**：ふつう／e で終わる／短い母音＋子音1字／子音字＋y。中1 Unit 14 の子音字重ね・中1 Unit 4 の y→i と同じきまりであることを明記）→「形が大きく変わる語」（**good/well-better-best、many/much-more-most**）→「**than のうしろの代名詞**」（`taller than I am` と `taller than me` の両方を表で。動詞を続けるなら主語の形、1語だけなら目的語の形）→「くらべる疑問文と答え方」（Which／Who、`like 〜 better`／`like 〜 the best`）→ 判定手順4段 → 境界事例4つ（much ＋ 比較級／one of the ＋ 最上級 ＋ 複数形／副詞の比較／than のうしろをそろえる `yours`）→ 入試での出方 → よくある間違い4つ → まとめ → 例文、の順です。`PLAN-g2g3.md` 3節 Unit 13 の3点（綴りルール表・than のうしろの格・the と in / of）はすべて入れました。
- **読解**：ユイの発表「いちばん好きな季節」（クラス20人の調査。春8・夏6・秋4・冬2票）。本文156語（めやす 120〜160語）。下線部①が `Winter is colder than the other seasons, but the stars look brighter on winter nights.`（和訳）、②が `I like spring the best, but now I like winter better than before.`（内容の選択）。E4 は `Spring got two (　) votes than summer.` に `more` を入れる空所補充です。
- **単語帳**：新出語 **31語**（めやす30〜40語）。比較の語5（than more most better best）・名詞14（season autumn survey vote number boy girl banana tower moon planet size race road）・形容詞8（bright deep low weak slow smart gentle black）・熟語4（much ＋ 比較級／one of the ＋ 最上級 ＋ 複数形／like 〜 better than …／like 〜 the best）。累計は中1 479語＋中2 464語＝**943語**。

### 検証結果

- **`check.py 13 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・見出し語31語・重複なし・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳4ページ）。
- **後続文法の検査**（`LATER_GRAMMAR_G2` のうち first が14以上の形と中3分（99）を、誤答例の行・選択肢・パートCの問題文を除いた本文に1文ずつ当てる）：**当たり0件**。`as` は本文に1語も無し（`as 〜 as` は Unit 14）。`more`／`most` は `many`／`much` の比較級・最上級としてだけ使い（`more books`・`more votes`・`the most votes`）、**`more` ＋ 形容詞（Unit 14 の内容）は誤答の選択肢とパートCの誤文（`more heavy`）以外では使っていません**。受動態・現在完了・too 〜 to・so 〜 that・関係代名詞・間接疑問・could も0件。
- **既存の検査はすべて NG 0件**：中1 `check.py 1`〜`16`・`--index`・`--word-test`・`--review 1`〜`4`・`--review final`、中2 `check.py 1`〜`12 --grade 2`・`--index --grade 2`（計36本）。Unit 13 を足した37本でも NG 0件。**`check.py` を変える前（復元直後の61,958バイト版）と後の両方で同じ36本を走らせて `diff` を取り、違いは中1 Unit 13 の［参考］「解説に出ていない出題語」から `sings` が1語減った1行だけ**でした（［参考］は NG にならない項目）。
- **`master-vocab.json`**：中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-12"` は復元直後の写しとキーごとに突き合わせて**完全に一致**（変更された既存キー0件）。増えたのは `"g2-13"` の31語だけです。回帰検査で全単元を走らせたあとも内容が変わらないことを `cmp` で確認しました。
- **playwright（Chromium）**：`g2/unit13`・`g2/vocab13`・`g2/index.html`・`g2/unit12`・`index.html`・`word-test.html`・`units/review01`・`review04`・`review-final` の9本を375px幅で開き、**scrollWidth 375px・はみ出した要素0個・JS の例外0件**（テストページは選択肢・ボタン・入力欄を操作したあとも0件）。新しい2本と `g2/index.html` に `<script>` は0件、外部読み込みは Google Fonts だけ。**未定義クラス0件**。

### 自分で判断したこと

1. **`check.py` の `lemma()` に比較級・最上級の語尾の処理を足しました。** これまで `-er`／`-est` を見出し語に寄せる処理が無く、`taller`・`bigger`・`easier`・`largest` などが既出語の `tall`・`big`・`easy`・`large` でカバーされませんでした。この単元は比較級・最上級そのものが主題なので、語ごとに `IRREGULAR` へ足すのではなく、`-ing`・`-ed` と同じ形の規則（`-er`/`-est` を落とす・`-r`/`-st` だけ落とす（e で終わる語）・重ねた子音字を落とす・`-ier`/`-iest` を y に戻す）にしました。Unit 14 以降と総合テストでも同じ形が出るためです。`better`／`best` は `IRREGULAR` で `good` に寄せています。**候補を足すだけの変更なので NG を増やす向きには働かず、変更前後で36本の出力の差は［参考］の1行だけでした。** 副作用として `player`→`play` のような「動詞＋er の名詞」も網羅の上では既出の動詞でカバーされるようになります（見出し語の数え方は変わりません）。
2. **`more`／`most`／`better`／`best` を見出し語に立てました。** `better`／`best` は `good` に寄せればカバーされますが、形ごと覚える語なので単語帳に載せています。`more`／`most` は今回 `many`／`much` の比較級・最上級（形容詞）として立てました。**Unit 14 で「`more` ＋ 長い形容詞」の副詞の用法を扱うときは、`README.md` の「別の単元で別の品詞として出てきたら、そこで改めてエントリを立てる」どおり、もう一度立てて構いません**（見出し語の重複検査は単元の中だけです）。
3. **`boy`・`girl`・`black`・`banana` が既出語に無かったので見出し語にしました。** 中1で使われていない（`master-vocab.json` の累計に無い）ことを確かめたうえで、比較の例文（`the tallest of the five boys`・`the tallest girl`・`apples or bananas`・`The black cat is smaller than the white one.`）に載せています。
4. **`Japan` は並べかえの語群でも大文字のままにしました。** 語群は「文の最初に来る語も小文字」の約束ですが、固有名詞は文の位置に関係なく大文字なので、小文字にすると別の語になります（`japan` だと網羅の検査でも未収録になる）。
5. **`-er`／`-est` を解説の日本語の中で書くときは、必ずハイフンつき（`-er`・`-est`・`-r`・`-st`）にしました。** ハイフンなしの `er`／`est`／`st` は網羅の検査が語として数えてしまうためです（`check.py` は `-` で始まる語尾表記を除く作り）。
6. **`like 〜 better`／`like 〜 the best` の `better`／`best` は `well` の比較級・最上級である、と解説に書きました。** `good` の形に見えて迷う生徒が多いところなので、意味（「より強く」「いちばん強く」好き）とあわせて一言入れています。
7. **D21（`My sister is older than me.`）は語数を6語に固定し、「代名詞1語で文を終える」と条件に書きました。** `than I am` も正しいので、条件が無いと6語と7語の両方が正解になり採点がぶれるためです。解答の解説に `than I am` なら7語になることを書いています。
8. **数は20までにしました**（読解の調査は20人・8／6／4／2票）。中1 Unit 11 の数の表現の既出が `twenty` までのため、前回の `eighty` と同じ判断です。

### 気になった点（次の回への申し送り）

- **次は順15＝中2 Unit 14（more / most と as 〜 as、スラッグ `comparative-more`）です。** `PLAN-g2g3.md` の要注意事項どおり、more / most をつける語（長い形容詞・副詞）の見分け方、**as 〜 as の中は原級であること、not as 〜 as が比較級の書き換えになること**、書き換え問題（`A is taller than B` ↔ `B is not as tall as A`）は**主語が入れ替わる**ので誤文訂正で必ず1問出してください。
- **Unit 14 で `as 〜 as` が使えるようになります。** 今回までは `as` を1語も使っていません。受動態は Unit 15 まで使えません。
- **`more beautiful`・`most popular` などの「`more`／`most` ＋ 形容詞」は今回1つも使っていません**（誤答の選択肢と誤文の `more big`／`more high`／`more early`／`more heavy` を除く）。Unit 14 で最初に出す形です。`more`／`most` は今回 `many`／`much` の形として見出し語にしてあります（上の判断2）。
- `lemma()` に `-er`／`-est` の処理が入ったので、Unit 14 以降の比較級・最上級（`longer`・`hottest` など）はそのまま既出語でカバーされます。`worse`／`worst`（bad の比較）は `IRREGULAR` に入れていません。使うときは `bad` を見出し語にするか既出か確かめたうえで、`IRREGULAR` に1行足してください。
- **`check.py` のアップロードで、`check_vocab()` の末尾（`return heads` の直前）の空行が1行落ちました**（`textContent` での転記による。Drive の `fileSize` 62,843 とローカル 62,844 の差で気づき、Drive から落とし直して `diff` で確認）。動作には関係しないので、**Drive 側（空行なし・62,843バイト）を正としてローカルも同じにし、そのうえで37本の検査を走らせ直して全部 NG 0件**を確かめています。リポジトリへはこの版を反映してください。
- `could` は引き続き使えません（中3 Unit 13 まで）。
- `word-test.html` の中2の語（順18）は中2 Unit 16 まで作ってからです。今回までで中2は464語（Unit 1〜13）。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です。

### 飛ばした操作

- **なし。** アップロードした `g2/unit13`・`g2/vocab13`・`g2/index.html`・`tools/master-vocab.json`・`tools/check.py` は Drive から落とし直してローカルと `cmp` で一致を確認しました。5フォルダ（ルート・units・tools・g2・g3）を一覧し、同名ファイルの重複が無いことを確認しました（`g3/` は空、ルートは23本、`units/` は37本、`tools/` は11本、`g2/` は作業前25本）。回帰検査のため `units/` の37本・`word-test.html`・`tools/tpl-review.html`・`g2/` の Unit 1〜12 の24本も含めて計75本を復元し、すべて Drive の `fileSize` と一致しました。サブエージェントが「大きすぎて保存された」と報告した分も、記録側（`tool-results/*.txt`）から復号してそろっています。

---

## 2026-10-05（夜の枠／JST。開始 2026-10-05 16:13 UTC ＝ 10-06 01:13 JST）　順13：中2 Unit 12（動名詞）

手順5の判定：1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り）は通過。N=1〜11 は Drive に `g2/unit*_*.html`・`vocab*_*.html` がそろい、復元して `python tools/check.py N --grade 2` を走らせ、1〜11 すべて NG 0件。`g2/unit12_*.html` が無い N=12 で止まったので、**順13＝中2 Unit 12（スラッグ `gerund`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit12_gerund.html` | **新規**（49,886バイト） | g2 |
| `g2/vocab12_gerund.html` | **新規**（37,989バイト） | g2 |
| `g2/index.html` | 変更（16,551 → 16,591バイト）Unit 12 をリンクに（`li class="ready"`、単語帳は「36語」） | g2 |
| `tools/check.py` | 変更（61,861 → 61,958バイト）`IRREGULAR` に `using → use` の1行を追加 | tools |
| `tools/master-vocab.json` | 変更（8,375 → 8,829バイト）`"g2-12"` を追加 | tools |
| `STATUS.md` | 変更（追記） | ルート |

**`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。**

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「動詞を <code>-ing</code> にして名詞のはたらきをさせる」（`I like tennis.` → `I like playing tennis.` の `transform`、`I like → playing tennis` の `diagram is-general`、**主語／動詞の目的語／be動詞のうしろ／前置詞の目的語**の4つの位置の表、**「-ing 形になった動詞は動詞そのものとしては働かない」という中1 Unit 14 の言い回しをそのまま使った理由づけ**）→「`-ing` 形の作り方」（中1 Unit 14 と同じ3行の綴りルール表＋重ねない語）→「`to` ＋ 原形と動名詞の使い分け」→「前置詞のうしろは動名詞」→ 判定手順4段 → 境界事例4つ → 入試での出方 → よくある間違い4つ → まとめ → 例文、の順です。
- `PLAN-g2g3.md` 3節 Unit 12 の4点はすべて入れました：①**使い分け表**（`enjoy`／`finish`／`stop`／`practice` は動名詞のみ、`want`／`hope`／`decide`／`need` は不定詞のみ、`like`／`start`／`begin`／`love` はどちらも）②**前置詞のうしろは動名詞を独立した見出しで扱った**（`be good at 〜ing` ほか8行の表。`instead of` と `look forward to` の `of`／`to` が前置詞であることを本文で注意喚起）③**`stop to 〜` と `stop 〜ing` を境界事例の先頭に置いた** ④**綴りルールは中1 Unit 14 の表を流用**。
- **読解**：ミサキのスピーチ「海岸でのそうじ」（ボランティア部で毎月、町の近くの海岸をそうじする）。本文144語（めやす 120〜160語）。下線部①が `Picking up trash on the sand is hard work.`（和訳）、②が `I will never give up cleaning the coast.`（`cleaning` と同じはたらきの `-ing` を最後の2文から1語で書きぬく）。E3 は `What did Misaki begin reading about the sea?` に `Articles about the sea.` と3語で答えさせる設問です。
- **単語帳**：新出語 **36語**（めやす30〜40語）。名詞14（coast sand wave shell trash activity habit effort collection coin instrument topic article poster）・動詞9（avoid imagine mind recycle reduce record succeed fail waste）・熟語10（be good at 〜ing／be interested in 〜ing／be afraid of 〜ing／give up 〜ing／How about 〜ing?／look forward to 〜ing／instead of 〜ing／without 〜ing／take part in 〜／Thank you for 〜ing.）・形容詞3（active creative patient）。**熟語を10本そろえたのは、この単元の中心が「前置詞のうしろは動名詞」だからです。** 累計は中1 479語＋中2 433語＝**912語**。

### 検証結果

- **`check.py 12 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・見出し語36語・重複なし・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳4ページ）。
- **後続文法の検査**（`LATER_GRAMMAR_G2` のうち first が13以上の形と中3分（99）を、英文462本＝`<span class="en">`・解答キー・読解本文の文・`span.hint`、に1文ずつ当てる。誤答例の行・選択肢・パートCは除く）：**当たり0件**。`than`／`more`／`most`／`better`／`best`・`the 〜est`・`as 〜 as`・受動態・現在完了・`too 〜 to`／`so 〜 that`・人 ＋ to・人 ＋ 原形・間接疑問・関係代名詞・仮定法・付加疑問はすべて0件。
- **中1の既存の検査はすべて NG 0件**：`check.py 1`〜`16`・`--index`・`--word-test`・`--review 1`〜`4`・`--review final`。**`check.py` を変える前（復元直後の61,861バイト版）と後の両方で同じ27＋5＋11項目を走らせ、出力に差分が無いことを `diff` で確認しています**（`--no-render` で比較）。
- **中2の既存の検査もすべて NG 0件**：`check.py 1`〜`11 --grade 2`・`--index --grade 2`。
- **`master-vocab.json`**：中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-11"` は復元直後の写し（8,375バイト）とキーごとに突き合わせて**完全に一致**（変更された既存キー0件）。増えたのは `"g2-12"` の36語だけです。
- **playwright（Chromium）**：`g2/unit12`・`g2/vocab12`・`g2/index.html`・`g2/unit11`・`index.html`・`word-test.html`・`units/review01`・`review04`・`review-final` の9本を375px幅で開き、**scrollWidth 375px・はみ出した要素0個・JS の例外0件**（テストページは入力・ボタン・選択肢をすべてクリックしたあとも0件）。`file://` から Google Fonts を取りに行く通信だけが失敗しますが、実行環境に外へ出る経路が無いためで、ページの不具合ではありません。
- **未定義クラス0件**（本文の `class="..."` をテンプレートの CSS と突き合わせ）。新しい2本と `g2/index.html` に `<script>` は0件、外部読み込みは Google Fonts だけ。

### 自分で判断したこと

1. **`check.py` の `IRREGULAR` に `using → use` を足しました。** 文法ではなく `lemma()` の穴です。`lemma()` は `-ing` を落とす処理に `len(w) > 5` の条件があるため、**5文字の `using` だけが `use` に寄らず**、既出語の `use`（中1 Unit 5）でカバーされませんでした（`taking`・`making`・`saying` などは6文字以上なので通ります。`doing`・`going` は見出し語・熟語の語として既に積まれているため別経路で通っていました）。`instead of using plastic bags` は「前置詞のうしろは動名詞」の表に要る文なので、語を避けるのではなく道具側を直しました。**10-04（夜）の `used → use` と同じ対処です。カバー範囲が増えるだけの変更なので既存の検査を落とす向きには働きません**が、変更前後で中1・中2の全検査を走らせて出力が同一であることを `diff` で確認しています。他に5文字の `-ing` 形（`being` など）が出たときも同じ対処で構いません。
2. **`drew` を選択肢から外しました。** A3 の誤答に `drew`（draw の過去形）を置いたところ、`lemma()` が `draw` に寄せず語の網羅で未収録になりました。`draw` は中1 Unit 13 の既出語ですが、不規則変化の `drew` は `IRREGULAR` にありません。ここは文法でも `lemma()` の穴でもなく**ただの誤答選択肢**なので、道具を触らず `draws`（三単現）に差しかえました。三単現も「名詞の位置に動詞をそのまま置けない」ことを問う誤答として同じだけ働きます。
3. **`eighty` を使わないことにしました。** `My grandmother is still active at eighty.` と書いたところ `eighty` が未収録でした（中1 Unit 11 の数の表現は `twenty` までが既出）。1語のために見出し語を増やさず、`My grandmother is still active.` にしています。
4. **`video` を見出し語から外し、`poster` を入れました。** 下書きでは `video` を立てて `poster` を落としていましたが、`poster` は読解本文に出る語なので網羅に要ります。36語の枠を動かさずに入れかえ、例文は `We made a poster for the school festival.`（読解と同じ文）にしました。`video` は使っていません。
5. **熟語を10本に増やしました。** 中2 Unit 1〜11 は熟語が5本前後でしたが、この単元は「前置詞のうしろは動名詞」が中心で、入試で問われるのは個々の熟語の形そのものです。`be good at`／`be interested in`／`be afraid of`／`Thank you for`／`How about`／`without`／`instead of`／`look forward to`／`give up`／`take part in` を見出し語に立て、どれもメモで「うしろは動名詞」を明記しました。名詞を14本に増やして全体の配分を保っています。
6. **`look forward to 〜ing` の `to` を本文で2回注意しました**（前置詞のうしろの表の直後の段落と、よくある間違いの4つ目）。形が不定詞の `to` と同じで、ここが入試で最も狙われるためです。
7. **`Do you mind 〜ing?` の答え方を `No, I don't.` と書きました。** 日本語の「はい」と答えが逆になる形なので、メモに「＝いやではありません」を添えています。出題はしていません（解説の範囲にとどめた）。
8. **B の「1語不要」の不要語はどちらも `to` にしました。** この単元の誤りの中心が「前置詞のうしろに `to` を入れてしまう」ことなので、B9（`be good at`）と B10（`How about`）で同じ不要語を2回出し、形として定着させています。
9. **E5 は2つの正解を認めました。** 「最後の2文から `cleaning` と同じはたらきの `-ing` を1語」と問うと、`protecting` と `listening` の両方が当てはまります。どちらも前置詞のうしろの動名詞なので、解答に両方正解と書いています。

### 気になった点（次の回への申し送り）

- **次は順14＝中2 Unit 13（比較級・最上級（-er / -est）、スラッグ `comparative-er`）です。** `PLAN-g2g3.md` の要注意事項どおり、**綴りルール表**（-er / -est、y→ier、子音重ね、good-better-best と many/much-more-most の不規則）を解説に置き、**`than` のうしろの代名詞の格**（`taller than I (am)` と `than me` の両方が使われること）に触れ、最上級の `the` と `in / of` の使い分けを扱ってください。**Unit 13 から第4部（比較・受動態）に入ります。**
- **Unit 13 で `than`・`more`・`most`・`better`・`best`・`the 〜est` が正面から使えるようになります。** 今回までの単元では1語も使っていません。`as 〜 as` は Unit 14 まで、受動態は Unit 15 まで使えません。
- `could` は引き続き使えません（中3 Unit 13 まで）。方角の語（east など）も未収録のままです。
- `lemma()` の穴は `-ed`（4文字）と `-ing`（5文字）の2つが出ました。**`being` が必要になったときも `IRREGULAR` に `being → be` を足す対処で構いません。** 不規則変化の過去形（`drew` など）は語の網羅の都合だけで道具に足さず、本文側で避けるほうを選んでいます。
- `word-test.html` の中2の語（順18）は中2 Unit 16 まで作ってからです。今回までで中2は433語（Unit 1〜12）。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です。順26（中3 Unit 1）までは着手に影響しません。

### 飛ばした操作

- **なし。** 5フォルダ（ルート・units・tools・g2・g3）を一覧し、同名ファイルの重複が無いことを確認しました（`g3/` は空、ルートは23本、`units/` は37本、`tools/` は11本、`g2/` は作業前23本）。回帰検査のため `units/` の37本・`word-test.html`・`tools/tpl-review.html`・`g2/` の Unit 1〜11 の22本も復元し、すべて Drive の `fileSize` と一致しました（計70本）。サブエージェントが「大きすぎて返せなかった」と報告した分も、記録側（`tool-results/*.txt`）から復号して全数そろいました。

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
