# 制作の記録

> **2026-09-27（昼）にこのファイルを分割しました。** 09-25（昼）〜09-27（夜）の記録（工程2〜5、答え合わせの追加）は `STATUS-archive-2026-09-26.md` にそのまま入っています。それより前は `STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で改名し、この新しい `STATUS.md` を置いています。**アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブとこの新しい `STATUS.md` の両方を置いてください。

---

## 2026-09-28（昼の枠／JST。開始 2026-09-28 06:08 UTC）　工程8：中1の総まとめテスト `units/review-final.html`

手順5の判定は**5番目で止まりました**。1番目（`word-test.html` あり・`--word-test` 11項目 NG 0件）、2番目（`index.html` に `word-test.html?unit=` が16件）、3番目（`tools/tpl-review.html` あり）、4番目（`--review 1`〜`--review 4` いずれも 18項目 NG 0件）を通過し、`units/review-final.html` が無かったので**工程8**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `units/review-final.html` | **新規**（65,480バイト） | units |
| `index.html` | 変更（中1のまとめの「総まとめ　準備中」を `units/review-final.html` への「総まとめテスト」リンクに。16,042→16,064バイト） | ルート |
| `STATUS.md` | 追記（この節を上に足した） | ルート |

`tools/` の道具（`tpl-review.html` `build.py` `check.py`）・`word-test.html`・単元の32本・`master-vocab.json`（4,330バイトのまま）・計画書類・`units/review01`〜`review04` は**変更していません**。本文は `python tools/build.py review final "中1の総まとめ" "Unit 1〜16" body.html` で組み立てました（名前は `build.py` の使い方の例と `index.html` の「中1のまとめ」に合わせました）。

### 中身（31問・100点）

- **大問1 文法 25点**（2点×5＋3点×5）：**10問を10個の Unit に1問ずつ**割り当てました。4択5問（Unit 1 are／Unit 4 women／Unit 5 play／Unit 8 him／Unit 15 Were）・語形変化（Unit 16 buy → bought）・並べかえ2問（Unit 2 Are you and Ken in the same class? ／ Unit 11 What time do you go to bed?）・誤文訂正の直した箇所2問（Unit 7 I am like → like ／ Unit 13 can speaks → speak）。
- **大問2 資料つきの読解 18点**（3点×6）：Minami Summer Festival の予定表（Time／What／Place の4行）と「お祭りのお知らせ」3項目、ミカがオーストラリアのルーシーに書いたメール（128語）。兄がしたことの選択（Unit 16）・表とメールから時刻を1語（one、Unit 11）・下線部 It が指すものの選択（Unit 3）・お知らせの空所に1語（touch、Unit 12）・対話の空所に3語以上（They are dancing.、Unit 14）・内容に合う文を2つ（Unit 5・16）。
- **大問3 対話文の読解 21点**（3・4・4・3・4・3）：リクと留学生トムの対話（144語）。( A ) の選択（Do you like temples, too?、Unit 6）・英問英答（He works on his farm.、Unit 9）・下線部 ① I often ride them with him. を them と him を明らかにして日本語で（Unit 8）・( B ) の選択（How many horses does he have?、Unit 10）・英問英答（No, he can't.、Unit 13）・内容一致（Tom is reading 〜、Unit 14）。
- **大問4 条件英作文 10点**：ALT の Mr. Smith に Minami Park と Minami Museum のどちらかをすすめる。表（開いている時間・料金・できること）を見て「Please visit 〜.」で書き始め、**because を使って25語以上**（Unit 12・13）。
- **大問5 長文の読解 26点**（2×3・3×2・4・4・6）：ソラの祖母についてのスピーチ（145語）。( 1 )〜( 3 ) の選択（lives／was／gave）・英問英答2問（She walks by the sea with her dog. ／ He stayed at his grandmother's house.）・下線部 ① She showed me her favorite place. を She と me を明らかにして日本語で・4文を話の順に並べる・内容に合う文を2つ。

### 検証結果

- `python tools/check.py --review final` … **18項目 NG 0件**（16の Unit すべてが出題に入っている、読解本文 128・144・145語、範囲より後の文法 0件、375px 横スクロールなし、印刷 A4 12ページ）。
- `--review 1`〜`--review 4` も **18項目 NG 0件**、`--word-test` は **11項目 NG 0件**、`--index` は **12項目 NG 0件**（第1〜4部と総まとめのすべてが総合テストへのリンク）。
- 語彙の照合：本文・選択肢・正解・模範解答・表に出る英語を、Unit 1〜16 の単語帳の見出し語（v-note と一覧表を含む）＋基本語77語に照らして機械で走査し、**範囲外 0件**（残りは人名・地名の Aya・Lucy・Mika・Riku・Tom・Sora・Kyoto・Minami・Mr. Sato・Mr. Smith・Emma・Ken と、日本語の文中の「ALT」だけ）。同じ走査を `review04.html` に当てると人名だけが残るので、照合の厳しさは前回と同じです。スクリプトは今回も作業用で、Drive には置いていません。
- playwright（chromium）で **320 / 375 / 414 / 768px**：`review-final.html` と `index.html` は横スクロールなし（結果画面も375px）、`pageerror` 0件。
- 動作：全問に正解（記述は模範解答）を入れ、**再読み込みして途中保存から復元してから採点 → 100点**（25/18/21/10/26）。「先生に送る」で **1080×5233px** の画像。3問に1問わざと間違えると **69点**で、Unit ごとの正答率（Unit 7・9 が0%、Unit 11 が50%、Unit 5 が60%、Unit 16 が68%に「見直し」）が出ました。
- 英問英答の別解（They are dancing with many people. ／ He works on the farm. ／ No, he cannot. ／ She walks with her dog. ／ He stayed at her house.）でも満点。大問4は模範解答の別解（Museum・41語）と**自分で書いた別の正答（Park・31語）でどちらも 10/10**、because なしの11語で **4/10**、`please visits minami park you can plays tennis it free because I am like flowers` で **0/10**。

### 自分で判断したこと

1. **16の Unit を全部埋めるため、大問1の10問を10個の Unit（1・2・4・5・7・8・11・13・15・16）に1問ずつ割り当て、残りの Unit 3・6・9・10・12・14 を読解の設問で受け持たせました。** 大問1で Unit 3・6・9・10・12・14 を外したのは、読解の中で自然に問える形（下線部 It の指すもの、Do you 〜? の選択、does の英問英答、How many 〜? の選択、お知らせの命令文、写真の中の進行形）があるためです。
2. **読解の題材は、計画の「日記・手紙・スピーチ」のうち、第4部で使っていない「手紙」を大問2に入れました（メール）。** 大問3は対話、大問5はスピーチです。第4部（日記・対話・スピーチ）と同じ並びにならないようにしています。
3. **`Dear` が範囲外なので、メールの書き出しは `Hello, Lucy.`、結びは名前だけ**にしました。`wall` も範囲外だったので、スピーチの「写真は部屋の壁に」は `Now it is on my desk.` にしています。`camp` `curry` `event` なども範囲外のため、お祭りの催しは `brass band concert` `Japanese cooking class` `dance with everyone` `movie night` と範囲内の語で書きました。
4. **大問4は「すすめる」題材にして、書き出しを命令文 `Please visit 〜.` にしました。** 第4部の大問4が過去形（先週の日曜日）だったので、総まとめでは命令文（Unit 12）と can（Unit 13）を使う形にしました。比較（better）・不定詞（want to）・未来（will）を使わずに理由が書けるよう、表には「できること」を3つずつ置いています。
5. **`sat` などの範囲外の不規則過去形は使いませんでした**（前回と同じ）。スピーチの「ベンチにすわって朝ごはんを食べた」は `We had breakfast there together.` にしています。
6. **大問3の内容一致の選択肢で「15頭の馬」を「10頭」に変えました。** `has fifteen` が `check.py` の現在完了の検出（`has` ＋ -en で終わる語）に引っかかったためで、誤検出です。`ten` は検出の除外語に入っています。
7. **並べかえ（大問5）の4文目は、本文に「着いた」という語が無いので `Sora went to his grandmother's house last summer.` にしました。** 本文の `I stayed at her house for a week.` に当たる出来事で、ほかの3文（早起き→朝ごはん→写真をもらう）より前です。
8. **判断が要る問題の要点（data-kw）は、review03・04 と同じく動詞の形まで含めました**（`he works` `she walks` `he stayed` `they are dancing`）。大問5の和訳の要点には「ソラ|私|僕|ぼく」のように一人称の書き方の別表記を入れています。

### 気になった点（申し送り）

- **次は工程9（中2・中3の単元構成の設計 `PLAN-g2g3.md`）です。** 設計だけの回で、教材は作りません。`REVISION-PLAN.md` の書き方が参考になります。`UPDATE-PLAN.md` の決定（学年ごとに Unit 1 から数える・中2は `g2/`、中3は `g3/`・`master-vocab.json` はリセットしない・ヘッダーの学年切り替えは中2の最初の回）を前提にしてください。
- これで `UPDATE-PLAN.md` の工程1〜8（中1の単語テストと総合テスト5本）がそろいました。
- **review02 の大問5の本文で、空所が ( 1 ) → ( 3 ) → ( 2 ) の順に出てきます**（前回からの申し送り）。今回の工程外なので直していません。
- 前回までの申し送り（フッターの「各30問」表記、`REVISION-PLAN.md` 冒頭、`tpl-vocab.html` の `table.rule`（**12回目**）、単語テストの別解4組、判断が要る問題の要点表示をテンプレート側で別属性にする件、語彙照合スクリプトを `check.py` に入れるかどうか）は**未対応**のままです。
- リポジトリへの反映は 09-15 以降止まったままです。**今回反映が要るのは `units/review-final.html`（新規）・`index.html`・`STATUS.md`。トップページの「中1のまとめ」に総まとめテストが出るので、生徒の見え方が変わります。** 前回までの分（`units/review01.html`〜`review04.html`・`word-test.html`・`tools/tpl-review.html`・`tools/build.py`・`tools/check.py`・`STATUS-archive-2026-09-26.md`）がまだなら一緒に。

### 飛ばした操作

- **重複ファイルの片付けは不要でした。** ルート16件（フォルダ2件を含む）・`tools/` 11件・`units/` 36件を全件一覧し、同名の重複はありませんでした。
- **`word-index.html`・`tools/ref-*.html`・`tools/tpl-workbook.html`・`tools/tpl-vocab.html`・`tools/gen-word-test.*`・`REVISION-PLAN.md`・過去の `STATUS-archive-*.md` は落としていません。** 工程8に要らないためです。
- **承認待ちで止まった操作はありません。**

### Drive からの復元（今回使った方法）

前回と同じく、`download_file_content` を**サブエージェントに5本ずつ呼ばせるだけ**にして（9エージェント並列＋1本は自分で）、セッション記録（`subagents/*.jsonl` と `tool-results/*.txt`）から base64 を復号しました。記録を `json` で読み、`content`・`id`・`title` を持つ辞書を再帰的に拾う書き方です。復元した47本（`STATUS.md` を含む）すべてで Drive の `fileSize` とローカルのバイト数が一致し、UTF-8 として読めることも確かめています。一覧もサブエージェントに任せました（1ページ5〜10件で、ページの境目で1件重なることがあるので ID で重複を除く）。

### 所要時間

開始 2026-09-28 06:08（UTC）。検証を終え、アップロードと照合を含めておよそ40分。

---

## 2026-09-27（夜の枠／JST。開始 2026-09-27 16:13 UTC）　工程7：第4部（Unit 12〜16）の総合テスト `units/review04.html`

手順5の判定は**4番目で止まりました**。1番目（`word-test.html` あり・`--word-test` 11項目 NG 0件）、2番目（`index.html` に `word-test.html?unit=` が16件）、3番目（`tools/tpl-review.html` あり）を通過。`--review 1`・`--review 2`・`--review 3` はいずれも 18項目 NG 0件で、`units/review04.html` が無かったので**工程7**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `units/review04.html` | **新規**（64,819バイト） | units |
| `index.html` | 変更（第4部のまとめの「総合テスト　準備中」を `units/review04.html` へのリンクに。16,033→16,042バイト） | ルート |
| `STATUS.md` | 追記（この節を上に足した） | ルート |

`tools/` の道具（`tpl-review.html` `build.py` `check.py`）・`word-test.html`・単元の32本・`master-vocab.json`（4,330バイトのまま）・計画書類・`units/review01`〜`review03` は**変更していません**。本文は `python tools/build.py review 4 "第4部　表現を広げる" "Unit 12〜16" body.html` で組み立てました（部の名前は `index.html` の見出し「第4部　表現を広げる」に合わせました）。

### 中身（31問・100点）

- **大問1 文法 25点**（2点×5＋3点×5）：4択5問（Don't be noisy／can のうしろは原形 drive／is sleeping／were（複数主語＋last week）／went）・語形変化（run → ran）・並べかえ2問（Is your mother talking on the phone now? ／ We can see the sea from here.）・誤文訂正の直した箇所2問（yesterday なので is → was ／ Please のあとは原形 stops → stop）。Unit 12 が5点・Unit 13 が5点・Unit 14 が5点・Unit 15 が5点・Unit 16 が5点。
- **大問2 資料つきの読解 18点**（3点×6）：Midori Aquarium の Today's Shows（Show／Time／Place の3列・4行）と「水族館のきまり」3項目、ユキの日記（141語）。到着時刻の選択・表から数を1語（eleven）・Was 〜? の答えの選択・きまりの空所に1語（take、`take off 〜` は Unit 12 の熟語）・対話の空所に3語以上（Yes, they can.）・内容に合う文を2つ。
- **大問3 対話文の読解 21点**（3・4・4・3・4・3）：先週のことを話すケンとエマの対話（148語）。( A ) の選択（否定の命令文 Don't study too hard today.）・英問英答2問（He climbed Midori Mountain with his father. ／ She can walk all day.）・下線部 ① We had a very good time. を We を明らかにして日本語で・( B ) の選択（How was the weather?）・内容一致（進行形 A bird was flying over the lake.）。
- **大問4 条件英作文 10点**：Midori Aquarium と Midori Mountain の表（だれと・天気・したこと）を見て、先週の日曜日にどちらへ行ったかを「Last Sunday I went to 〜.」で書き始め、**because を使って25語以上**。
- **大問5 長文の読解 26点**（2×3・3×2・4・4・6）：エミの「はじめての英語のスピーチ」（142語）。( 1 )〜( 3 ) の選択（said／were waiting／was）・英問英答2問（She practiced in the music room. ／ It was cloudy.）・下線部 ① Mr. Brown listened to me and taught me many words. を me を明らかにして日本語で・4文を話の順に並べる・内容に合う文を2つ。

### 検証結果

- `python tools/check.py --review 4` … **18項目 NG 0件**（読解本文 141・148・142語、範囲より後の文法 0件、375px 横スクロールなし、印刷 A4 12ページ）。
- `--review 1`・`--review 2`・`--review 3` も **18項目 NG 0件**、`--word-test` は **11項目 NG 0件**、`--index` は **12項目 NG 0件**（第1〜4部すべて総合テストへのリンク、総まとめだけ「準備中」）。
- 語彙の照合：本文・選択肢・正解・模範解答・表に出る英語を、Unit 1〜16 の単語帳の見出し語（v-note と単語帳の一覧表を含む）＋基本語77語に照らして機械で走査。**最初の版で `notice` `oh` `bad` `thank` `wow` `out` `hi` `year` が範囲外**だったので、下の「自分で判断したこと」のとおり書き換え、**範囲外 0件**にしました。同じ走査を `review03.html` に当てると 0件になるので、照合の当たり方は前回と同じ厳しさです。
- playwright（chromium）で **320 / 375 / 414 / 768px**：`review04.html` は横スクロールなし（結果画面も375px）、`index.html` も 320・375px で横スクロールなし、`pageerror` 0件。
- 動作：全問に正解（記述は模範解答）を入れて採点 → **100点**（25/18/21/10/26）。再読み込みで**31問すべて途中保存から復元**し、採点しても 100点。「先生に送る」で **1080×4666px** の画像。3問に1問わざと間違えると **66点**で、Unit ごとの正答率（Unit 14 が43%・Unit 15 が51%・Unit 12 が55%に「見直し」の印）が出ました。
- 大問4は、模範解答の別解（Midori Mountain・35語）と**自分で書いた別の正答（32語）でどちらも 10/10**、`because` なしで13語だと **4/10**、`last Sunday I go to Midori Mountain with my friends because it is sunny`（語数不足・文頭小文字・ピリオドなし・過去形の落とし）だと **1/10** でした。

### 自分で判断したこと

1. **読解の題材は、計画の「日記・手紙・スピーチ」に合わせて日記（大問2）とスピーチ（大問5）にし、大問3は対話にしました。** 大問2の資料は水族館の上演表で、Unit 16 の `aquarium` `dolphin` `souvenir` `diary` `get to 〜` `before` が自然に使えます。
2. **`notice` が範囲外だったので、資料の見出しを英語の「Notice」から日本語の「水族館のきまり」に変えました。** review02・review03 の大問4 の表と同じで、見出しだけ日本語・中身は英語という形です。設問文も「「水族館のきまり」の ( X ) に入る語」に直しました。
3. **`Hi` `Oh` `Wow` `Thank you` `too bad` は、どれも単語帳にも基本語にも無いので使っていません。** あいさつは Unit 1 の見出し語 `hello` に、( A ) の選択肢は Unit 12 の見出し語 `sorry` を使った `I am sorry. Don't study too hard today.` に、`Wow, it is beautiful.` は `It is very beautiful.` に、Emma の `Thank you.` は review03 でも使った `I see.` に置き換えました。
4. **`out` が範囲外だったので、`the sun came out at twelve` を `it was sunny at twelve` にしました。** `sunny` は Unit 15 の見出し語です。
5. **`year` は単語帳では `~ years old`（Unit 1）の形しか扱っていないので、スピーチの「昨年」を月で書きました**（`In September`／スピーチ当日は `a cloudy Monday in October`）。月の名前は Unit 11 の単語帳の下の一覧表にあります。大問5の内容一致の選択肢も `in September` に直しています。
6. **未来の表し方を避けるため、進行形の文に `going to` を使っていません。** `\bgoing to\b` は `check.py` の `LATER_GRAMMAR` で未来の形として引っかかるので、移動は `walked to 〜` で書いています。`I want to 〜`（不定詞）・`enjoy 〜ing`（動名詞）・比較・受動態・現在完了も使っていません。
7. **`sat` `stood` `began` `told` `threw` は使いませんでした。** Unit 16 の単語帳の見出し語にある不規則変化は14語（came・took・wrote・bought・brought・caught・taught・met・ran・gave・found・heard・slept・sang）だけなので、それ以外の不規則過去形は避け、`walked` `started` `said` のように範囲内の語で書いています。
8. **大問3の英問英答の1問は、can の問い（What can Emma do all day?）にしました。** 対話の中に `Yes, we can.` があるため「Can Ken see the sea 〜?」では答えが本文そのままになってしまい、Unit 13 を問う意味が薄いと判断しました。`all day` は Unit 15 の熟語です。
9. **記述の要点（data-kw）は、review03 と同じく動詞の形まで含めました**（`he climbed` `she practiced` `it was`）。部分一致なので短い語だけにすると別の語に当たってしまいます。
10. **大問5の下線部の和訳は、代名詞が1つ（me）だけの文にしました。** 大問3の下線部が `We`（2人）を明らかにさせる問題なので、同じ形が2問続かないようにしています。

### 気になった点（申し送り）

- **次は工程8（中1の総まとめテスト `units/review-final.html`）です。** `REVIEW_SPEC` は Unit 1〜16・読解本文 100〜200語・条件英作文 25語以上。`check.py` は「範囲の Unit がすべて出題に入っている」を見るので、**16 の Unit すべてに `data-unit` を割り振る必要があります**（大問1を2点×5＋3点×5の10問にしても Unit は10個しか埋まらないので、読解の設問に複数 Unit を割り当てて残りを埋める作りが要ります）。`build.py` は `review final` に対応済みで、出力は `review-final.html`、単語テストへのリンクは `?grade=1` になります。作ったら `index.html` の `id="review-final"` の「準備中」をリンクに差し替えてください。
- **語彙の照合に使ったスクリプトは作業用で、Drive には置いていません。** 単語帳16本の `v-word`・`v-note`・一覧表と `basic-words.html` から許容語を組み、屈折形（-s/-es/-ed/-ing/-er/-est、y→ies、子音重ね）と人名・地名・曜日・月・`Mr.` などを除いて残りを報告するだけのものです。`check.py` に入れるかどうかは判断していません（誤検出があるので人が見る前提の道具です）。
- **review02 の大問5の本文で、空所が ( 1 ) → ( 3 ) → ( 2 ) の順に出てきます**（前回からの申し送り）。今回の工程外なので直していません。
- 前回までの申し送り（フッターの「各30問」表記、`REVISION-PLAN.md` 冒頭、`tpl-vocab.html` の `table.rule`（**11回目**）、単語テストの別解4組、判断が要る問題の要点表示をテンプレート側で別属性にする件）は**未対応**のままです。
- リポジトリへの反映は 09-15 以降止まったままです。**今回反映が要るのは `units/review04.html`（新規）・`index.html`・`STATUS.md`。トップページに第4部の総合テストが出るので、生徒の見え方が変わります。** 前回までの分（`units/review01.html`・`units/review02.html`・`units/review03.html`・`word-test.html`・`tools/tpl-review.html`・`tools/build.py`・`tools/check.py`・`STATUS-archive-2026-09-26.md`）がまだなら一緒に。

### 飛ばした操作

- **重複ファイルの片付けは不要でした。** ルート18件（フォルダ2件を含む）・`tools/` 11件・`units/` 35件を全件一覧し、同名の重複はありませんでした。
- **`units/unit01`〜`unit11`・`word-index.html`・`tools/ref-*.html`・`tools/tpl-workbook.html`・`tools/tpl-vocab.html`・`REVISION-PLAN.md`・過去の `STATUS-archive-*.md`（復元手順を読んだ2本を除く）は落としていません。** 工程7に要らないためです。
- **承認待ちで止まった操作はありません。**

### Drive からの復元（今回使った方法）

前回と同じく、`download_file_content` を**サブエージェントに呼ばせるだけ**にして、セッション記録（`subagents/*.jsonl` と `tool-results/*.txt`）から base64 を復号しました。**1つのサブエージェントに5本までにすると途中終了しません**（前回の「6本前後まで」より安全側）。復元した37本すべてで Drive の `fileSize` とローカルのバイト数が一致し、UTF-8 として読めることも確かめています。

- **復号スクリプトの注意**：記録から `{"content","id","title"}` を正規表現で拾う書き方は、エスケープされた base64（数万文字）に対して**破滅的バックトラックで止まります**。`json` で構造的に読む（`os.walk` で `*.jsonl` と `*.txt` を開き、`json.loads` した結果を再帰的にたどって `content`/`title` を持つ辞書を拾う）書き方にしてください。今回はそれで数秒で終わりました。

### Drive へのアップロード（今回わかった落とし穴）

`create_file` の `textContent` は**モデルのトークン出力を通る**ので、制御文字がそのまま運べません。今回 `STATUS.md` に**バックスペース（0x08）が2個**紛れており（python のヒアドキュメントで `\\b` を書いたつもりが `\b` = 0x08 になっていた。原文は正規表現の `\\bgoing to\\b`）、アップロードすると 0x08 が `\` + `b` の2文字に化けて **24,277 → 24,279 バイト**になりました。ローカル側の 0x08 を正しい2文字に直して照合し直しています。

- **`fileSize` の一致だけで安心しないこと。** base64 経路なら1文字ずれてもサイズは変わりません。**Drive から落とし直して `cmp`（または md5）で突き合わせる**のが確実です。今回は `units/review04.html`（md5 `d3a5c881c3317d86481cfaba45b7f3b3`）・`index.html`（`8c31fba3ab433628f201b9ea8d178010`）・`STATUS.md`（`7e92febfa637b3a2177e5344bfc3d95a`）の3本すべてで、落とし直した版とローカルが**1バイト残らず一致**しました。Drive のメタデータに md5 は返らないので、照合はこの方法になります。
- **python で STATUS.md を書くときは raw 文字列（`r"""…"""`）を使うこと。** `\b` `\n` `\t` が化けます。

### 所要時間

開始 2026-09-27 16:13（UTC）。検証を終え、アップロードと照合を含めておよそ55分。

---

## 2026-09-27（昼の枠／JST。開始 2026-09-27 06:08 UTC）　工程6：第3部（Unit 8〜11）の総合テスト `units/review03.html`

手順5の判定は**4番目で止まりました**。1番目（`word-test.html` あり・`--word-test` 11項目 NG 0件）、2番目（`index.html` に `word-test.html?unit=` が16件）、3番目（`tools/tpl-review.html` あり）を通過。`--review 1`・`--review 2` はどちらも 18項目 NG 0件、`units/review03.html` が無かったので**工程6**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `units/review03.html` | **新規**（64,392バイト） | units |
| `index.html` | 変更（第3部のまとめの「総合テスト　準備中」を `units/review03.html` へのリンクに。16,024→16,033バイト） | ルート |
| `STATUS.md` | 新しく立て直し（旧版は `STATUS-archive-2026-09-26.md` に改名） | ルート |

`tools/` の道具（`tpl-review.html` `build.py` `check.py`）・`word-test.html`・単元の32本・`master-vocab.json`（4,330バイトのまま）・計画書類は**変更していません**。本文は `python tools/build.py review 3 "第3部　語のはたらき" "Unit 8〜11" body.html` で組み立てました（部の名前は `index.html` の見出し「第3部　語のはたらき」に合わせました）。

### 中身（31問・100点）

- **大問1 文法 25点**（2点×5＋3点×5）：4択5問（前置詞のうしろの him／Does／Which ～, A or B?／on Sunday／How ～? By bus.）・語形変化（study → studies）・並べかえ2問（What time does your sister get up? ／ My uncle often shows us his pictures.）・誤文訂正の直した箇所2問（and で2人なら plays → play ／ Who → Whose）。Unit 8 が5点・Unit 9 が8点・Unit 10 が7点・Unit 11 が5点。
- **大問2 資料つきの読解 18点**（3点×6）：町の夏の教室の予定表（教室・曜日と時刻・場所・料金の4列）とミカの紹介文（131語）。時刻の選択・表から数を1語（eight）・Yes/No の答えの選択・名詞を代名詞に（them）・対話の空所に3語以上（She goes to the gym.）・内容に合う文を2つ。
- **大問3 対話文の読解 21点**（3・4・4・3・4・3）：エマの家族の写真をめぐるケンとエマの対話（139語）。( A ) ( B ) の選択（Who is the man next to you? ／ What do you do on your birthday?）・英問英答2問（He works at a hospital in London. ／ It is on May fifth.）・下線部 She takes care of it every morning. を She と it を明らかにして日本語で・内容一致。
- **大問4 条件英作文 10点**：Midori Zoo と Minami Museum の表（開いている時間・料金・見られるもの・駅から）を見て、トムにどちらをすすめるかを「〜 is good for Tom.」で書き始め、**because を使って20語以上**。
- **大問5 長文の読解 26点**（2×3・3×2・4・4・6）：リクの祖父（農家）についてのスピーチ（126語）。( 1 )〜( 3 ) の選択（gets／him／because）・英問英答2問（He gets up at five o'clock. ／ His aunt does.）・下線部 She loves them very much. を日本語で・4文を話の順に並べる・内容に合う文を2つ。

### 検証結果

- `python tools/check.py --review 3` … **18項目 NG 0件**（読解本文 131・139・126語、範囲より後の文法 0件、375px 横スクロールなし、印刷 A4 12ページ）。
- `python tools/check.py --index` … **12項目 NG 0件**（第1〜3部は総合テストへのリンク、第4部と総まとめは「準備中」）。`--review 1`・`--review 2`・`--word-test` も NG 0件のまま。
- 語彙の照合：本文・選択肢・正解・模範解答・表に出る英語を、Unit 1〜11 の単語帳の見出し語と基本語77語に照らして機械で走査。最初の版で `everyone` と `girl` が範囲外だったので `Hello.` と `the child` に直し、**残りは人名・地名・曜日・月の名前だけ**になりました（曜日と月は Unit 11 の単語帳の下の一覧表にある語）。
- playwright（chromium）で **320 / 375 / 414 / 768px**：`review03.html` の横スクロールなし（結果画面も375px）、`index.html` も 320・375px で横スクロールなし、`pageerror` 0件。
- 動作：全問に正解を入れて採点 → **100点**（25/18/21/10/26）。再読み込みで**31問すべて途中保存から復元**。「先生に送る」で **1080×4420px** の画像。3問に1問わざと間違えると **69点**で、Unit ごとの正答率（Unit 9 が63%・Unit 11 が66%で「見直し」の印）が出ました。大問4は Midori Zoo を選ぶ別解（26語）でも **10/10**、`midori zoo is good for Tom because he like animals`（語数不足・大文字なし・ピリオドなし・he like）だと **1/10**。

### 自分で判断したこと

1. **大問2の資料は「町の夏の教室の予定表」にしました。** 計画の「予定表・時刻表」に合わせ、Unit 11 の曜日・時刻・数（hundred yen）を使う問題を2問入れています。予定の話は未来の表し方を使いたくなるので、「毎年夏にある教室」「毎週〇曜日に通う」という**習慣の現在形**で書きました。
2. **表の見出しは `Class / Time / Place / Yen` の英語にしました。** いずれも単語帳にある語です（Place は Unit 10、Time・yen は Unit 11）。第2部のときの `Place` のような範囲外の見出しはありません。大問4の表は review02 と同じく行の見出しを日本語にし、中身だけ英語にしています。
3. **表の時刻は `10:00–11:30` とダッシュの前後を詰めました。** 375px で「10:00 –」「11:30」と2行に割れて読みにくかったためです。
4. **命令文（Unit 12）を避けるため、紹介文の終わりは `Which class is good for you?` にしました。** 「Look at 〜」「Choose 〜」のような呼びかけは使っていません。`I want to 〜`（不定詞）や `enjoy 〜ing`（動名詞）も避け、`enjoy it` の形にしています。
5. **大問5の「( 3 ) に入る語」は because にし、選択肢に so / but / or を並べました。** Unit 10 の「why には because で答える」をスピーチの中の問答で問う形です。review02 では本文中の空所が ( 1 ) → ( 3 ) → ( 2 ) の順に並んでいたので、今回は本文の出てくる順と番号をそろえました。
6. **英問英答の要点（data-kw）には、代名詞だけでなく動詞の形まで含めました**（`he works` `she goes` `gets up`）。要点の照合は部分一致なので、`he` だけだと `the` にも当たってしまうためです。
7. **`Who lives in Tokyo?`（疑問詞が主語）の答えは `His aunt does.` を模範解答にし、`His aunt lives in Tokyo.` も満点にしました。**

### 気になった点（申し送り）

- **review02 の大問5の本文で、空所が ( 1 ) → ( 3 ) → ( 2 ) の順に出てきます**（第3段落に ( 3 )、第4段落に ( 2 )）。採点は正しく動きますが、生徒は戸惑うかもしれません。今回の工程外なので直していません。直すなら本文の ( 3 ) と ( 2 ) の番号を入れ替え、設問の順（問2・問3）も合わせる必要があります。
- 第4部（Unit 12〜16）は命令文・can・進行形・過去形が使えるので日記・手紙が書けますが、`LATER_GRAMMAR` の不定詞・動名詞・比較・未来は引き続き使えません。日記は `I want to 〜` を書きたくなる題材なので注意が要ります。
- 前回までの申し送り（フッターの「各30問」表記、`REVISION-PLAN.md` 冒頭、`tpl-vocab.html` の `table.rule`（**10回目**）、単語テストの別解4組、判断が要る問題の要点表示をテンプレート側で別属性にする件）は**未対応**のままです。
- リポジトリへの反映は 09-15 以降止まったままです。**今回反映が要るのは `units/review03.html`（新規）・`index.html`・`STATUS.md`・`STATUS-archive-2026-09-26.md`（改名）。トップページに第3部の総合テストが出るので、生徒の見え方が変わります。** 前回までの分（`units/review01.html`・`units/review02.html`・`tools/tpl-review.html`・`tools/build.py`・`tools/check.py`）がまだなら一緒に。

### 飛ばした操作

- **重複ファイルの片付けは不要でした。** ルート17件（フォルダ含む）・`tools/` 11件・`units/` 34件を全件一覧し、同名の重複はありませんでした。
- **`units/unit01`〜`unit07` と `unit12`〜`unit16`（ワークブック）・`word-index.html`・`tools/ref-*.html`・`tools/tpl-workbook.html`・`tools/tpl-vocab.html` は落としていません。** 工程6に要らないためです。
- **承認待ちで止まった操作はありません。**

### 次回の対象

手順5の判定では、次は**工程7：第4部（Unit 12〜16）の総合テスト `units/review04.html`** になるはずです。要るもの：`units/unit12`〜`unit16`・`units/vocab01`〜`vocab16`、`basic-words.html`、`tools/tpl-review.html`、`tools/build.py`、`tools/check.py`、`index.html`。英作文は **25語以上**、読解本文は 90〜180語、題材は日記・手紙・スピーチ。作ったら `index.html` の `id="review4"` の「準備中」をリンクに差し替えてください。

### Drive からの復元（今回使った方法）

前回と同じく、`download_file_content` を**サブエージェントに呼ばせるだけ**にして、セッション記録（`subagents/*.jsonl` と `tool-results/*.txt`）から base64 を復号しました。3つのサブエージェントに10〜11本ずつ割り振ったところ、2つは「プロンプトが長すぎる」で途中終了しましたが、**終了前に呼んだ分は記録に残っていて、33本すべて復元できました**（全ファイルで Drive の `fileSize` とバイト数が一致）。1つのサブエージェントには大きな HTML を6本前後までにすると途中終了しにくいはずです。

### 所要時間

開始 2026-09-27 06:08（UTC）。検証を終え、アップロードと照合を含めておよそ30分。
