# 制作の記録

> **2026-10-15（夜）にこのファイルを分割しました。** 新しい記録は上に足しています（最新は 2026-10-15（昼）の順32：中3 Unit 7、その前が 2026-10-15（夜）の順31：中3 Unit 6）。2026-10-14（昼）の順30：中3 Unit 5、10-14（夜）の順29：中3 Unit 4、10-13（昼）の順28：中3 Unit 3 の記録は `STATUS-archive-2026-10-14.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-13.md`、`STATUS-archive-2026-10-11.md`、`STATUS-archive-2026-10-10.md`、`STATUS-archive-2026-10-08.md`、`STATUS-archive-2026-10-07.md`、`STATUS-archive-2026-10-06.md`、`STATUS-archive-2026-10-05.md`、`STATUS-archive-2026-10-03.md`、`STATUS-archive-2026-10-02.md`、`STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で `STATUS-archive-2026-10-14.md` に改名し、この新しい `STATUS.md` を置いています。** アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブとこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-15（昼の枠／JST。開始 2026-10-15 06:08 UTC ＝ 15:08 JST）　順32：中3 Unit 7「want / tell / ask + 人 + to 〜」

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"`／`"g3-N"` のキーで積む作り）。2番目は `g2/` に Unit 1〜16 の2本ずつがそろい、復元した Unit 1・8・16 は `--grade 2` で NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `GRADE_REVIEW_SPEC[2]` あり。5・6番目は `g2/review01`〜`04`・`review-final` が NG 0件。7番目は `g3/index.html` あり・`LATER_GRAMMAR_G3` あり。8番目で N=1〜6 は2本ずつそろって NG 0件、**N=7 で `g3/unit07_*.html` が無い**ので、**順32＝中3 Unit 7** です。N=9 ではないので whose・関係副詞の判断は要りませんでした。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g3/unit07_ask-to.html` | **新規**（50,549バイト）ワークブック。31問（A6・B6・C5・D7・E5・F2） | **g3** |
| `g3/vocab07_ask-to.html` | **新規**（34,916バイト）単語帳。見出し語34語 | **g3** |
| `g3/index.html` | 変更（16,093 → 16,119バイト）Unit 7 のワークブック・単語帳をリンクに（単語テストは順41まで準備中） | g3 |
| `tools/master-vocab.json` | 変更（12,566 → 12,925バイト）`"g3-7"` に34語を追加。中1・中2・`"g3-1"`〜`"g3-6"` のキーは1語も変えていない（復元直後の版と機械で突き合わせ、差分は `g3-7` の追加だけ） | tools |
| `STATUS.md` | 変更（この記録を追記） | ルート |

ほかの復元ファイル（計画書類4本・`index.html`・`word-test.html`・`tools/` の5本・`units/` の37本・`g2/` の38本・`g3/` の12本）は**1バイトも変えていません**（復元直後の md5 と突き合わせ）。**`check.py`・`build.py`・テンプレート2本は今回触っていません。**

### 中身

- **新出語34語**（めやす30〜40語）。人 ＋ to をとる動詞 `encourage`・`remind`・`allow`・`expect`、そのほかの動詞 `quit`・`stretch`・`shoot`・`beat`・`blame`・`gather`・`apologize`・`forgive`・`reply`、形容詞・副詞 `upset`・`injured`・`final`・`seriously`、名詞 `basketball`・`tournament`・`round`・`opponent`・`referee`・`whistle`・`court`・`half`・`point`・`knee`・`role`・`responsibility`・`decision`、熟語 `pay attention to 〜`・`for a while`・`in the end`・`cheer up 〜`。累計は中1 479語＋中2 567語＋中3 239語＝**1,285語**。
- **読解本文は全校集会のスピーチ「キャプテンとして学んだこと」162語**（めやす130〜180語。表示は「およそ160語」）。バスケットボール部のキャプテンが、負けた試合のあとチームメートを責め、コーチに `told me to listen to my teammates` と言われ、`asked Taku not to quit`・`asked him to forgive me`・`reminded everyone to stretch`・`asked the players on the bench to cheer for the team` と変わっていく話です。下線部①は `I asked the players on the bench to cheer for the team` です。
- 解説：`I want to join the team.` → `I want you to join the team.` の書き換え（`transform`）→ 用語枠「動詞 ＋ 人 ＋ to 〜」→ **`want to` と `want ＋ 人 ＋ to` で動作をする人が変わる図解を上下に並べた**（PLAN-g2g3.md 4節の最大のつまずき）→ なぜ人を入れると動作主が変わるか → 人は目的格（中1 Unit 8）の表と `would like ＋ 人 ＋ to` → **want／tell（指示）／ask（依頼）の表**と使い分けの説明 → **`not to` の位置**の図解（`did not tell` との意味の違いも）→ **中2 Unit 8 の SVOO との違いの表**（`told him the story`／`told him to come`、`asked me a question`／`asked me to help her`）→ 同じ形をとる動詞（encourage・remind・allow・expect）の表 → **`said to 人, "〜."` からの書き換え表**（命令文は tell、Please は ask、Don't は not to）→ 手順5段 → 境界（say は人 ＋ to をとらない、`Do you want me to 〜?` は申し出で中2 Unit 7 の Shall I とつなぐ、ask の2つの意味、人の位置に名詞句が入る形）→ 入試での出方 → よくある間違い4件 → まとめ。

### 検証結果

- **`check.py 7 --grade 3`：17項目 NG 0件**（語の網羅 未収録0語・例文の一致 不一致0件・375px で横スクロールなし・A4 ワークブック16ページ／単語帳4ページ）。
- **`LATER_GRAMMAR_G3` で first が8以上の形を、ワークブックの全文（設問・解答・読解を含む）に機械でかけて0件**。`make／let／help + 人 + 原形`、間接疑問、分詞の後置修飾、関係代名詞（主格・省略）、仮定法、付加疑問、感嘆文はいずれも0件です。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 1`・`8`・`16`。**中2もすべて NG 0件**：`--index --grade 2`・`--review 1`〜`4 --grade 2`・`--review final --grade 2`・`check.py 1`・`8`・`16 --grade 2`。**中3**は `--index --grade 3`・`check.py 1`〜`7 --grade 3` が NG 0件（計28通り）。
- **検査の前後で `master-vocab.json` が変わらないことも確かめました**（既存キーを全件比較して同一）。
- **playwright（Chromium・375px、Google Fonts は空の CSS に差し替え、`details` をすべて展開）**：`g3/unit07`・`g3/vocab07`・`g3/unit06`・`g3/index.html`・`g2/index.html`・`index.html`・`units/review01.html`・`units/review-final.html`・`g2/review01.html`・`g2/review-final.html`・`word-test.html`（`?g=1`・`?g=2`・`?unit=5`・`?unit=2-5`・`?part=2-1`）の**15通り**で scrollWidth 375px・JS の例外0件・console エラー0件。
- 新しい2本は `<script>` 0件、外部読み込みは Google Fonts だけ。`div` の開閉数も対応しています（36／36・65／65）。本文は `<nav class="topnav">` から始めて `</ol>` で終えました（前回の申し送りどおり）。

### 自分で判断したこと

1. **題材を「部活動（バスケットボール部）のキャプテン」にしました。** 指示（コーチ・審判 → tell）、依頼（キャプテン → ask）、希望（want）が一つの場面で自然にそろい、試合の語（`tournament`・`opponent`・`referee`・`whistle`・`court`・`half`・`point`）がまとめて未収録だったためです。Unit 5（防災）・Unit 6（文化祭の劇）と重なりません。読解の形式は `PLAN-g2g3.md` 2節の「スピーチ」です。
2. **`encourage`・`remind`・`allow`・`expect` を「同じ形をとる動詞」として表に置きました。** `PLAN-g2g3.md` の単元名は want / tell / ask ですが、入試では同じ形の動詞がまとめて出るため、意味の表と例文1本ずつにとどめ、設問では B10（expect）・B11（allow）・D24（remind）で使いました。
3. **`would like ＋ 人 ＋ to 〜` を扱いました。** `would like to 〜` は中2 Unit 9 の熟語として既出（`would` も既出扱い）なので新出語は増えません。D23 で使っています。
4. **`said to 人, "〜."` からの書き換えを解説と A5 に入れました**（命令文 → tell、Please → ask、Don't → not to）。直接話法は中1から使っている形なので、後の文法を先取りしていません。
5. **`Do you want me to 〜?` は申し出として境界事例に置き、中2 Unit 7 の `Shall I 〜?` とつなぎました**（A6・B12）。
6. **`shoot` の過去形 `shot`、`forgive` の過去形 `forgave`、`blow` の過去形 `blew` は本文で使っていません。** どれも `IRREGULAR` に無いため未収録語になります。`check.py` を触らずに済ませるため、「タクは許してくれた」は `I asked him to forgive me` と依頼の形で書き、笛は `wait for the whistle` で使いました。`shot` は単語帳の注記（`v-note`）にだけ書いています（注記は網羅の検査の対象外）。
7. **`ankle` は候補に入れましたが外しました**（`knee` だけで足り、34語に収めるため）。`basketball` は未収録だったので見出し語に立てました。
8. **関係代名詞の省略の検査（`the 名詞 + 主語 + 動詞`）に当たらないよう、`After the game, I blamed …` のように副詞句のあとは必ずコンマを打ちました。** `the points we lost` のような形も避けています。
9. **単元名は `g3/index.html` の表記（「want / tell / ask + 人 + to 〜」。＋ は半角）に合わせました**（前回の判断6と同じく目次を正とする）。
10. **`g3/index.html` の Unit 7 の `<li>` には `class="ready"` を付けていません。** Unit 1〜3 には付いていて Unit 4〜6 には付いていない不揃いがありますが、直前の Unit 4〜6 に合わせました（`--index --grade 3` は NG 0件）。

### 気になった点（次の回への申し送り）

- **次は順33＝中3 Unit 8（`make / let / help + 人 + 原形`。スラッグ `make-let-help`）です。** 要るもの：このワークブックと単語帳（`g3/unit07_ask-to.html`・`g3/vocab07_ask-to.html`。書きぶりの見本）、`tools/tpl-workbook.html`・`tools/tpl-vocab.html`。新出語は累計との差分で、`"g3-8"` のキーに積みます。Unit 8 は**to が付かない形であることを Unit 7 と並べて図解で分ける**こと、**中2 Unit 8 の SVOC の make（〜にする）とこの make（〜させる）を並べて区別する**こと、help は `help 人 原形` と `help 人 to 原形` の両方、see / hear ＋ 人 ＋ 原形は1〜2例です（`PLAN-g2g3.md` 4節）。`LATER_GRAMMAR_G3` の `first=8` が解禁になります。
- **`whose`・関係副詞は `UPDATE-PLAN-g2g3.md` で「保留」のままです。** 判断が要るのは中3 Unit 9（順34）の前、つまり**あと1工程先（次の次の回）**です。最優先の `UPDATE-PLAN-g2g3.md` は保留なので、順34の回は手順5の 8 の但し書きどおり**作らずに通知して終える**ことになります。**和歌山の過去問での出題の有無を人が確かめて `UPDATE-PLAN-g2g3.md` に書いておくと止まりません。**
- **今回あらたに未収録だと分かった語**：`shot`（shoot の過去形）・`forgave`・`blew` は `IRREGULAR` に無い不規則変化です。`ankle`・`side`・`luck`・`pain`・`ahead`・`loss`・`volleyball`・`politely`・`request`・`suggest`・`persuade` も未収録です。前の回からの申し送り（`couldn't` が `CONTRACTIONS` に無い、`hang`・`either`・`meaning`・`ourselves`・`everybody` などが未収録、`-ly` の副詞は `lemma` が元の形容詞に寄せない、曜日名・月名・`worker`・`through` など、`g2/vocab12_gerund.html` と `g3/vocab06_too-enough.html` に既出語の熟語の重複〔`take part in 〜`・`pick up 〜`〕、使われていない `tools/gen-word-test.tpl.html`）は人の判断のままです。
- ［参考］の「解説に出ていない出題語」が10語（`brother`・`calls`・`clean`・`friend`・`lend`・`room`・`spoke`・`taku`・`umbrella`・`writer`）あります。どれも既出語か人名で NG ではありません。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート28本、`units/` 37本、`tools/` 11本、`g2/` 38本、`g3/` 13本〔今回の前〕）。復元は計画書類4本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の5本・`units/` の37本・`g2/` の38本・`g3/` の13本の **100本**で、すべて Drive の `fileSize` とバイト数が一致しました。

---

## 2026-10-15（夜の枠／JST。開始 2026-10-14 16:13 UTC ＝ 2026-10-15 01:13 JST）　順31：中3 Unit 6「too 〜 to … と 〜 enough to … / so 〜 that …」

手順5の判定：1番目は通過（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"`／`"g3-N"` のキーで積む作り）。2番目は `g2/` に Unit 1〜16 の2本ずつがそろい、復元した Unit 1・8・16 は `--grade 2` で NG 0件。3番目は `word-test.html` に `data-g="2"` があり `--word-test` が NG 0件。4番目は `GRADE_REVIEW_SPEC[2]` あり。5・6番目は `g2/review01`〜`04`・`review-final` が NG 0件。7番目は `g3/index.html` あり・`LATER_GRAMMAR_G3` あり。8番目で N=1〜5 は2本ずつそろって NG 0件、**N=6 で `g3/unit06_*.html` が無い**ので、**順31＝中3 Unit 6** です。N=9 ではないので whose・関係副詞の判断は要りませんでした。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g3/unit06_too-enough.html` | **新規**（52,038バイト）ワークブック。31問（A6・B6・C5・D7・E5・F2） | **g3** |
| `g3/vocab06_too-enough.html` | **新規**（36,626バイト）単語帳。見出し語34語 | **g3** |
| `g3/index.html` | 変更（16,059 → 16,093バイト）Unit 6 のワークブック・単語帳をリンクに（単語テストは順41まで準備中） | g3 |
| `tools/master-vocab.json` | 変更（12,244 → 12,566バイト）`"g3-6"` に34語を追加。中1・中2・`"g3-1"`〜`"g3-5"` のキーは1語も変えていない（復元直後の版と機械で突き合わせ、差分は `g3-6` の追加だけ） | tools |
| `STATUS.md` | **新規**（古い版は `STATUS-archive-2026-10-14.md` に改名） | ルート |

ほかの復元ファイル（計画書類4本・`index.html`・`word-test.html`・`tools/` の5本・`units/` の37本・`g2/` の38本・`g3/` の11本）は**1バイトも変えていません**（復元直後の md5・バイト数と突き合わせ）。**`check.py`・`build.py`・テンプレート2本は今回触っていません。**

### 中身

- **新出語34語**（めやす30〜40語）。動詞 `lift`・`arrange`・`act`・`rehearse`・`clap`・`cheer`・`whisper`・`cooperate`、助動詞 `could`、形容詞・副詞 `enough`・`alone`・`silent`・`tight`・`neat`・`upstairs`、名詞 `ladder`・`hammer`・`nail`・`board`・`cardboard`・`rope`・`tape`・`rehearsal`・`applause`・`success`・`drama`・`flute`・`microphone`・`row`・`theme`・`partner`、熟語 `pick up 〜`・`in time`・`one by one`。累計は中1 479語＋中2 567語＋中3 205語＝**1,251語**。
- **読解本文は学校新聞の記事「幕が上がるまで」174語**（めやす130〜180語。表示は「およそ175語」）。文化祭の劇の準備で、段ボールの板が重すぎて一人で持ち上げられなかったこと、ロープが十分に長くなかったこと、体育館が騒がしくて声がとどかなかったことを置き、`too heavy to lift alone`・`not long enough`・`so noisy that 〜 could not hear us`・`so loud that some of us cried` を本文に出しました。下線部①は `The applause at the end was so loud that some of us cried` です。
- 解説：`The box is very heavy. I cannot carry it.` → `The box is too heavy to carry.` の書き換え（`transform`）→ 用語枠「too 〜 to …」→ **too は「必要以上に」なのでうしろの動作が成り立たない**図解 → なぜ否定語が無いのに否定の意味になるか → **to のうしろに目的語を書かない**図解（`to carry it` としない）→ `for` ＋ 人（Unit 5 と中1 Unit 8 の目的格につなぐ）→ 用語枠「〜 enough to …」と **enough は形容詞・副詞のうしろ**の図解 → **enough が名詞につくときは前**（`enough time`）の表 → `so` 〜 `that` ＋ 主語 ＋ 動詞の図解（中2 Unit 4 の接続詞 that につなぐ）→ **too 〜 to ↔ so 〜 that ＋ cannot の書き換え表**（書き換えると主語と目的語を書き足すことを明示）→ 手順5段 → 境界（名詞につく `too many`／`too much`、`not 〜 enough to`、`that` の省略、単独の副詞 `enough`）→ 入試での出方 → よくある間違い4件 → まとめ。

### 検証結果

- **`check.py 6 --grade 3`：17項目 NG 0件**（語の網羅 未収録0語・例文の一致 不一致0件・375px で横スクロールなし・A4 ワークブック16ページ／単語帳4ページ）。
- **`LATER_GRAMMAR_G3` で first が7以上の形を、ワークブックの全文（設問・解答・読解を含む）に機械でかけて0件**。`want／tell／ask + 人 + to`、`make／let／help + 人 + 原形`、間接疑問、分詞の後置修飾、関係代名詞（主格・省略）、仮定法、付加疑問、感嘆文はいずれも0件です。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 1`・`8`・`16`。**中2もすべて NG 0件**：`--index --grade 2`・`--review 1`〜`4 --grade 2`・`--review final --grade 2`・`check.py 1`・`8`・`16 --grade 2`。**中3**は `--index --grade 3`・`check.py 1`〜`6 --grade 3` が NG 0件（計27通り）。
- **検査の前後で `master-vocab.json` が変わらないことも確かめました**（中1・中2・中3の既存キーを全件比較して同一）。
- **playwright（Chromium・375px、Google Fonts は空の CSS に差し替え、`details` をすべて展開）**：`g3/unit06`・`g3/vocab06`・`g3/unit05`・`g3/index.html`・`g2/index.html`・`index.html`・`units/review01.html`・`units/review-final.html`・`g2/review01.html`・`g2/review-final.html`・`word-test.html`（`?g=1`・`?g=2`・`?unit=5`・`?unit=2-5`・`?part=2-1`）の**15通り**で scrollWidth 375px・JS の例外0件・console エラー0件。
- 新しい2本は `<script>` 0件、外部読み込みは Google Fonts だけ。`div` の開閉数も対応しています（下の5）。

### 自分で判断したこと

1. **題材を「文化祭の劇の準備」にしました。** `too 〜 to …` の典型（重すぎて持ち上げられない）と `〜 enough to …`（とどくほど背が高い）が自然に何度も出る題材で、道具の語（`ladder`・`hammer`・`nail`・`board`・`cardboard`・`rope`・`tape`）がまとめて未収録だったためです。防災（Unit 5）と重なりません。読解の形式は `PLAN-g2g3.md` 2節の「記事」です。
2. **`could` を見出し語に立てました。** `so 〜 that … could not` は入試で出る形ですが、`could` は `master-vocab.json` にも `BASIC` にも無く、`check.py` の `IRREGULAR` も `could` → `can` に寄せません。**`check.py` を触らずに済ませるため、`could` を助動詞のエントリとして立て**、注に「`can` の過去形・うしろは原形・否定は `could not`」と書きました。前の回からの申し送り（`could` が未収録）はこれで解消です。
3. **`couldn't` は使っていません。** `CONTRACTIONS` に `couldn't` が無いため未収録語になります。本文・設問・解答はすべて `could not` と書きました。**`couldn't` を `CONTRACTIONS` に足すかは人の判断に残します。**
4. **並べ替え（B8）の主語を `Ken` から `he` に変えました。** 並べ替えの語群は「文の最初に来る語も小文字」の約束なので `ken` と書くことになり、`check.py` の固有名詞の除外（`\b[A-Z][a-z]+\b` で拾う）に当たらず未収録語になります。**中2・中3の並べ替えでは人名を使わない**のが安全です。設問と解答の両方を `He is tall enough to reach the top of the wall.` に直しました。
5. **本文に `<div class="sheet">` を書かないこと**（今回いちど誤って入れ、組み立て後に直しました）。`tpl-workbook.html` も `tpl-vocab.html` も、テンプレート側が `<div class="sheet">` を開いて `{{BODY}}` のうしろで閉じます。**本文は `<nav class="topnav">` から始め、`</ol>` で終える**のが正しい形です（中3 Unit 5 の2本と同じ）。最初は見本の完成版 HTML をそのまま写してしまい `div` が二重になっていたので、`check.py` が NG を出さない（検査項目に div の対応が無い）ことを承知の上で、`div` の開閉数を機械で数えて直しました。直した2本は開39／閉39・開66／閉66 で、中3 Unit 5 の2本（35／35・63／63）と同じく対応しています。
6. **単元名は `g3/index.html` の表記（「too 〜 to … と 〜 enough to … / so 〜 that …」）に合わせました。** `PLAN-g2g3.md` の単元表は「too 〜 to … / 〜 enough to … / so 〜 that …」ですが、目次の単元名は `build.py` の `unit_table` が読んで総合テストの結果画面にも出るので、**目次を正として** `<title>`・`h1` をそちらに揃えました（目次は触っていません）。
7. **`It is kind of you to 〜` のような `of` ＋ 人は扱っていません**（Unit 5 で境界事例として置いた範囲のまま）。`enough` の境界事例は `too many`／`too much`、`not 〜 enough to`、`that` の省略、単独の副詞 `enough` の4つに絞りました。
8. **`hang`・`either`・`meaning`・`ourselves`・`everybody`・`glue`・`scissors`・`stick`・`able`（`be able to 〜`）は未収録なので本文から外しました。** 「ロープで幕をつるす」は `We used a rope for the curtain` と書き、文末は `The drama was a great success.` で結びました。
9. **中3 第2部の名前は前の回のとおり「不定詞の発展・原形不定詞」のままです**（`g3/index.html` の見出しは触っていません）。単語テストのボタンは「準備中」のままです（順41まで）。

### 気になった点（次の回への申し送り）

- **次は順32＝中3 Unit 7（`want / tell / ask + 人 + to 〜`。スラッグ `ask-to`）です。** 要るもの：このワークブックと単語帳（`g3/unit06_too-enough.html`・`g3/vocab06_too-enough.html`。書きぶりの見本）、`tools/tpl-workbook.html`・`tools/tpl-vocab.html`。新出語は累計との差分で、`"g3-7"` のキーに積みます。Unit 7 は**中2 Unit 8（SVOO）との違いを表で分ける**こと、`I want to go` と `I want you to go` を並べて**動作をする人が変わること**を図解で示すこと（最大のつまずき）、ask＝依頼・tell＝指示の差に触れることです（`PLAN-g2g3.md` 4節）。`LATER_GRAMMAR_G3` の `first=7` が解禁になります。
- **`whose`・関係副詞は `UPDATE-PLAN-g2g3.md` で「保留」のままです。** 判断が要るのは中3 Unit 9（順34）の前、つまり**あと2工程先**です。最優先の `UPDATE-PLAN-g2g3.md` は保留なので、**和歌山の過去問での出題の有無を人が確かめて決める必要があります。** 順32・順33 のうちに決めておくと止まりません。
- **本文に `<div class="sheet">` を書かない**（上の5）。`check.py` は div の対応を見ないので、ここは人の目か `div` の開閉数の数え上げでしか捕まりません。次の回も、見本にするのは**完成版 HTML ではなく、その構造（nav から始めて `</ol>` で終える）**にしてください。
- **並べ替えに人名を使わない**（上の4）は、中1・中2の既存ファイルには影響しません（既存の並べ替えに小文字の人名は無く、`--grade 1`・`--grade 2` の検査は NG 0件のままです）。
- **今回あらたに未収録だと分かった語**：`hang`・`either`・`meaning`・`ourselves`・`everybody`・`glue`・`scissors`・`stick`・`able`・`hardly`・`silently`（`-ly` の副詞は `lemma` が元の形容詞に寄せないため、使うなら見出し語に立てる必要があります）。`couldn't`（`CONTRACTIONS` に無い）も同じです。曜日名・月名・`worker`・`through`・単独の `after`／`next`・`feel`／`felt`・`nothing`、`IRREGULAR` に無い `worse`／`worst`・`kept`・`begun`・`thought`・`hid`、`g2/vocab12_gerund.html` の `take part in 〜` の重複、使われていない `tools/gen-word-test.tpl.html` は前の回からの申し送りのままです（人の判断）。
- ［参考］の「解説に出ていない出題語」が8語（`bring`・`fast`・`home`・`join`・`partner`・`run`・`team`・`than`）あります。どれも既出語で NG ではありません（`partner` は今回の新出語で、読解と単語帳に出ています）。

### 飛ばした操作

- **なし。** 5フォルダを一覧し、**同名ファイルの重複が無いことを確認しました**（ルート28本、`units/` 37本、`tools/` 11本、`g2/` 38本、`g3/` 11本〔今回の2本を含む〕）。復元は計画書類4本・`STATUS.md`・`index.html`・`word-test.html`・`tools/` の5本・`units/` の37本・`g2/` の38本・`g3/` の9本の **90本**で、すべて Drive の `fileSize` とバイト数が一致しました。大きいファイルは `tool-results/*.txt` に残っていたので復号できました（下の節の要点どおり）。

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
