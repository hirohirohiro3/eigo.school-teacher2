# 制作の記録

> **2026-10-07（夜）にこのファイルを分割しました。** 新しい記録は上に足しています。 10-07（昼）の順16：中2 Unit 15、10-06（夜）の順15：中2 Unit 14 の記録は `STATUS-archive-2026-10-07.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-06.md`、`STATUS-archive-2026-10-05.md`、`STATUS-archive-2026-10-03.md`、`STATUS-archive-2026-10-02.md`、`STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で改名し、この新しい `STATUS.md` を置いています。** アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブ（`STATUS-archive-2026-10-07.md`）とこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-08（昼の枠／JST。開始 2026-10-08 06:08 UTC ＝ 15:08 JST）　順18：単語テスト `word-test.html` に中2の語を足す

手順5の判定：1番目は通過（`g2/index.html` あり・`--grade` あり・`"g2-N"` のキー）。2番目は Drive の `g2/` に Unit 1〜16 の2本ずつがそろい、復元して `check.py 1`〜`16 --grade 2` がすべて NG 0件。3番目で `word-test.html` に `data-g="2"` の語が無いので、**順18＝単語テストに中2の語を足す回**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `word-test.html` | 変更（58,416 → 105,856バイト）中2の567語を追加・学年の切り替え・中2の URL | ルート |
| `g2/index.html` | 変更（16,809 → 17,215バイト）単語テストのボタン・部のまとめ・中2のまとめを「準備中」からリンクに | g2 |
| `tools/check.py` | 変更（63,452 → 68,053バイト）`--word-test` の学年対応、`--index` の中2以降の共通リンク | tools |
| `tools/gen-word-test.py` | 変更（3,167 → 5,404バイト）中2の単語帳からも機械で一覧を作り、`word-test.html` をその場で書きかえる | tools |
| `STATUS.md` | 変更（この記録） | ルート |

**`index.html`・`tools/build.py`・`tools/master-vocab.json`・テンプレート3本・`units/` の中1のファイル・`g2/` の単元ファイル32本・計画書類は1バイトも変えていません**（`index.html` 17,197／`build.py` 5,512／`master-vocab.json` 10,439（中1のキー479語そのまま）／`tpl-workbook.html` 12,909／`tpl-vocab.html` 16,329／`tpl-review.html` 36,631）。`tools/gen-word-test.tpl.html` も触っていません（下の判断3）。

### 中身

- **語の一覧**：`units/vocab01`〜`16`（中1 479語、`data-g="1"`）のあとに `g2/vocab01`〜`16`（中2 567語、`data-g="2"`）を、学年→単元→単語帳の順で**機械で**並べました（`python tools/gen-word-test.py`）。合計 **1,046語**。**中1の479行は作業前と1文字も変わっていません**（`<li data-g="1"` の行を作業前の写しと diff して確認）。
- **中2の語数**：第1部 145語／第2部 144語／第3部 144語／第4部 134語、合計 567語（`g2/index.html` の部のまとめ・中2のまとめの表示もこの数）。
- **学年の切り替え**：設定画面の「中2」を押せるようにしました（中3は「準備中」のまま）。学年を変えると単元の番号・部・「中2全体」の範囲が切り替わります。問題カードの単元表示は、中1は従来どおり「Unit 5」、中2は「中2 Unit 5」。
- **URL**（`UPDATE-PLAN-g2g3.md` 3節）：中1の `?unit=5`・`?part=2`・`?grade=1` は**そのまま**動きます。中2は `?unit=2-5`・`?part=2-1`・`?grade=2`。これに加えて `?g=2`（設定画面を中2を選んだ状態で開く）を足しました（判断2）。
- **`g2/index.html`**：16単元の「単語テスト」を `../word-test.html?unit=2-N` のリンクに、第1〜4部のまとめの単語テストを `?part=2-N`（語数つき）に、中2のまとめを `?grade=2`（567語）に。共通リンクの先頭の「単語テスト」は `../word-test.html?g=2`、2つめの「単語テスト（中1）」は `../word-test.html?g=1` にしました。総合テストは引き続き「準備中」です。

### 検証結果

- **`check.py --word-test`：23項目 NG 0件**（学年ごとの語数一致 中1 479／中2 567・単語帳との差分0件・並び順一致・同じ単元の中の重複0件・和訳の空0件・学年ごとの部の定義と部ごとの語数・単元名16件ずつ・部の名前4件ずつ・学年の切り替え・URL の読み方・外部読み込み）。［参考］として `take part in 〜`（中2 Unit 2・中2 Unit 12）が出ます（下の「気になった点」）。
- **`check.py --index --grade 2`：15項目 NG 0件**（`wt_ready(2)` が真になり、単語テストのリンクを要求する検査に自動で切り替わったうえで通過）。
- **既存の検査はすべて NG 0件**：中1 `check.py 1`〜`16`・`--index`・`--word-test`・`--review 1`〜`4`・`--review final`（23本）、中2 `check.py 1`〜`16 --grade 2`・`--index --grade 2`（17本）、合計**40本**。**作業前にも同じ40本で NG 0件のベースラインを取りました。**
- **playwright（Chromium・375px）**：`word-test.html` を引数なし・`?unit=5`・`?part=2`・`?grade=1`・`?unit=16`（中1の既存 URL）・`?unit=2-5`・`?part=2-1`・`?grade=2`・`?g=2`・`?unit=2-17`（範囲外→設定画面）の10通りで開き、範囲の表示と学年の選択が正しいこと、**scrollWidth 375px**を確認。中2 Unit 12 を「日本語→英語・全部」で、見出し語の `〜` を `~` に打ちかえて全36問答え、**36/36 正解**。中1 Unit 1 を「英語→日本語」で全33問進めて結果画面まで。中2 Unit 15 の日本語→英語で「文型の形」5語が除かれて27語になり、注記が出ることを確認。`g2/index.html`・`index.html` も 375px で横スクロールなし。**JS の例外0件**（Google Fonts へ接続できないのは作業環境の制限で、ページの不具合ではありません）。

### 自分で判断したこと

1. **記号を含む熟語の見出しの扱い（前回からの申し送り）**：
   - `be ＋ 過去分詞`・`much ＋ 比較級`・`more ＋ 長い形容詞 ＋ than` のように**「＋」や日本語（比較級・過去分詞など）を含む見出し**（中2で9語）は、語ではなく文型の形なので、**一覧には単語帳どおり入れたうえで、日本語→英語では出さない**ことにしました（入力しようがないため）。英語→日本語（自己申告）では出します。見分けは JS が見出し語の文字（「＋」・ひらがな・カタカナ・漢字）で機械的に行うので、単語帳を直せば自動で追従します。日本語→英語を選んだとき、除いた語数を設定画面に注記します。
   - `〜` を含む熟語（`be made of 〜` など）は従来どおり出題し、`〜` を除いて比べます。**`〜ing` は `ing` ごと除く**ようにしました（`How about 〜ing?` は `how about` でも `how about ~ing` でも正解）。`as 〜 as …` の `…` も除きます。中1の見出しには `〜ing`・`…` が無いので、**中1の採点は変わりません**。
2. **`?g=2` を足しました。** `check.py` の `--index` は共通リンクの先頭を `word-test.html` ちょうどにするよう求めていましたが、それだと中2の目次から開いても中1が選ばれた状態になります。`?grade=2` は「中2全体」の出題画面に直行するので、範囲を選ぶ画面用に別の引数が要りました。`?g=学年` は範囲を決めず学年だけを選ぶ引数で、既存の `?unit`・`?part`・`?grade` の意味は変えていません。`check.py` の `--index` も、中2以降の目次は `../word-test.html?g=学年` を求めるように直しました（中1の目次は従来どおり `word-test.html`）。
3. **`gen-word-test.py` は `word-test.html` をその場で書きかえる作りに改めました。** `tools/gen-word-test.tpl.html` は「目次から直接来たときの選択」の改修より古く、これから作り直すと中1のページの機能が落ちます。新しい `gen-word-test.py` は `<ol id="words">` の中身・語数の表示・学年ごとの単元名と部（`UNITS`／`UNITS_G2` など。各学年の目次から取る）だけを差しかえます。**テンプレートのファイルは使わなくなりましたが、消さずに残しています**（ゴミ箱に移すかどうかは人の判断に任せます）。中3の語を足す順41では、`g3/` の単語帳と `g3/index.html` があれば同じスクリプトでそのまま `data-g="3"` と `UNITS_G3` などが入ります（JS 側に `const UNITS_G3=[]` などの受け皿と `GR` への登録を足す必要があります）。
4. **重複している `take part in 〜` は一覧に両方残しました。** 中2 Unit 2 と中2 Unit 12 の単語帳に同じ見出し語・同じ和訳（〜に参加する）で立っています。単元の単語テストは単語帳どおりに出すほうがよいので、一覧からは外さず、`check.py` の重複の判定を「同じ単元の中での重複は NG、別の単元どうしは［参考］」に分けました。中1には重複が無いので中1の判定は変わりません。
5. **中1の目次（`index.html`）は変えませんでした。** 共通リンクの説明（「単元・部・中1全体から範囲を選んで」）は中1の目次としては今も正しく、触らずに済むためです。

### 気になった点（次の回への申し送り）

- **`g2/vocab12_gerund.html` が `take part in 〜` を再び見出し語に立てています**（中2 Unit 2 で既出。`master-vocab.json` の `"g2-2"` と `"g2-12"` の両方に入っています）。Unit 12 の新出語は実質35語です。直すなら Unit 12 の単語帳からこの項目を外し（例文は Unit 12 の動名詞の文脈の別の熟語に差しかえるか、そのまま削る）、`"g2-12"` からも外して、`gen-word-test.py` を走らせ直します。単元の完成品に手を入れる作業なので、今回はしていません。**人が判断してください。**
- **次は順19＝中2の総合テストの道具**（`PLAN-g2g3.md` 5.6。学年別 `REVIEW_SPEC`、`build.py` の `build_review` の学年対応）。今回も `tools/tpl-review.html` と `units/review01`〜`04`・`review-final` を回帰検査のために復元しました。
- `g2/index.html` の冒頭の説明「これから1単元ずつ足していきます。」は、16単元そろったので古くなっています。総合テストの回でまとめて直すとよいと思います（今回は単語テストの範囲外なので触っていません）。
- `IRREGULAR` に入っていない過去分詞（`gone`・`begun`・`drawn`・`kept`・`stood`・`rebuilt`・`worn`・`thrown` など）、`worse`／`worst`、`could` は前回の申し送りのままです。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です（順34以降。今回は通知していません）。

- **アップロードで1回つまずきました。** 最初に上げた `word-test.html` が Drive で12バイト短く、落として突き合わせると、JS の正規表現に書いた文字コードのエスケープ（バックスラッシュと u と16進4桁）が、文字そのものに置きかわっていました（`textContent` で渡す途中で起きる）。そこで**その行をエスケープを使わない書き方（`[...w.en].some(c=>c.charCodeAt(0)>=12352)`、ひらがな以降の文字を含むかどうか）に改め**、検査と playwright をやり直してから上げ直しました。働きは同じです（中1の該当0語、中2の該当9語）。**今後も、アップロードするファイルにバックスラッシュ＋u のエスケープを書かないほうが安全です。**

### 飛ばした操作

- **なし。** 5フォルダ（ルート・units・tools・g2・g3）を一覧し、**同名ファイルの重複が無いことを確認しました**（ルート25本、`units/` 37本、`tools/` 11本、`g2/` 33本、`g3/` は空）。復元は計画書類5本・`index.html`・`word-test.html`・`basic-words.html`・`tools/` の9本・`g2/` の33本・`units/` の37本の**87本**で、**すべて Drive の `fileSize` とバイト数が一致**しました。

---

## 2026-10-07（夜の枠／JST。開始 2026-10-07 16:13 UTC ＝ 10-08 01:13 JST）　順17：中2 Unit 16（受動態の発展（by 以外の前置詞・過去形との識別））

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り）。Drive の `g2/` に Unit 1〜15 の2本ずつがそろい、復元して `python tools/check.py 1`〜`15 --grade 2` がすべて NG 0件。`g2/unit16_*.html` が無い N=16 で止まったので、**順17＝中2 Unit 16（スラッグ `passive-advanced`）**です。これで中2の16単元がそろいました。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit16_passive-advanced.html` | **新規**（49,657バイト） | g2 |
| `g2/vocab16_passive-advanced.html` | **新規**（36,818バイト） | g2 |
| `g2/index.html` | 変更（16,749 → 16,809バイト）Unit 16 をリンクに（`li class="ready"`、単語帳は「35語」） | g2 |
| `tools/master-vocab.json` | 変更（9,999 → 10,439バイト）`"g2-16"` を追加 | tools |
| `STATUS.md` | 変更（分割して新規に立て直し） | ルート |

**`tools/check.py`・`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。** 復元直後のバイト数と作業後のバイト数を突き合わせて確認しました（`check.py` 63,452／`build.py` 5,512／`index.html` 17,197／`word-test.html` 58,416／`tpl-workbook.html` 12,909／`tpl-vocab.html` 16,329／`tpl-review.html` 36,631）。今回は道具に手を入れずに済みました（`IRREGULAR` に足す語がありませんでした）。

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「by 以外の前置詞をとる受動態」（**どの前置詞をとるかは語ごとに決まっていて規則で選ぶものではない**ことを最初に明示）→ **気持ちを表す受動態の表3行**（`be interested in`／`be surprised at`／`be pleased with`。日本語では「〜される」と訳さない）→ **状態を表す受動態の表6行**（`be covered with`／`be filled with`／`be surrounded by`／`be known to`／`be known for`／`be born in`）→ **材料と場所を表す受動態の表3行**（`be made of`／`be made from`／`be made in`）と材料の語の例（`cotton`・`wool`・`bamboo`・`metal`・`silk`）→ 場所や時刻を添える受動態（`Lunch is served at noon in this hall.`）→ **能動態と受動態の書きかえ**（`My brother made this chair.` → `This chair was made by my brother.` の `transform`、手順3つ）→ **代名詞は形が変わる**（`Everyone knows him.` → `He is known to everyone.` の `transform` と `diagram`、**中1 Unit 8 の4格表を再掲**、能動態・受動態・変わった形の3行の対応表）→ **同じ形の過去形と過去分詞を見分ける**（`diagram` と4行の対応表。目印は①前に be動詞があるか ②うしろに目的語があるか）→ 判定手順4段 → 境界事例4つ → 入試での出方 → よくある間違い4つ → まとめ → 例文、の順です。
- `PLAN-g2g3.md` 3節 Unit 16 の3点はすべて入れました：①**by 以外の前置詞を表で置いた**（`be interested in`／`be known to`／`be covered with`／`be made of`／`be made from` を含む、3つの表で合計12形）②**能動態との書きかえで目的語が主語に上がるときの代名詞の格の変化（him → he）を、中1 Unit 8 の4格表を再掲して扱った**（独立した見出し・`transform`・`diagram`・4格表・対応表。誤文訂正 C14 で `Him is known to everyone.` を直させ、並べ替え B9 では不要語 `he` を混ぜた）③**`be made of` と `be made from` の違いを境界事例に置いた**（独立した h3 と4行の対応表。「材料が見た目でわかるかどうか」で分け、A2・A3・C12・D17・D18 で出題）。
- 単元名にある**「過去形との識別」**は独立した見出しで扱いました。Unit 15 の過去分詞の一覧表の2つめ（過去形と同じ形の13語）を土台に、`My father made this desk ten years ago.`（過去形）と `This desk was made by my father.`（過去分詞）を並べ、A4・A5・C15 で出題しています。
- **読解**：エミの発表「紙の村」（山の村の和紙づくりを見学する）。本文156語（めやす 120〜160語）。下線部①が `Paper from wood is cheap, but this paper is made by hand, so it is more expensive.`（和訳）、②が `I was not pleased with his last words.`（そう感じた理由の選択）。`be known for`・`be known to`・`be made from`・`be covered with`・`be surprised at`・`be pleased with` を本文の中で使い、`by` を使わない受動態（`are cut and boiled`・`are washed`・`is dried`・`is used`）を重ねました。
- **単語帳**：新出語 **35語**（めやす30〜40語）。動詞4（cover fill surround serve）・名詞16（material metal wood cotton wool silk cloth cheese ice oil tool step thousand bamboo noon flag。うち thousand は数詞のタグ）・形容詞3（interested pleased born）・熟語12（be interested in／be surprised at／be pleased with／be covered with／be filled with／be surrounded by／be known to／be known for／be born in／be made of／be made from／be made in）。累計は中1 479語＋中2 567語＝**1,046語**（`PLAN-g2g3.md` 2節の中2の見込み「約550語」にほぼ一致）。

### 検証結果

- **`check.py 16 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・見出し語35語・重複なし・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳4ページ）。**［参考］の「解説に出ていない出題語」も0語**にしました（最初は9語＝`club, hall, lunch, music, noon, paper, river, school, served` が出たので、解説側に `Lunch is served at noon in this hall.`・`Our school is known for its music club.`・`Paper is made from wood.`・`In winter the river is covered with ice.` を置いて解消）。
- **後続文法の検査**（`LATER_GRAMMAR_G2` のうち first が17以上＝中3分（99）を、誤答例の行と打ち消し線を除いたワークブックの英文4,858字に当てる）：**当たり0件**。現在完了・`too 〜 to`／`so 〜 that`・人 ＋ to・間接疑問・関係代名詞・仮定法・付加疑問はすべて0件。**中2 Unit 16 は中2の最終単元なので、first が16以下の形（受動態・比較・不定詞など）はすべて範囲内です。**
- **既存の検査はすべて NG 0件**：中1 `check.py 1`〜`16`・`--index`・`--word-test`・`--review 1`〜`4`・`--review final`（23本）、中2 `check.py 1`〜`16 --grade 2`・`--index --grade 2`（17本）。合計**40本で NG 0件**です。**作業に入る前にも Unit 16 を除く39本を走らせて NG 0件のベースラインを取ってあります。**
- **`master-vocab.json`**：中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-15"` は復元直後の写しとキーごとに突き合わせて**完全に一致**（変更された既存キー0件）。増えたのは `"g2-16"` の35語だけです。
- **playwright（Chromium）**：`g2/unit16`・`g2/vocab16`・`g2/index.html`・`g2/unit15`・`index.html`・`word-test.html`・`units/review01`・`review04`・`review-final`・`units/unit08`（4格表の比較用）の10本を375px幅で開き、**scrollWidth 375px・JS の例外0件**（テストページは選択肢・入力欄・ボタンを操作したあとも0件）。新しい2本に `<script>` は0件、外部読み込みは Google Fonts だけ。**未定義クラス0件**（インラインの `<style>` の定義と `class` 属性を突き合わせて確認。`@media print` の中の定義も拾う方法に直してから数えています）。

### 自分で判断したこと

1. **中1 Unit 8 の4格表は、列を削らずそのまま再掲しました。** この表だけは375px幅で `.table-wrap` の中が横に広がります（はみ出す要素8個）。ただし**中1 Unit 8 の原本もまったく同じ8要素がはみ出していて**（同じ表なので当然です）、**ページ自体の横スクロールは出ていません**（`scrollWidth` 375px ＝ `clientWidth`）。`.table-wrap` は中身を横に流して見せるための枠なので、これは設計どおりの振るまいです。受動態の書きかえで要るのは主格と目的格の2列だけなので列を減らすことも考えましたが、`PLAN-g2g3.md` が「中1 Unit 8 の4格表を再掲する」と書いているので、**原本と同じ形を保つほうを選びました**。CSS は触っていません。
2. **`thousand` は数詞（`t-num`）のタグで立てました。** 中1 Unit 11 の数の表現で `twenty` までが既出で、`hundred` もすでに数詞として入っています。それにそろえました。例文は `This temple was built about a thousand years ago.` で、Unit 15 の「約400年前」から数を1つ増やす形です。
3. **`born` は形容詞のタグで立てました。** `bear` の過去分詞ですが、原形 `bear` は中学では使わず、いつも `be born` の形で出ます。原形を見出しに立てると使えない語が1つ増えるので、`born`（生まれた）を形容詞として立て、メモに「いつも `be born` の形で使う」と書きました。
4. **`pleased` を見出し語に立てました。** `lemma()` は `pleased` → `please` に寄せるので、検査の上では既出語 `please`（どうぞ）でカバーされてしまい、未収録になりません。ですが `please`（副詞・動詞）と `pleased`（形容詞「満足している」）は別の語なので、`README.md` の「別の単元で別の品詞として出てきたら改めて立てる」に従って立てました。Unit 14 の `more` の判断（熟語の見出しに回す）とは別の選び方をしています。
5. **受動態の形を熟語として12立てました。** Unit 15 で6つ立てたのと同じ扱いです。単語が23語で、形の熟語を足して35語です。**前置詞が語ごとに決まっていることがこの単元の中心なので、`be known to` と `be known for` のように前置詞だけがちがう形も別の見出しに分けました**（意味がちがうので、入試でも区別が問われます）。
6. **`be surrounded by` を足しました。** `PLAN-g2g3.md` が挙げている5つ（`in`／`to`／`with`／`of`／`from`）には入っていませんが、`surround` は `with` と書く間違いが多く、**「by 以外の前置詞をとる」という思い込みへの反例**として要ると判断しました（A1・C16 で出題。よくある間違いの4つめにも置いています）。
7. **`silk`・`wool`・`cotton`・`bamboo`・`metal`・`wood` の6語を材料の語としてまとめて入れました。** `be made of` の出題はすべてこの6語の範囲に収めてあり、解説の表と本文に全語が出ています。`be made of` の熟語のメモにも6語を並べました。
8. **数えられない名詞の扱いを境界事例に1つ置きました。** `oil`・`ice`・`metal`・`cotton`・`wool`・`silk`・`bamboo`・`cheese` はいずれも `a` をつけず複数形にもしないため、中1 Unit 4 の扱いと同じであることを1か所でまとめて書きました（語ごとのメモにも書いています）。
9. **読解の題材を和紙にしました。** `be made from`（材料の形が変わる）・`be known for`（産地）・`be covered with`（氷）・`be surprised at`（手順の数）・`be known to`（全国に知られている）・`be pleased with`（否定形）を1本の文章に自然に入れられるためです。固有名詞は `Japan` だけで、`washi` のようなローマ字の語は語の網羅の検査で未収録になるので使わず、`Japanese paper` と書いています。
10. **`spoon`・`shirt`・`kimono` は使いませんでした。** いずれも既出語になく、この単元の内容に要る語でもないので、本文側を既出語（`box`・`bag`・`cloth`）に書きかえました。
11. **本文に `<div class="sheet">` を書いてしまい、検査では気づけなかったので目で見つけて直しました。** テンプレート（`tpl-workbook.html` 394行目・`tpl-vocab.html` 271行目）が `{{BODY}}` の前に `<div class="sheet">` を置いているので、**本文（`build.py` に渡す body）には `sheet` の div を書きません。** 最初の版は二重になっていて（`<div class="sheet">` が2つ）、`check.py` の17項目も playwright もすべて通っていました（入れ子でも表示は変わらないため）。**中1・中2の既存の単元ファイルはすべて1つ**なので、そろえるために本文から外して組み直しました。この分だけサイズが減っています（ワークブック 49,685 → 49,657／単語帳 36,845 → 36,818、どちらも `<div class="sheet">\n` の20バイトと `</div>\n` の7バイト）。組み直したあとに `check.py` 40本・後続文法・`master-vocab.json` の突き合わせ・playwright をすべてやり直し、結果は同じです。**次の回も、本文には `sheet` の div を書かないでください。**

### 気になった点（次の回への申し送り）

- **次は順18＝単語テスト `word-test.html` に中2の語を足す回です**（`PLAN-g2g3.md` 5.5）。中2の16単元がこれでそろいました。今回までで中2は**567語**（Unit 1〜16）、中1と合わせて**1,046語**です。語の一覧は `g2/vocab01_*.html`〜`vocab16_*.html` から**機械で**作ってください（`check.py` の `vocab_pairs()` が `<span class="v-word">` と `v-sense` の `<p>` から（見出し語, 和訳）を取り出します。`<span class="sub">` の補足は除かれます）。
- **URL の決まりは `UPDATE-PLAN-g2g3.md` の3節のとおりです**：中1の `?unit=5`・`?part=1` は**そのまま**（生徒に渡した URL を切らない）、中2は `?unit=2-5`・`?part=2-1`・`?grade=2`。`build.py` の `build_review()` にすでに `tag = "" if grade == 1 else "%d-" % grade` の形で同じ決まりが入っているので、そろえてください。
- **熟語の見出しの扱いに注意してください。** 中2の567語のうち、`be ＋ 過去分詞`・`be made of 〜`・`as 〜 as …` のように**日本語の記号（〜・＋）を含む見出しが多数あります**（Unit 13〜16 だけで30近くあります）。単語テストにそのまま出すと答えようがない形が混ざります。**`PLAN-g2g3.md` 5.5 の指示を読んだうえで、記号を含む見出しを出題対象にするかどうかをその回で決めて、`STATUS.md` に書いてください。**
- **`g2/index.html` の「単語テスト」は16単元すべて「準備中」のままです。** 順18 で中2の語を足したら、`check.py` の `--index --grade 2` の「共通リンクの先頭が単語テスト（この学年の語がまだ無いので準備中）」の判定も合わせて変える必要があります（`wt_ready()` を見てください）。
- 順19（中2の総合テストの道具）に入る前に、`tools/tpl-review.html` と `units/review01.html` を復元しておくと速いです。今回も回帰検査のために両方復元してあります。
- **`IRREGULAR` に入っていない過去分詞**：`gone`・`begun`・`drawn`・`kept`・`stood`・`rebuilt`・`worn`・`thrown` などはまだ入っていません（中3 Unit 1 の現在完了の表で要ります）。`worse` ／ `worst` も引き続きありません。`could` は引き続き使えません（中3 Unit 13 まで）。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です。中3 第3部（順34以降）に入る前に、和歌山の過去問で出題の有無を確かめる必要があります。**まだ先（順26 から中3 Unit 1）なので、今回は通知していません。**

### 飛ばした操作

- **なし。** 5フォルダ（ルート・units・tools・g2・g3）を一覧し、**同名ファイルの重複が無いことを確認しました**（ルートはファイル25本、`units/` は37本、`tools/` は11本、`g2/` は作業前31本、`g3/` は空）。回帰検査のため `units/` の37本・`word-test.html`・`basic-words.html`・`UPDATE-PLAN.md`・`tools/tpl-review.html`・`g2/` の Unit 1〜15 の30本と `g2/index.html` を復元し、**すべて Drive の `fileSize` とバイト数が一致**しました（復元 71本）。

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
