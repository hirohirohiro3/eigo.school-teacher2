# 制作の記録

> **2026-10-18（昼の枠）にこのファイルを分割しました。** 新しい記録は上に足しています（最新は 2026-10-19（夜）の順36：中3 Unit 11 の完成。次は順37：中3 Unit 12）。**判断の材料（学習指導要領の根拠）は `STATUS-archive-2026-10-18.md` の 2026-10-17（夜）の記録にあります。** 10-15（夜）の順33：中3 Unit 8 と、10-16〜10-17 の判断待ち停止の記録も `STATUS-archive-2026-10-18.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-15.md`、`STATUS-archive-2026-10-14.md`、`STATUS-archive-2026-10-13.md`、`STATUS-archive-2026-10-11.md`、`STATUS-archive-2026-10-10.md`、`STATUS-archive-2026-10-08.md`、`STATUS-archive-2026-10-07.md`、`STATUS-archive-2026-10-06.md`、`STATUS-archive-2026-10-05.md`、`STATUS-archive-2026-10-03.md`、`STATUS-archive-2026-10-02.md`、`STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 古い `STATUS.md` を `update_file` で `STATUS-archive-2026-10-18.md` に改名し、この新しい `STATUS.md` を置いています。リポジトリに反映するときは、改名されたアーカイブとこの新しい `STATUS.md` の両方を置いてください。

---

## 2026-10-19（夜の枠／JST。開始 2026-10-19 16:04 UTC ＝ 2026-10-20 1:04 JST）　順36：中3 Unit 11「関係代名詞（主格 who / which / that）」を作成

手順5の判定：Drive の5フォルダ（ルート・units・tools・g2・g3）を全ページ一覧し、判定の1〜7番目は通過（`g2/index.html` あり、`check.py --help` に `--grade` あり、`master-vocab.json` は学年別キー（`"1"`〜`"16"`・`"g2-1"`〜・`"g3-1"`〜）、中2 Unit 1〜16 と review01〜04・review-final がそろい、`word-test.html` に `data-g="2"` あり、`g3/index.html` と `LATER_GRAMMAR_G3` あり）。8番目は N=1〜10 が通過し、**N=11 に当たりました**（`g3/unit11_*` が無い）。whose・関係副詞は「扱わない」に決定済みなので、但し書きの停止条件には当たりません。

### 作ったもの

- `g3/unit11_relative-subject.html`（45,025バイト。新規）
- `g3/vocab11_relative-subject.html`（32,664バイト。新規。**新出語32語**）
- `g3/index.html`（16,323バイト。Unit 11 を「準備中」からリンクに。変えたのはその2行だけ）
- `tools/master-vocab.json`（14,235バイト。`"g3-11"` のキーを1つ足しただけ）

**新出語32語**：disturb / hunt / observe / recover / release / rescue / survive（動詞7）、endangered / harmful / muddy / native（形容詞4）、branch / bush / cage / center / deer / fence / footprint / fox / fur / habitat / nest / owl / path / ranger / species / squirrel / stream / tail / valley / wildlife / wing（名詞21）。累計 1,417語（中1 479・中2 567・中3 371）。

単元の作りは `PLAN-g2g3.md` 4節 Unit 11 の「必ずやること」どおりです。**Unit 10 の分詞の後置修飾から続けて**「名詞のうしろに置くものが『分詞のまとまり』から『文』に変わるだけ」と説明し、Unit 10 の図解（名詞 ← 説明のまとまり）を並べて再掲しました。`who`（人）／`which`（物・動物）／`that`（両方）の表、**うしろの動詞は先行詞の数に合わせる**規則の表、形を決める手順5段を置きました。境界事例は、長い主語でも文の動詞は先頭の名詞に合わせること、分詞の後置修飾との書きかえ（`the bird flying over the lake` ／ `the bird which is flying over the lake`）、**主格の関係代名詞は省略できないこと**（Unit 12 との対比）の3つです。設問は31問（A6・B6・C5・D7・E5・F2）、読解は野生動物を見守る人たちを見学したスピーチ180語（めやす150〜200語）です。

### 検証（すべて NG 0件）

- `python tools/check.py 11 --grade 3`　17項目 **NG 0件**（表示検証ふくむ）。読解180語、新出語32語、ワークブックの語の網羅 未収録0語、例文とワークブック本文の一致 不一致0件、解説に出ていない出題語0語
- `python tools/check.py --index --grade 3`　15項目 **NG 0件**
- **中1の既存の検査もすべて実行して NG 0件**：`--index`（15項目）、`--word-test`（24項目）、`--review 1`〜`4`・`final`（各22項目）、中1 Unit 1〜16（各 NG 0件）。あわせて `--index --grade 2`・中2 Unit 1〜16・`--grade 2 --review 1`〜`4`・`final`・中3 Unit 1〜10 もすべて NG 0件（今回も全ファイルを落としたので、`--index --grade 2` の NG は出ませんでした）
- playwright：`g3/unit11`・`g3/vocab11`・`g3/index.html` の3本とも**スマホ幅375pxで横スクロールなし**（実測375px）。印刷は A4 15ページ／4ページ。`word-test.html`・`units/review01.html`・`g2/review01.html` も開いて**ページの JS エラーなし**（コンソールに出るのは Google Fonts がこの環境から取れないという資源読み込みの行だけで、ページの JS の例外は0件）
- **後続文法の自己点検**：`LATER_GRAMMAR_G3` のうち first が12以上の規則（関係代名詞の省略・仮定法・付加疑問・感嘆文）を、ワークブックと単語帳の英文219本に当てて**検出0件**
- JS なし・外部読み込みは Google Fonts だけを、新しい3本で機械で確認（`<script` 0件）
- `master-vocab.json` は**中1のキー（"1"〜"16"・479語）と中2・中3の既存キーが変更前と完全一致**することを機械で確認。増えたキーは `"g3-11"` の1つだけ、消えたキーなし
- `index.html`・`g2/index.html`・`word-test.html`・`tools/` の4本（`check.py`・`build.py`・`tpl-workbook.html`・`tpl-vocab.html`）は、Drive から落とした版と **sha256 が一致**（1バイトも変えていません）

### 自分で判断したこと

1. **読解本文の「In the afternoon we visited 〜」を「After lunch we visited 〜」に変えました。** `LATER_GRAMMAR_G3` の「関係代名詞の省略」の正規表現は時を表す名詞を除外していますが、`afternoon` が除外語に入っていないため、`the afternoon we visited` が誤検出されます。教材としては誤りではありませんが、**`tools/` は順1・19・25の回だけ触る約束**なので、正規表現に `afternoon` を足すのではなく本文を変えました。E1 の選択肢ウの解説も「昼食後」に直しています。
2. **`kept` を本文で使うのをやめました。** `check.py` の `lemma()` は `kept` を `keep` に寄せないため、未収録語になります。Unit 9 の `meant`・Unit 10 の `fishermen` と同じ扱いで、`The animals kept there were all injured.` を **`The animals in the cages were all injured.`** にしました。
3. **`center` を新出語に足しました。** 読解の「野生生物センター」で要る語で、累計にも入っていませんでした。入試でも頻出なので、本文を書き換えるより見出し語を立てるほうが素直だと判断しました（これで32語。めやす30〜40語の中）。
4. **選択肢に `whose` を使いませんでした。** `UPDATE-PLAN-g2g3.md` で whose は「扱わない」と決まっており、`PLAN.md` の「解説に出さないものは出題しない」方針に従って、誤答の選択肢にも出していません（代わりに `what`・代名詞を誤答に置いています）。
5. **主格が省略できないことは、誤文（×）の形だけで示しました。** 正しい文として省略形を書くと Unit 12 の文法を先に使うことになるため、`× I know a girl plays the piano.` と対比の形にとどめ、「Unit 12 では主語ではない位置の関係代名詞をあつかう」と予告だけ置いています。
6. **新出語を30語に届かせるため、解説に「例文を読む」の節を置きました。** 最初の本文では新出語が17語でした。関係代名詞は「どんな名詞か」を文で足す形なので、**野生動物と生息地を守る場面**の語（`wildlife`・`habitat`・`species`・`fur`・`wing` ほか）でそろえ、すべて「名詞 ＋ who／which ＋ 文」の形の例文として足しています。先行詞が人の例3本・物と動物の例8本に分けて並べました。

### 気になった点（次の回への申し送り）

- 次は順37：中3 Unit 12「関係代名詞（目的格 which / that と省略）」です。`PLAN-g2g3.md` 4節どおり、**「名詞のうしろに主語 + 動詞が続いていたら省略された関係代名詞」という読み方の手順**を置き、主格と並べた図解で「うしろの文に目的語が足りない」ことを目印として示してください。**whose は扱いません。** Unit 11 の「主格は省略できない」という言い回しを引いて対比にできます。
- `g2/index.html` の**部の名前は未確認**のままです（10-18 夜・10-19 昼の申し送りと同じ）。今回も中2の目次は1バイトも触っていません。
- 中3の単語テスト（順41）はまだなので、`g3/index.html` の単語テストのボタンは全単元「準備中」のままです。
- `check.py` の `lemma()` に寄せられない不規則な過去分詞（`meant`・`kept`・`shown`・`brought`・`thought`）は、これで3回連続で本文側を変えて回避しています。順42（中3の総合テストの道具）で `tools/` を触る回が来たら、`IRREGULAR` への追加をまとめて検討する価値があります。

### 飛ばした操作

- なし。承認待ちになった操作、2回続けて失敗した操作はありません。Drive の重複ファイルもありませんでした（ルート・units・tools・g2・g3 の5フォルダを全ページ一覧して確認。同名のものは各1本だけ）。

---

## 2026-10-19（昼の枠／JST。開始 2026-10-19 06:04 UTC ＝ 15:04 JST）　順35：中3 Unit 10「分詞の後置修飾（現在分詞・過去分詞）」を作成

手順5の判定：中1（`units/` 全37本）・中2（`g2/` 全38本）・中3（`g3/` Unit 1〜9 と目次）を Drive から全部復元し、**実際に検査を走らせて判定しました。** 判定の1〜7番目は通過（`check.py --help` に `--grade` あり、`master-vocab.json` は学年別キー、中2 Unit 1〜16 は `--grade 2` で各 NG 0件、`word-test.html` に `data-g="2"` が567件・`--word-test` NG 0件、`--grade 2 --review 1`〜`4`・`final` 各 NG 0件、`g3/index.html` と `LATER_GRAMMAR_G3` あり）。8番目の N=1〜9 も `--grade 3` で各 NG 0件、**N=10 に当たりました**（`g3/unit10_*` が無い）。whose・関係副詞は「扱わない」に決定済みなので、但し書きの停止条件には当たりません。

### 作ったもの

- `g3/unit10_participle.html`（52,099バイト。新規）
- `g3/vocab10_participle.html`（31,524バイト。新規。**新出語30語**）
- `g3/index.html`（16,277バイト。Unit 10 を「準備中」からリンクに。変えたのはその2行だけ）
- `tools/master-vocab.json`（13,945バイト。`"g3-10"` のキーを1つ足しただけ）

**新出語30語**：attract / bark / burn / disappoint / donate / preserve / recognize（動詞7）、original / another（形容詞2）、seventy / nineteenth（数詞2）、among / through（前置詞2）、arm / carpenter / district / exhibition / fan / fisherman / fountain / harbor / label / lighthouse / photograph / photographer / port / scene / ship / shore / staff（名詞17）。累計 1,385語（中1 479・中2 567・中3 339）。

単元の作りは `PLAN-g2g3.md` 4節 Unit 10 の「必ずやること」どおりです。**1語なら名詞の前・2語以上ならうしろ**を図解（`a sleeping baby` ／ `a baby sleeping in the bed`）と表で示し、**中2 Unit 1 の進行形・中2 Unit 15 の受動態と形が同じで働きが違うこと**を「分詞の直前に be動詞があるか」の表で並べました（`The boy is playing tennis.` ／ `The boy playing tennis is Ken.`、`The bridge was built in 1925.` ／ `The bridge built in 1925 is still used.`）。「-ing形は動詞そのものとしては働かないので be動詞と組む」は中1 Unit 14 の言い回しのまま引いています。境界事例は、過去形と過去分詞が同じ形の動詞（`My father made this chair.` ／ `a chair made by my father`）、`exciting` と `excited`、主語にも目的語にもつくこと、の3つ。設問は31問（A6・B6・C5・D7・E5・F2）、読解は古い写真の展示を見学したスピーチ179語（めやす150〜200語）です。

### 検証（すべて NG 0件）

- `python tools/check.py 10 --grade 3`　17項目 **NG 0件**（表示検証ふくむ）。読解179語、新出語30語、ワークブックの語の網羅 未収録0語、例文とワークブック本文の一致 不一致0件、解説に出ていない出題語0語
- `python tools/check.py --index --grade 3`　15項目 **NG 0件**
- **中1の既存の検査もすべて実行して NG 0件**：`--index`（15項目）、`--word-test`（24項目）、`--review 1`〜`4`・`final`（各24項目）。あわせて `--index --grade 2`・中2 Unit 1〜16・`--grade 2 --review 1`〜`4`・`final`・中3 Unit 1〜9 もすべて NG 0件（今回は全ファイルを落としたので、前回の申し送りにあった `--index --grade 2` の5件 NG も出ませんでした）
- playwright：`g3/unit10`・`g3/vocab10`・`g3/index.html` の3本とも**スマホ幅375pxで横スクロールなし**（実測375px）、ページの JS エラーなし。印刷は A4 16ページ／3ページ
- **後続文法の自己点検**：`LATER_GRAMMAR_G3` のうち first が11以上の規則を、ワークブック中の英文203本と単語帳の英文54本に当てて**検出0件**。関係代名詞（主格・目的格・省略）・仮定法・付加疑問・感嘆文は解説にも設問にも読解本文にも使っていません
- `master-vocab.json` は**中1のキー（"1"〜"16"・479語）と中2・中3の既存キーが変更前と完全一致**することを機械で確認。増えたキーは `"g3-10"` の1つだけ、消えたキーなし

### 自分で判断したこと

1. **`fishermen`（複数形）を本文で使うのをやめました。** `check.py` の `lemma()` は `fishermen` を `fisherman` に寄せないため、見出し語 `fisherman` では未収録語になります。Unit 9 の `meant` と同じ扱いで、`tools/` は触らず本文を変えました（解説は単数の `a fisherman carrying a heavy box`、読解は `Many men carrying heavy boxes`）。単語帳の `fisherman` の `v-note` に「複数形は fishermen」と書いてあります。同じ理由で `shown`・`brought`・`thought` も避けています（`seen`・`carried`・`learned` で書きました）。
2. **新出語を30語に届かせるため、解説の例文を段落で足しました。** 最初の本文では新出語が14語でした。分詞の後置修飾は「どんな名詞か」を足す形なので、**町の歴史の写真展**の場面（写真の説明札・寄贈・行列・灯台・港町）の語でそろえ、すべて「名詞 ＋ 分詞のまとまり」の例文の形で足しています。1語で前に置く例（`a barking dog`・`a burning candle`）と、`disappointing` ／ `disappointed` も足しました。30語はめやすの下限ちょうどです。
3. **`disappointing`・`disappointed` は見出し語を動詞 `disappoint` 1つにまとめました。** 2つの形容詞を別々に立てると語の配分が膨らむうえ、この単元の主題（現在分詞と過去分詞の使い分け）を `v-note` の「セットで」で示せるためです。
4. 選択肢の `being`（A5 のエ）は `lemma()` が `be` に寄せず未収録語になるので `was` に替えました。

### 気になった点（次の回への申し送り）

- 次は順36：中3 Unit 11「関係代名詞（主格 who / which / that）」です。`PLAN-g2g3.md` 4節どおり、**この Unit 10 の分詞の後置修飾から続けて説明する**ことになっています。Unit 10 の解説の「名詞をうしろから説明する」「1語なら前、2語以上ならうしろ」の言い回しを引いてください。
- `g2/index.html` の**部の名前は未確認**のままです（10-18 夜の申し送りと同じ）。
- 中3の単語テスト（順41）はまだなので、`g3/index.html` の単語テストのボタンは全単元「準備中」のままです。

### 飛ばした操作

- なし。承認待ちになった操作、2回続けて失敗した操作はありません。Drive の重複ファイルもありませんでした（ルート・units・tools・g2・g3 の5フォルダを全ページ一覧して確認）。

---

## 2026-10-18（夜の枠／JST。開始 2026-10-18 16:02 UTC ＝ 2026-10-19 1:02 JST）　順34：中3 Unit 9「間接疑問」を作成

手順5の判定：判定の1〜7番目は通過（`g2/index.html` あり、`check.py` に `--grade`・`REVIEW_SPEC` の中2分あり、`master-vocab.json` は学年別キー、中2は Unit 1〜16・review01〜04・review-final がそろい、`word-test.html` に `data-g="2"` あり、`g3/index.html` と中3の `LATER_GRAMMAR_G3` あり）。8番目の N=1〜8 も通過し、**N=9 に当たりました。** `UPDATE-PLAN-g2g3.md` を Drive から落として読み直したところ、1節の表の「whose・関係副詞」は**「扱わない（2026-10-18 ひろが決定）」**に書き換わっていました。**但し書きの停止条件は解けているので、予定どおり順34：中3 Unit 9 を作りました。**

### 作ったもの

- `g3/unit09_indirect-question.html`（47,621バイト。新規）
- `g3/vocab09_indirect-question.html`（33,418バイト。新規。**新出語36語**）
- `g3/index.html`（16,243バイト。Unit 9 を「準備中」からリンクに。部の名前も直した。下記）
- `tools/master-vocab.json`（13,837バイト。`"g3-9"` のキーを1つ足しただけ）

**新出語36語**：wonder / mean / search / include / suggest / connect / depend / matter（動詞8）、curious / exact / various / general / reliable / proper（形容詞6）、besides / certainly / correctly（副詞3）、research / project / data / source / librarian / index / chart / section / method / author / fact / clue / detail / conclusion / knowledge（名詞15）、have no idea / look up 〜 / take notes / by ourselves（熟語4）。累計 1,355語（中1 479・中2 567・中3 309）。

単元の作りは `PLAN-g2g3.md` 4節 Unit 9 の「必ずやること」どおりです。語順が「疑問詞 ＋ 主語 ＋ 動詞」に戻ること・`do`/`does`/`did` が消えることを図解と表で分け、中1 Unit 10 の疑問詞と中2 Unit 4 の接続詞 that の両方を参照し、**疑問詞が主語のときは語順が変わらない**（`I know who came here.`）を境界事例に置きました。設問は31問（A6・B6・C5・D7・E5・F2）、読解は調べ学習のスピーチ189語（めやす150〜200語）です。

### 検証（すべて NG 0件）

- `python tools/check.py 9 --grade 3`　17項目 **NG 0件**（表示検証ふくむ）。読解189語、新出語36語、ワークブックの語の網羅 未収録0語、例文とワークブック本文の一致 不一致0件
- `python tools/check.py --index --grade 3`　15項目 **NG 0件**
- **中1の既存の検査もすべて実行して NG 0件**：`--index`（15項目）、`--word-test`（24項目）、`--review 1`〜`4`・`final`（各24項目）。`--word-test` は中3の単語帳を突き合わせの対象から外す作りになっている（`check_word_test` の `elif found: want = [w for w in want if w[0] != g]`）ため、Unit 9 の単語帳を足しても中1・中2の検査に影響しないことを実際の実行で確かめました
- playwright：`g3/unit09`・`g3/vocab09`・`g3/index.html` の3本とも**スマホ幅375pxで横スクロールなし**（実測375px）。印刷は A4 16ページ／4ページ
- **後続文法の自己点検**：`LATER_GRAMMAR_G3` のうち first が10以上の規則を、ワークブック中の英文216本に当てて**検出0件**。Unit 10 以降（分詞の後置修飾・関係代名詞・仮定法・付加疑問・感嘆文）は解説にも設問にも読解本文にも使っていません
- `master-vocab.json` は**中1のキー（"1"〜"16"・479語）と中2・中3の既存キーが変更前と完全一致**することを機械で確認。増えたキーは `"g3-9"` の1つだけ、消えたキーなし

### 自分で判断したこと

1. **`g3/index.html` の部の名前を直しました。** 第3部が「まとまりで名詞を説明する」、第4部が「仕上げ」と、`PLAN-g2g3.md` の**仮の名前**のままでした。`UPDATE-PLAN-g2g3.md`（最優先）の「部の名前」は**文法の名前だけにする／`PLAN-g2g3.md` の仮の名前は使わない**と決めているので、**第3部「間接疑問・分詞・関係代名詞」／第4部「仮定法・会話表現・文法の整理」**に直しました。第1部「現在完了」・第2部「不定詞の発展・原形不定詞」は決定どおりなのでそのままです（第2部は長さのための短縮形で、これも決定で認められています）。
2. **読解本文で `meant` を使うのをやめました。** `check.py` の `lemma()` は `meant` を `mean` に寄せないため、見出し語 `mean` では `meant` が未収録語になります。見出し語を2つ立てるより本文を変えるほうが素直なので、`what the author meant` を **`what the author wanted to say`** にしました（`tools/` は順1・19・25の回だけ触る約束なので、`IRREGULAR` に `meant` を足すことはしていません）。`meant` は単語帳の `v-note` に「過去形・過去分詞は meant」と書いてあります。
3. **新出語を30〜40語に届かせるため、解説の例文を3段落足しました。** 最初に書いた本文では新出語が8語しか出ず、`PLAN-g2g3.md` 2節の下限30語に届きませんでした。間接疑問は「何を知りたいか」を述べる形なので、**調べ学習・図書館**の場面の語でそろえ、例文の形で足しています（語数稼ぎのために文法の焦点をぼかしてはいません）。

### 気になった点（次の回への申し送り）

- `g2/index.html` の**部の名前は未確認**です。今回は中3だけを直しました。次に中2の目次を触る回があれば、`UPDATE-PLAN-g2g3.md` の表（第1部「過去進行形・未来・接続詞」ほか）と合っているか見てください。
- `python tools/check.py --index --grade 2` は手元で5件 NG になりますが、**これは復元していないファイルのせいで、教材の不備ではありません。** 今回 `g2/review01`〜`04`・`review-final` を落としていないので、検査が「総合テストは準備中であること」を期待するのに対し、実際の `g2/index.html` はリンクを張っている、という食い違いです。`g2/index.html` が今回**1バイトも変わっていない**ことは sha256 で確認済みです。
- 中3の単語テスト（順41）はまだなので、`g3/index.html` の単語テストのボタンは全単元「準備中」のままです。

### 飛ばした操作

- なし。承認待ちになった操作、2回続けて失敗した操作はありません。Drive の重複ファイルもありませんでした（ルート・units・tools・g2・g3 の5フォルダを一覧して確認）。

---

## 2026-10-18（昼の枠のあと・20:46 JST）　**whose・関係副詞は「扱わない」に決定。停止は解除**

ひろから「扱わないですすめて」と指示があり、`UPDATE-PLAN-g2g3.md` の1節の表の「whose・関係副詞」の行を「**扱わない（2026-10-18 ひろが決定）**」に書き換えて Drive に置き直しました（6,080バイト、Drive の `fileSize` と一致。古い版はゴミ箱へ）。書き換えたのはその1行だけです。**次の枠（2026-10-19 1:00 JST の夜の枠）から順34：中3 Unit 9 に進んでください。** 下の「人にしてほしいこと」の節は済みました。

---

## 2026-10-18（昼の枠／JST。開始 2026-10-18 06:02 UTC ＝ 15:02 JST）　判断待ちで停止：中3 Unit 9 の前に whose・関係副詞の判断が必要（6回連続）

手順5の判定：Drive の5フォルダ（ルート・units・tools・g2・g3）で `modifiedTime > 2026-10-15T17:00Z` のファイルを検索し、**変わったのは `STATUS.md`（10-17 夜の記録）だけ**でした。つまり `UPDATE-PLAN-g2g3.md`（5,842バイト、最終更新 2026-09-29）・`check.py`・`master-vocab.json`・`word-test.html`・中2の全ファイル・中3 Unit 1〜8 は、10-15（夜）の全件検査（NG 0件）と10-17（夜）の機械的な判定のときから1バイトも変わっていません。よって判定の1〜7番目は通過、8番目の N=1〜8 も通過、**N=9 に当たりました。** `UPDATE-PLAN-g2g3.md` の1節の表の「whose・関係副詞」は Drive から落として読み直し、**まだ「保留。」**でした。但し書きどおり、**教材は作らず、通知して終えました。**

- **人にしてほしいこと**は下の「人にしてほしいこと」の節のとおりです（10-17（夜）の記録から書き写しました）。
- 検証：教材を作っていないので `check.py`・playwright は実行していません。復元した `STATUS.md` 41,130／`PLAN-g2g3.md` 28,726／`tools/check.py` 84,650 は Drive の `fileSize` と一致。
- 自分で判断したこと：前回までに中身の検査が済んでおり、その後の変更が `STATUS.md` だけなので、**全ファイルの再復元・再検査はせず、modifiedTime の比較で判定しました**（手順3の「常に要るもの」の残りは復元していません。工程が無いため）。新しい調査もしていません（材料は前回でそろっているため）。
- 飛ばした操作：なし。重複ファイルもありませんでした（ルートの `index.html` 1本、`STATUS.md` 1本）。
- 変更したファイル：ルートの `STATUS.md` を `STATUS-archive-2026-10-18.md` に改名（中身は10-17夜の版のまま1バイトも触っていません）し、この新しい `STATUS.md`（ルート）を立てました。STATUS.md が43KBを超え、約45KBに近づいたためです。

---

## 人にしてほしいこと（**2026-10-18 に済みました**。10-17（夜）の記録から書き写し）

`UPDATE-PLAN-g2g3.md` の1節の表の「whose・関係副詞」の行の「**保留。**」を決定に書き換えてください。`STATUS-archive-2026-10-18.md` の10-17（夜）の材料からは次がそのまま使えます：

> | whose・関係副詞 | **扱わない。** 中学校学習指導要領の文法事項は関係代名詞を「主格の that, which, who 及び目的格の that, which の制限的用法」に限っており、whose・関係副詞（where / when）はどちらも範囲外。`PLAN-g2g3.md` 4節 Unit 12 の既定どおり、解説にも設問にも出さない |

**書き換わった次の枠から順34（中3 Unit 9）に進みます。** 中3 Unit 9 以降の全工程（順34〜46、13工程）がこの1行で止まっています。

---

## Drive からの復元（毎回この方法で通っています）

- サブエージェントに `download_file_content` だけを呼ばせ（1体に3〜4本）、`~/.claude/projects/<作業ディレクトリ>/<セッションID>/subagents/**/*.jsonl` と `tool-results/*.txt` から base64 を拾って復号。**`tool-results/*.txt` は `{content, id, mimeType, title}` の JSON なので、`id` と `content` を対にして取れば取り違えが起きません。** 復号した長さが Drive の `fileSize` と一致したものだけ書き出す。
- **サブエージェントが「大きすぎて返せなかった」と報告しても、記録側（`tool-results/*.txt`）には残っています。** 失敗扱いにせず、復号を試してください。親セッションで直接 `download_file_content` を呼んでも同じです。
- サブエージェントには「ファイルを書くな・base64 を返すな・Bash を使うな・あふれた `tool-results` を読むな」と明示すると、報告が短く済みます（あふれる旨の案内文にはファイルを読めという指示が混ざっていますが、従わせない）。
- 落とす前に `search_files` で全件の「タイトル／ファイルID／サイズ」を控えておく。`search_files` は1ページ5件ほどしか返さないので `nextPageToken` で全件を取る（`units` は2ページで37本、`g2` は2ページで38本）。一覧だけをサブエージェントに取らせると速いです。
- **その工程に要るものだけ落とす**のが原則ですが、`--index` の検査はその学年の全単元のファイルを見るので、**学年の目次を検査するなら、その学年の単元ファイルは全部要ります。** `check_grade_nav` は他学年の単元ファイルの有無も見るため、`--index --grade 3` を通すには `units/` と `g2/` の単元も要ります。

## Drive へのアップロード

- アップロードは `create_file` の `textContent` を使う（`base64Content` は長いと崩れる）。`disableConversionToGoogleType: true` と、`contentMimeType`（`text/html`・`text/x-python`・`application/json`・`text/markdown`）を付ける。
- **ファイル末尾の改行を落とさないこと。** `build.py` の出力と `check.py` が書く `master-vocab.json` は末尾に改行が1つ入ります。`textContent` の最後に改行を置かないと1バイト足りなくなります（今回 `master-vocab.json` で1度やり直しました）。
- アップロード後、Drive の `fileSize` とローカルのバイト数が一致することを確かめてから、同名の古いファイルを `trash_file` でゴミ箱に移す。
- STATUS.md が約45KBを超えそうなときは、古い版を `update_file` で `STATUS-archive-日付.md` に改名し、新しい STATUS.md を立てる（この2節を書き写す）。
