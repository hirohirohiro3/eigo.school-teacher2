# 制作の記録

> **2026-10-04（昼）にこのファイルを分割しました。** 10-02（夜）の順7：中2 Unit 6、10-03（昼）の順8：中2 Unit 7、10-03（夜）の順9：中2 Unit 8 の記録は `STATUS-archive-2026-10-03.md` にそのまま入っています。それより前は `STATUS-archive-2026-10-02.md`、`STATUS-archive-2026-10-01.md`、`STATUS-archive-2026-09-30.md`、`STATUS-archive-2026-09-28.md`、`STATUS-archive-2026-09-26.md`、`STATUS-archive-2026-09-24.md`、`STATUS-archive-2026-09-23-night.md`、`STATUS-archive-2026-09-23.md`、`STATUS-archive-2026-09-22.md`、`STATUS-archive-2026-09.md` です。
>
> 手順は前回と同じで、**古い `STATUS.md` を `update_file` で改名し、この新しい `STATUS.md` を置いています。**アーカイブ側の中身は1バイトも触っていません。リポジトリに反映するときは、改名されたアーカイブ（`STATUS-archive-2026-10-03.md`）とこの新しい `STATUS.md` の両方を置いてください。「Drive からの復元」「Drive へのアップロード」の要点は下に書き写してあります。

---

## 2026-10-05（昼の枠／JST。開始 2026-10-05 06:08 UTC ＝ 15:08 JST）　順12：中2 Unit 11（不定詞（形容詞的用法）と 疑問詞 + to 不定詞）

手順5の判定：1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り）は通過。N=1〜10 は Drive に `g2/unit*_*.html`・`vocab*_*.html` がそろい、復元して `python tools/check.py N --grade 2` を走らせ、1〜10 すべて NG 0件。`g2/unit11_*.html` が無い N=11 で止まったので、**順12＝中2 Unit 11（スラッグ `infinitive-adjective`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit11_infinitive-adjective.html` | **新規**（50,924バイト） | g2 |
| `g2/vocab11_infinitive-adjective.html` | **新規**（37,042バイト） | g2 |
| `g2/index.html` | 変更（16,483 → 16,551バイト）Unit 11 をリンクに（`li class="ready"`、単語帳は「36語」） | g2 |
| `tools/master-vocab.json` | 変更（8,010 → 8,375バイト）`"g2-11"` を追加 | tools |
| `STATUS.md` | 変更（追記） | ルート |

**`tools/check.py`・`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません**（`check.py` は復元直後の写しと `cmp` で一致）。

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「名詞 ＋ to ＋ 原形 ＝『〜するための』『〜するべき』」（`I have a lot of homework.` → `I have a lot of homework to do.` の `transform`・`something ← to drink` の `diagram is-general`・**1語の形容詞は名詞の前、2語以上のまとまりは名詞のうしろ**という理由づけ）→「something ／ anything ＋ to 〜」（肯定・疑問・否定・すすめる文の表。中1 Unit 6 の some／any の使い分けにつなげた）→「3つのはたらきを並べる」（**to のすぐ前が動詞／言い終わった文・気持ちの形容詞／名詞**で Unit 9・10・11 を分ける表）→「疑問詞 ＋ to ＋ 原形」（how／what／where の表、`I don't know.` → `I don't know how to use this machine.` の `transform`）→「know ／ learn ／ tell と組む」（`tell 人 how to 〜` を中2 Unit 8 の「人 ＋ もの」につなげた）→ なぜ `what to do it` としないか → 判定手順4段 → 境界事例4つ（〜すること／〜するための、something ＋ 形容詞 ＋ to、前置詞が最後に残る `something to write with`、how to と what to の使い分け）→ 入試での出方 → よくある間違い4つ → まとめ → 例文、の順です。
- `PLAN-g2g3.md` 3節 Unit 11 の3点はすべて入れました：①`something to eat`／`time to go` 型（`I had no time to eat breakfast.` など）②**how to／what to／where to を同じ単元に同居**③**how to は know／learn／tell と組む形を中心に**（表・B8・D19・D23・読解）。
- **読解**：アヤのスピーチ「はじめての料理」（両親が忙しい土曜日に、祖母に電話で作り方を聞いて弟にカレーを作る）。本文148語（めやす 120〜160語）。下線部①が `I didn't know what to do first.`（和訳）、②が `I have a lot of things to learn.`（`to learn` が説明している語 `things` を1語で書きぬく）。E3 は `Who told Aya how to make curry?` に `Her grandmother did.` と3語で答えさせる設問です。
- **単語帳**：新出語 **36語**（めやす30〜40語）。代名詞3（anything everything myself）・名詞18（thing recipe meat potato onion carrot sugar bowl plate machine button screen line exit tourist schedule price left）・動詞6（mix boil press discuss guess describe）・熟語5（Would you like 〜?／a piece of 〜／a glass of 〜／go straight／change trains）・形容詞3（sweet spicy correct）・副詞1（easily）。累計は中1 479語＋中2 397語＝**876語**。

### 検証結果

- **`check.py 11 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・見出し語36語・重複なし・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳4ページ）。
- **後続文法の検査**（`LATER_GRAMMAR_G2` のうち first が12以上の形と中3分（99）を、英文352本＝`<span class="en">`・解答キー・読解本文の文、に1文ずつ当てる。誤答例の行・選択肢・パートCは除く）：**当たり0件**。`-ing` は `something`・`anything`・`everything` の3語だけで、動名詞・進行形は使っていません。`than`／`more`／`most`／`better`／`best`・`as 〜 as`・受動態・現在完了・`too 〜 to`・`It is 〜 to`・人 ＋ to（`tell me to` など）・間接疑問・関係代名詞もすべて0件。
- **中1の既存の検査はすべて NG 0件**：`check.py 1`〜`16`・`--index`・`--word-test`・`--review 1`〜`4`・`--review final`。
- **中2の既存の検査もすべて NG 0件**：`check.py 1`〜`10 --grade 2`・`--index --grade 2`。
- **`master-vocab.json`**：中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-10"` は復元直後の写し（8,010バイト）とキーごとに突き合わせて**完全に一致**。増えたのは `"g2-11"` の36語だけです。
- **playwright（Chromium）**：`g2/unit11`・`g2/vocab11`・`g2/index.html`・`index.html`・`word-test.html`・`units/review01.html`・`units/review-final.html`・`g2/unit10` の8本を375px幅で開き、**scrollWidth 375px・はみ出した要素0個・JS の例外0件**（テストページはボタン・選択肢をクリックしたあとも0件）。`file://` から Google Fonts を取りに行く通信だけが失敗しますが、実行環境に外へ出る経路が無いためで、ページの不具合ではありません。
- **未定義クラス0件**（本文の `class="..."` をテンプレートの CSS と突き合わせ）。新しい2本と `g2/index.html` に `<script>` は0件、外部読み込みは Google Fonts だけ。

### 自分で判断したこと

1. **`Would you like 〜?` を別の熟語として見出し語に立てました**（Unit 9・10 から持ち越しの判断）。Unit 9 の `would like to 〜`（〜したい）とは、うしろに名詞を置き相手にすすめる点で使い方がちがうため、単語帳でも「〜はいかがですか」として分け、メモで Unit 9 の形との違いを書いています。答え方 `Yes, please.`／`No, thank you.` も解説に載せました。
2. **すすめる文では疑問文でも `something` を使う**ことを表の1行として明示しました（`Would you like something to drink?`）。C15 の `Do you have cold something to drink?` は `something cold` に直すのが正解で、解答に `anything cold to drink` でも正解と書いています。
3. **疑問詞 ＋ to は how／what／where の3つに絞りました。** `which to`・`when to` は PLAN の指定に無く、`check.py` の正規表現（first 11）には含まれますが、出題・解説とも使っていません。
4. **`It's time to 〜` は使いませんでした。** `It is 〜 to`（中3 Unit 5）と形が似て混乱しやすいため、`time to 〜` の例は `I had no time to eat breakfast.` にしています。
5. **前置詞が残る形（`something to write with`）を境界事例に1つだけ置きました。** 入試で出る形ですが、出題はしていません（解説の範囲にとどめた）。
6. **固有名詞は並べかえの語群に入れませんでした。** 語群は小文字で示すため、`kyoto` のように小文字になった固有名詞は `check.py` の語の網羅で未収録として拾われます。B7 は `this town` にしています。同じ理由で、所有格つきの人名（`Aya's`）も本文から外しました（E3 の別解の書き方を変更）。
7. **`north`・`Blue Line` を使わないことにしました。** 方角の語（east／west／south／north）はどれも未収録で、1語のために見出し語を増やさないよう `near the exit`・`Which line goes to the museum?` に書き換えています。

### 気になった点（次の回への申し送り）

- **次は順13＝中2 Unit 12（動名詞、スラッグ `gerund`）です。** `PLAN-g2g3.md` の要注意事項どおり、不定詞と動名詞の使い分け表（enjoy／finish／stop は動名詞のみ、want／hope／decide は不定詞のみ、like／start／begin はどちらも）、**前置詞のうしろは動名詞**（`good at playing`）の独立した説明、`stop to 〜` と `stop 〜ing` の境界事例を入れてください。
- Unit 12 で `-ing` が正面から使えるようになります。今回までの単元では、`-ing` の動名詞は1語も使っていません。
- `could` は引き続き使えません（中3 Unit 13 まで）。方角の語（east など）も未収録のままです。
- `word-test.html` の中2の語（順18）は中2 Unit 16 まで作ってからです。今回までで中2は397語（Unit 1〜11）。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です。順26（中3 Unit 1）までは着手に影響しません。

### 飛ばした操作

- **なし。** 5フォルダ（ルート・units・tools・g2・g3）を一覧し、同名ファイルの重複が無いことを確認しました（`g3/` は空、ルートは23本、`units/` は37本、`tools/` は11本、`g2/` は作業前21本）。回帰検査のため `units/` の37本・`word-test.html`・`tools/tpl-review.html`・`g2/` の Unit 1〜10 の20本も復元し、すべて Drive の `fileSize` と一致しました（計70本）。

---

## 2026-10-04（夜の枠／JST。開始 2026-10-04 16:13 UTC ＝ 10-05 01:13 JST）　順11：中2 Unit 10（不定詞（副詞的用法））

手順5の判定：1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`master-vocab.json` が `"g2-N"` のキーで積む作り）は通過。N=1〜9 は Drive に `g2/unit0N_*.html`・`vocab0N_*.html` がそろい、復元して `python tools/check.py N --grade 2` を走らせ、1〜9 すべて NG 0件。`g2/unit10_*.html` が無い N=10 で止まったので、**順11＝中2 Unit 10（スラッグ `infinitive-adverb`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit10_infinitive-adverb.html` | **新規**（51,836バイト） | g2 |
| `g2/vocab10_infinitive-adverb.html` | **新規**（38,210バイト） | g2 |
| `g2/index.html` | 変更（16,421 → 16,483バイト）Unit 10 をリンクに（`li class="ready"`、単語帳は「36語」） | g2 |
| `tools/check.py` | 変更（61,764 → 61,861バイト）`IRREGULAR` に `used → use` の1行を追加 | tools |
| `tools/master-vocab.json` | 変更（7,586 → 8,010バイト）`"g2-10"` を追加 | tools |
| `STATUS.md` | 変更（追記） | ルート |

**`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。**

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「to ＋ 原形 ＝『〜するために』（目的）」（`I went to the park.` → `I went to the park to play tennis.` の `transform`・**to 〜 を取ると文が成り立つかどうかで Unit 9 と分ける表**）→「Why 〜? の答えに使う」（`To 〜.` と `Because 〜` の2通りを表で並べ、`For catch 〜` が誤りである理由）→「to ＋ 原形 ＝『〜して』（原因）」（happy／glad／sad／surprised／excited の表。**気持ちを表す語と組むという条件を明示**）→「前置詞の to と不定詞の to」→「3つのはたらきを並べる」（名詞的用法・目的・原因の一覧。**用法名は覚えなくてよいと明記**）→ 判定手順4段 → 境界事例4つ（〜すること／〜するために／for ＋ 動詞は不可／enter のうしろに to を置かない／気持ちを表さない形容詞には使わない）→ 入試での出方 → よくある間違い4つ → まとめ → 例文、の順です。
- `PLAN-g2g3.md` 3節 Unit 10 の2点はどちらも入れました：①**目的（〜するために）と原因（〜して）を独立した見出しで分けた** ②**`I went to the park to play tennis.` の to が「公園へ」の to と別物であることを `diagram is-general` の図解で分けた**（「to のすぐうしろが名詞なら前置詞、動詞の原形なら不定詞」の1行の見分け方と、4行の対照表つき）。Unit 9 の境界事例（`I want to go to the park.`）を土台として本文で参照しています。
- **読解**：ユウタのスピーチ「マークと過ごした一週間」（交換留学生のホストファミリーになった一週間）。本文148語（めやす 120〜160語）。下線部①が `Before he arrived, I cleaned my room to welcome him.`（和訳）、②が `I am very glad to meet your family.`（うれしく思った**原因**を表す部分＝`to meet your family` の4語を書きぬく）。E3 は `Why did Yuta clean his room?` に `To welcome Mark.` と**3語で答えさせる**設問で、解説の「Why 〜? の答えに使う」と対応しています。
- **単語帳**：新出語 **36語**（めやす30〜40語）。動詞7（welcome communicate realize support reach respect thank）・熟語5（say hello to 〜／such as 〜／go back to 〜／take a walk／at the same time）・名詞18（host family exchange student hometown experience custom chopsticks gesture opinion information exercise energy earth college conversation sentence mistake purpose flight）・形容詞5（different similar several both shy）・副詞1（clearly）。累計は中1 479語＋中2 361語＝**840語**。

### 検証結果

- **`check.py 10 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・見出し語36語・重複なし・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳5ページ）。
- **後続文法の検査**（`LATER_GRAMMAR_G2` のうち first が11以上の形を、英文315本＝`<span class="en">`・解答キー・読解本文の文、に1文ずつ当てる。誤答例の行・選択肢・パートCは除く）：**当たり0件**。目で見る検査も0件：`than`／`more`／`most`／`better`／`best` 0件、`as 〜 as` 0件、`have`／`has`／`had` ＋ 過去分詞 0件、`how`／`what`／`where` ＋ `to` 0件、`something`／`anything` ＋ `to` ＋ 動詞 0件、「名詞 ＋ to ＋ 原形」（形容詞的用法の疑い）0件。`-ing` は `evening`・`morning`・`something` の3語だけで、進行形も動名詞も使っていません。
- **中1の既存の検査はすべて NG 0件**：`check.py 1`〜`16`・`--index`・`--word-test`・`--review 1`〜`4`・`--review final`。**`check.py` を変える前（復元直後の61,764バイト版）と後の両方で同じ27＋5項目を走らせ、出力に差分が無いことを `diff` で確認しています。**
- **中2の既存の検査もすべて NG 0件**：`check.py 1`〜`9 --grade 2`・`--index --grade 2`。
- **`master-vocab.json`**：中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-9"` は復元直後の写し（7,586バイト）とキーごとに突き合わせて**完全に一致**。増えたのは `"g2-10"` の36語だけです。
- **playwright（Chromium）**：`g2/unit10`・`g2/vocab10`・`g2/index.html`・`index.html`・`word-test.html`・`units/review01.html`・`units/review04.html`・`units/review-final.html`・`g2/unit09` の9本を375px幅で開き、**scrollWidth 375px・はみ出した要素0個・JS の例外0件**（テストページは選択肢と各ボタンをすべてクリックしたあとも0件）。`file://` から Google Fonts を取りに行く通信だけが失敗しますが、これはこの実行環境に外へ出る経路が無いためで、ページの不具合ではありません。
- **未定義クラス0件**（本文の `class="..."` をテンプレートの CSS と突き合わせ）。新しい2本と `g2/index.html` に `<script>` は0件、外部読み込みは Google Fonts（`fonts.googleapis.com`・`fonts.gstatic.com`）だけ。

### 自分で判断したこと

1. **`could` を1語も使わないことにしました。** 読解の下書きで `I could not make long sentences.` と書いたところ、`could` が語の網羅で未収録になりました。`can` は中1 Unit 13 の既出語ですが、**`could`（can の過去形）を扱う単元は中2の16単元のどこにも無く**、`UPDATE-PLAN-g2g3.md` では中3 Unit 13（仮定法）で would／could に絞ると決めています。`IRREGULAR` に足して通すのは「その単元より後で扱う文法事項を先に使わない」に反するため、本文を `I studied English hard, but long sentences were difficult for me.` に書き直しました。**次の回も `could` は使えません。**
2. **`check.py` の `IRREGULAR` に `used → use` を足しました。** これは文法ではなく `lemma()` の穴です。`lemma()` は `-ed` を落とす処理に `len(w) > 4` の条件があるため、**4文字の `used` だけが `use` に寄らず**、既出語の `use` でカバーされませんでした（`played`・`cleaned` などは5文字以上なので通ります）。`He used gestures to help me.` は図解にも読解にも要る文なので、語を避けるのではなく道具側を直しました。**カバー範囲が増えるだけの変更なので既存の検査を落とす向きには働きません**が、念のため変更前後で中1・中2の全検査を走らせて出力が同一であることを確認しています。他に4文字の `-ed` 形が出たときも同じ対処で構いません。
3. **原因の用法に使う形容詞を happy／glad／sad／surprised／excited の5つに絞り、すべて既出語で済ませました。** `PLAN.md` の「解説に出さないものは出題しない」に合わせ、`disappointed` などは入れていません。あわせて「気持ちを表す形容詞と組む」という条件を規則として書き、`I was busy to go out.` が成り立たない例を置きました。
4. **`enter のうしろに to は置かない` を境界事例に立てました。** 前置詞の to との混同がこの単元の最大のつまずきなので、`to the park`（正）と `to enter to college`（誤）を対にすると効きます。`enter`／`visit`／`reach` と `go`／`come`／`walk` の対比表も入れました。`reach` は今回の新出語です。
5. **`We must do something to protect the earth.` を `We must plant trees to protect the earth.` に差しかえました。** `something to protect` は「守るための何か」＝形容詞的用法（中2 Unit 11）と読めてしまい、先取りに見えます。**`something`／`anything` ＋ `to` ＋ 動詞は Unit 11 まで使えません。**
6. **`example` を見出し語に立てませんでした。** `for example` が中1の既出の熟語で、`check.py` は熟語を語ごとにばらしてカバー範囲に入れるため、`example` は新出語になりません。代わりに `such as 〜` を熟語として立て、`for example` との使い分け（文頭か、名詞のうしろか）をメモに書きました。
7. **E3 を「英語3語で答える」と語数を指定しました。** `To welcome Mark.` と答えさせたいところで、`He cleaned his room to welcome Mark.` のような文で答えても内容は合ってしまうためです。解説の `To 〜.` の形と対応させています。
8. **B の「1語不要」の不要語は `happy` と `for` にしました。** 動名詞（`-ing`）は Unit 12 で正解になる形なので、Unit 9 と同じ方針で不要語にも誤答の選択肢にも混ぜていません。

### 気になった点（次の回への申し送り）

- **次は順12＝中2 Unit 11（不定詞の形容詞的用法と 疑問詞 + to 不定詞、スラッグ `infinitive-adjective`）です。** `PLAN-g2g3.md` の要注意事項どおり、`something to eat`／`time to go` の形と、`how to`／`what to`／`where to` を同じ単元に同居させてください。`how to` は `know`／`learn`／`tell` と組む形が中心です。
- **今回 `something to protect` を避けた判断（上の5）をそのまま土台に使えます。** Unit 11 では `something to 〜` が主役になるので、「名詞のうしろから説明する」形として正面から扱えます。
- **`would like to 〜`（中2 Unit 9 の既出語）と `Would you like 〜?` の扱いは、Unit 9 の申し送りのまま未判断です。** `Would you like something to drink?` は Unit 11 の形容詞的用法とよく組むので、この回で `Would you like 〜?` を別の熟語に立てるかを決めてください。
- `word-test.html` の中2の語（順18）は中2 Unit 16 まで作ってからです。今回までで中2は361語（Unit 1〜10）。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です。順26（中3 Unit 1）までは着手に影響しません。

### 飛ばした操作

- **なし。** 5フォルダ（ルート・units・tools・g2・g3）を一覧し、同名ファイルの重複が無いことを確認しました（`g3/` は空、ルートは22本、`units/` は37本、`tools/` は11本、`g2/` は作業前19本）。回帰検査のため `units/` の37本・`word-test.html`・`tools/tpl-review.html`・`g2/` の Unit 1〜8 の16本も復元し、すべて Drive の `fileSize` と一致しました（計55本＋最初の14本）。

---

## 2026-10-04（昼の枠／JST。開始 2026-10-04 06:08 UTC ＝ 15:08 JST）　順10：中2 Unit 9（不定詞（名詞的用法））

手順5の判定：1番目（`g2/index.html` あり・`check.py --help` に `--grade` あり・`"g2-N"` のキーで積む作り）は通過。N=1〜8 は Drive に `g2/unit0N_*.html`・`vocab0N_*.html` がそろい、復元して `python tools/check.py N --grade 2` を走らせ、1〜8 すべて NG 0件。`g2/unit09_*.html` が無い N=9 で止まったので、**順10＝中2 Unit 9（スラッグ `infinitive-noun`）**です。

### 作ったもの・変えたもの

| ファイル | 種別 | 置き場所 |
|---|---|---|
| `g2/unit09_infinitive-noun.html` | **新規**（49,313バイト） | g2 |
| `g2/vocab09_infinitive-noun.html` | **新規**（37,903バイト） | g2 |
| `g2/index.html` | 変更（16,363 → 16,421バイト）Unit 9 をリンクに（`li class="ready"`、単語帳は「36語」） | g2 |
| `tools/check.py` | 変更（61,668 → 61,764バイト）`IRREGULAR` に `began → begin` の1行を追加 | tools |
| `tools/master-vocab.json` | 変更（7,201 → 7,586バイト）`"g2-9"` を追加 | tools |
| `STATUS.md` | **新しく立て直し**（古い版は `STATUS-archive-2026-10-03.md` に改名） | ルート |

**`tools/build.py`・`units/` の中1のファイル・`index.html`・`word-test.html`・テンプレート・計画書類は1バイトも変えていません。**

### 中身

- **ワークブック**：30問（A 5／B 6（うち「1語不要」2問）／C 5／D 7／E 5／F 2）。解説は「to ＋ 動詞の原形 ＝『〜すること』」（`want a new bike` → `want to buy a new bike` の `transform`・「文の動詞は wants だけ」の図解）→「to のうしろは必ず原形」（三単現・過去・否定でも原形の表と、**なぜ原形のままか**＝時と主語は文の動詞が表している）→ **中1 Unit 13 の can と同じ理屈であることを図解（can play ＝ to play）と本文で明示**（will・must にも触れる）→ to ＋ 原形をとる動詞の表（want／like／try／hope／need／start・begin／decide／would like）→ want to be 〜 → 否定文・疑問文 → 主語・補語になる形 → 判定手順4段 → 境界事例4つ（前置詞の to との見分け／want 〜 と want to 〜／have to・be going to も to ＋ 原形／try to は「しようとする」）→ 入試での出方 → よくある間違い4つ → 例文、の順です。
- `PLAN-g2g3.md` 3節 Unit 9 の3点はすべて入れました：①**名詞的用法から入り「to のうしろは原形」を最初に固める**（最初の見出しの直後に独立した小見出し・表・A 1〜2番・C 12番・C 16番）②**主語になる to は1例だけ**（`To read books is fun.`。出題はなし）、目的語（want to／like to／try to）を中心に ③**中1 Unit 13 の can のうしろの原形と同じ理屈**（図解・本文・まとめ）。
- **読解**：ケンタのスピーチ「私の夢」（技術者になりたい。おじに連れられたロボットのショー、コンピューター部でのロボット作り）。本文160語（めやす 120〜160語の上限）。下線部①が `After the show, I decided to make my own robot.`（和訳）、②が `My goal is to make robots for people in hospitals.`（`My goal` と同じものを指す部分＝補語の7語を書きぬく）。
- **単語帳**：新出語 **36語**（めやす30〜40語）。動詞5（continue design improve solve introduce）・熟語5（would like to 〜／come true／grow up／all over the world／these days）・名詞20（job world goal engineer scientist chef writer artist musician designer firefighter police officer language culture robot space skill clothes lesson novel）・形容詞4（foreign own simple real）・副詞2（especially actually）。累計は中1 479語＋中2 325語＝**804語**。

### 検証結果

- **`check.py 9 --grade 2`：17項目 NG 0件**（パート構成・設問数30・解答数30・並べ替えの語群と語数・和訳の有無・語の網羅 未収録0語・例文一致 不一致0件・見出し語36語・重複なし・375px 横スクロールなし・印刷 A4 ワークブック16ページ／単語帳5ページ）。
- **後続文法の検査**（`LATER_GRAMMAR_G2` のうち first が10以上の形を、英文331本＝`<span class="en">`・読解本文の文・解答キー。誤答例の行・選択肢・パートCは除く、に1文ずつ当てる）：**当たり0件**。目で見る検査も0件：`than`／`more`／`most`／`as` 0件、`have`／`has`／`had` ＋ 過去分詞 0件、`how`／`what`／`where` ＋ `to` 0件、`something to` 0件、`It is` 0件。`-ing` は進行形（`were dancing`・`am trying`・`are trying`）、`be going to`、熟語 `go shopping`（中2 Unit 3 の見出し語）だけです。**目的の to（副詞的用法）も使っていません**（`to` ＋ 動詞はすべて want／like／try／hope／need／start／begin／decide／would like の目的語か、be動詞のうしろの補語、主語1例）。
- **中1の既存の検査はすべて NG 0件**：`--index`・`--word-test`・`--review 1`〜`4`・`--review final`・`check.py 16`。**`check.py` を変える前後の両方で走らせて確認しています。**
- **中2の既存の検査もすべて NG 0件**：`--index --grade 2`・`check.py 1`〜`8 --grade 2`。
- **`master-vocab.json`**：中1のキー（`"1"`〜`"16"`、479語）と `"g2-1"`〜`"g2-8"` は作業前の写し（復元直後の7,201バイト）とキーごとに突き合わせて**完全に一致**。増えたのは `"g2-9"` の36語だけです。
- **playwright（Chromium）**：`g2/unit09`・`g2/vocab09`・`g2/index.html`・`index.html`・`word-test.html`・`units/review01.html`・`units/review-final.html` の7本を375px幅で開き、**scrollWidth 375px・はみ出した要素0個・ページのJSエラー0件**（テストページは選択肢を選んでボタンを押したあとも0件）。
- **未定義クラス0件**（本文の `class="..."` をテンプレートの CSS と突き合わせ）。新しい2本と `g2/index.html` に `<script>` は0件、外部読み込みは Google Fonts だけ。

### 自分で判断したこと

1. **`would like to 〜` を熟語の見出し語に立て、解説の表にも入れました。** 中2の教科書では不定詞の名詞的用法と同じ課で扱うのがふつうで、入試の会話文でも頻出です。`would` を単独の見出し語には立てず（助動詞 would は中3の仮定法で扱う）、「`want to 〜` のていねいな言い方」として決まった言い方で覚える扱いにしました。`LATER_GRAMMAR_G2` の仮定法の正規表現（`if I were`・`I wish`）には当たりません。
2. **`check.py` の `IRREGULAR` に `began → begin` を足しました**（`told`／`sent` を足した前回と同じ扱い）。`begin` は中1 Unit 14 の既出語で、`It began to rain in the afternoon.` の1文のために見出し語を立てるのは筋が通らないためです。中1・中2の検査を前後で走らせて影響0件を確認しています。
3. **主語になる to は解説で1例（`To read books is fun.`）だけにし、出題しませんでした。** `PLAN-g2g3.md` の「1〜2例にとどめる」に従いました。「中3でもう一度扱います」と日本語で書くだけにして、`It is 〜 to …`（中3 Unit 5）の英文は出していません。
4. **前置詞の to との見分けは、境界事例で `I want to go to the park.` の1文だけで扱いました。** 目的の to（`went to the park to play tennis`）は次の Unit 10 の中心なので、英文には出していません。
5. **誤答の選択肢は既出語と to ＋ 動詞の形だけで組みました**（`to buys`・`to wrote`・`is want` など）。動名詞（`-ing`）を誤答に混ぜると、Unit 12 で正解になる形を「誤り」として見せてしまうので避けました。
6. **パートA 2番の主語は最初 `Ms. Sato's daughter` でしたが、`daughter` が未収録語になり、`Sato's` も固有名詞の除外に引っかからなかったので `My cousin` に差しかえました。** 所有格の `'s` がついた人名は語の網羅で未収録になります。次の回も気をつけてください。
7. **パートD 17番は（want を使う）と指定したので、`would like to` の別解は書きませんでした。**

### 気になった点（次の回への申し送り）

- **次は順11＝中2 Unit 10（不定詞の副詞的用法、スラッグ `infinitive-adverb`）です。** `PLAN-g2g3.md` の要注意事項どおり、目的（〜するために）と原因（〜して）の2つに分け、**`I went to the park to play tennis.` の to が「公園へ」の to と別物であることを図解で分けてください。** 今回の境界事例「to のうしろが名詞なら前置詞の to」（`I want to go to the park.`）をそのまま土台に使えます。
- 原因の用法（`I was happy to hear 〜`）は `glad`・`happy`・`sad`・`surprised` が既出なので、新出語を増やさずに書けます。
- **`would like to 〜` は中2 Unit 9 で既出**になりました。Unit 11 の形容詞的用法（`something to drink`）と組んだ `Would you like something to drink?` を使うなら、`Would you like 〜?` は別の熟語として立てるかを判断してください。
- `word-test.html` の中2の語（順18）は中2 Unit 16 まで作ってからです。今回までで中2は325語（Unit 1〜9）です。
- 中3 Unit 9 の whose・関係副詞は `UPDATE-PLAN-g2g3.md` でまだ「保留」です。順26（中3 Unit 1）までは着手に影響しません。

### 飛ばした操作

- **なし。** 5フォルダ（ルート・units・tools・g2・g3）を一覧し、同名ファイルの重複が無いことを確認しました（`g3/` は空、`units/` は37本、`g2/` は作業前17本）。回帰検査のため `units/` の単語帳16本・総合テスト5本・`unit16`・`word-test.html`・`tools/tpl-review.html`・`g2/` の Unit 1〜8 の16本も復元し、すべて Drive の `fileSize` と一致しました（計52本）。

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
