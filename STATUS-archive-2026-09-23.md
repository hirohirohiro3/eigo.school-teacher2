# 制作の記録

> **2026-09-22（夜）にこのファイルを再び分割しました。** 09-20（夜）〜09-22（昼）の記録（Unit 8 の途中〜Unit 14）は `STATUS-archive-2026-09-22.md`（51,981 バイト）にそのまま入っています。Drive 上でファイル名を変えただけで、中身は1バイトも書き換えていません。それより前の記録は `STATUS-archive-2026-09.md` です。
>
> 分割したのは、本体が 52KB になり、追記のたびに全文を書き写してアップロードする必要があったためです（ツールの都合で、Drive へはファイルの中身を引数に書き写して渡すしかありません）。
>
> リポジトリに反映するときは、**古い `STATUS.md` を `STATUS-archive-2026-09-22.md` にリネームしてから、この新しい `STATUS.md` を置いてください。**

---

## 2026-09-23（昼）　新規単元なし。全16単元を再検証し、総索引 `word-index.html` を新規作成

### やったこと

| ファイル | 種別 | Drive |
|---|---|---|
| `word-index.html` | 新規作成（49,883 バイト） | ルートへアップロード |
| `index.html` | 変更（「総索引　準備中」をリンクに差し替え） | ルートへアップロード、旧版はゴミ箱 |
| `STATUS.md` | 変更（この節を追記） | ルートへアップロード、旧版はゴミ箱 |

`README.md` `PLAN.md` `tools/check.py` `tools/master-vocab.json` と `units/` の全32本は復元して読んだ・検査しただけで、変えていません。`REVISION-PLAN.md` `tools/build.py` `tools/tpl-workbook.html` `tools/tpl-vocab.html` は今回は落としていません（制作対象が無く、必要がなかったため）。

### 対象判定（手順5）

**Unit 1 から番号順に、機械判定を通しで実行しました。** `units/` の全32本（`unit01`〜`unit16`、`vocab01`〜`vocab16`）を Drive から復元し、`python tools/check.py NN --no-render` を16回。

- **全16単元とも 13項目中 NG 0件。** `unitNN_*.html` の欠けも、`vocabNN_*.html` の欠けもなし
- よって**新規作成・作り直しの対象は0件**。前回の申し送りのとおり、全16単元が新基準で完成しています

### 自分で判断したこと

1. **対象が無いので単元制作は行わず、総索引 `word-index.html` を作った。** `PLAN.md`「5. まだ決めていないこと」で**「総索引は全単元が終わってから。`master-vocab.json` から機械生成できる」**と条件づけられていたもので、その条件がいま満たされたためです。もう一方の `basic-words.html`（基本語リスト）は、同じ節で「Unit 1 の作り直し直後が適切」とされていて時期を外しており、載せる範囲も決まっていないので**作っていません**。
2. **CSS は新しく書いていない。** `word-index.html` は `index.html` の `<style>` ブロックをそのまま複製し、本文は `index.html` が既に持つクラス（`.sheet` `.site-head` `.tools` `.units` `.u-links a.vocab` `.part-note` `.foot`）だけで組みました。「CSS は触らない」に反しないようにするためです。**見た目を整えるなら、テンプレート側の変更として別途指示してください。**
3. **索引は `tools/master-vocab.json` から機械生成した。** 479語を先頭の文字で A〜Z に分け、各語に、その語をはじめて扱う単元の単語帳へのリンクを張っています。X で始まる語が無いので25文字分です。生成スクリプトは作業用で、Drive には置いていません。
4. **`tools/master-vocab.json` と `tools/check.py` はアップロードしていない。** 中身が変わっていないためです。`check.py` を単語帳つきで走らせると `master-vocab.json` が字下げ付きで書き直されますが、JSON として比較して復元時と同一であることを確認し、元の1行版に戻してあります。
5. **単元の検査は `--no-render` ではなく実レンダリングでも一部確かめた。** playwright を入れて `word-index.html` と `index.html` はスマホ幅・印刷とも実測しました。単元16本の再レンダリングは、前回までに確認済みで中身が変わっていないため省いています。

### 検証結果

- **Unit 1〜16、`python tools/check.py NN --no-render`：各13項目中 NG 0件**（16単元すべて）
- `master-vocab.json`：16単元・479語、**単元間の重複0語**、各単元 27〜34語ですべて 25〜40語のレンジ内
- `word-index.html`：見出し語479語をすべて収録（`master-vocab.json` と集合として一致、過不足0）、**リンク切れ0件**、語にそえた単元番号とリンク先ファイル名の単元番号が全件一致、JavaScript なし
- `word-index.html` はスマホ幅 375px で横スクロールなし（実測 375px）、印刷は A4 で12ページ。`index.html` も 375px で横スクロールなし・A4 3ページ
- スマホ幅のスクリーンショットを撮り、語のボタンが崩れず2列に並ぶことを目で確認した
- 復元の照合：復元した32本＋`check.py`＋`index.html`＋`master-vocab.json`＋`STATUS.md` は、すべて Drive の `fileSize` とローカルのバイト数が一致

### 気になった点（申し送り）

- **この定期実行は、いまのままでは次回以降も対象を見つけられません。** 昼（15:00 JST）と夜（1:00 JST）の2枠とも、手順5で必ず「対象なし」になります。**次の作業を指示文か `PLAN.md` に書き足すか、実行を止めるかを決めてください。**
- 残っている未作成ファイルは `basic-words.html`（基本語リスト）だけです。`check.py` の `BASIC` に載っている語（代名詞・be動詞・do/does/did・冠詞・接続詞・前置詞・疑問詞・数詞）がそのまま材料になりますが、**どこまで載せるか・どう並べるかが未決定**なので指示が要ります。
- 単語帳テンプレート（`tpl-vocab.html`）に `table.rule` の CSS が無い件（前回の申し送り）は、今回も手をつけていません。
- **Drive からの復元について、今回わかった補足。** `download_file_content` の結果は**およそ50,000文字を境に、超えるとツール出力ファイル（`tool-results/*.txt`）へ、それ以下は会話に直接返ります**。ワークブック（37KB〜53KB）は前者、単語帳（29KB〜38KB）は後者でした。どちらもセッション記録から python で `base64` 復号できます。単語帳16本は会話を埋めてしまうので、**サブエージェントに `download_file_content` だけを呼ばせ、その記録（`<セッションID>/subagents/agent-*.jsonl`）から拾いました**。そちらは `\"content\":\"...\"` とエスケープされて入っているので、復号の前にエスケープを外す必要があります。
- リポジトリへの反映は 09-15 以降止まったままです。人が反映してください。

### 飛ばした操作

- なし（承認待ちで止まった操作はありません）。
- Drive の重複ファイルは作業前の時点で0件でした（ルート・units・tools の3フォルダを一覧し、同名ファイルなし）。

### 次回の対象

**機械判定では対象なし。** 全16単元が新基準で完成し、総索引も作成済みです。残るのは `basic-words.html` ですが、内容が未決定のため**指示が必要です**。

### 所要時間

開始 06:08（UTC）、終了 06:35（UTC）ごろ。所要およそ27分。Drive からの復元（32本＋ツール類）と全16単元の検査が約12分、総索引の生成・検証が約6分、アップロードと照合が約9分でした。

## 2026-09-22（深夜）　Unit 16「一般動詞の過去形」を新規作成（全16単元がそろった）

### やったこと

| ファイル | 種別 | Drive |
|---|---|---|
| `units/unit16_general-past.html` | 新規作成 | units へアップロード |
| `units/vocab16_general-past.html` | 新規作成 | units へアップロード |
| `tools/check.py` | 変更（Unit 16 に対応する3点。下の「判断したこと」3） | tools へアップロード、旧版はゴミ箱 |
| `tools/master-vocab.json` | 変更（Unit 16 の29語を追加。累計479語） | tools へアップロード、旧版はゴミ箱 |
| `index.html` | 変更（Unit 16 の「準備中」をリンクに差し替え） | ルートへアップロード、旧版はゴミ箱 |
| `STATUS.md` | 変更（この節を追記） | ルートへアップロード、旧版はゴミ箱 |

`README.md` `PLAN.md` `REVISION-PLAN.md` `tools/build.py` `tools/tpl-workbook.html` `tools/tpl-vocab.html` は復元して読んだだけで、変えていません。

### 検証結果

`python tools/check.py 16`（playwright あり）で **17項目中 NG 0件**。

- 設問数 30問（A5／B6／C5／D7／E5／F2）＝ Unit 1〜15 と同じ構成
- 解答 30問、並べ替えの語群・語数とも一致（1語不要は2問、`data-extra="1"` と問題文の「1語不要」を両方つけた）、A・C・E に和訳なし
- 見出し語 29語（めやす 25〜40語）、重複なし、ワークブックの語の未収録 0語、例文の不一致 0件
- 読解本文 93語（めやす 80〜120語）。日記形式
- スマホ幅 375px で横スクロールなし（実測 375px）、印刷は A4 でワークブック18ページ・単語帳5ページ
- ［参考］解説に出ていない出題語 10語（`because` `bed` `early` `first` `friends` `soccer` `store` `weekend` `wet` `yuta`。すべて既出語か固有名詞）
- 後続の文法（未来形・不定詞・過去進行形・there is・比較・接続詞 when）が入っていないことを正規表現で全文走査して確認（0件）。Unit 16 は最後の単元なので、Unit 1〜16 の文法はすべて使える
- 図解2つ（played の文・Did の疑問文）と不規則動詞の一覧表、単語帳の項目は、スマホ幅でスクリーンショットを撮って崩れがないことを確認した
- **Unit 1〜15 のワークブックを全部 Drive から落とし、`check.py NN --workbook --no-render` で NG 0件を確認した。** Unit 1〜4 と 15 は単語帳も落として `check.py NN --no-render` で NG 0件。`check.py` を直したあとも Unit 1〜4・15 を再実行して NG 0件のまま

### 自分で判断したこと

1. **対象判定は Unit 1 から機械的に行った。** Unit 1〜15 のワークブックはすべて NG 0件、`unit16_*.html` が無かったので Unit 16 を対象とした。**Unit 5〜14 の単語帳は落とさなかった**（落とすと中身が会話に直接返り、1本あたりの分量が大きいため）。Unit 5〜14 の単語帳は前回までの実行で NG 0件が確認済みで、Drive 上で作成後に更新されておらず、`master-vocab.json` の Unit 1〜15 も今回の復元時点と一致していたので、単語帳側も OK と判断した。
2. **不規則動詞の過去形は、`check.py` の `IRREGULAR` を増やすのではなく見出し語に立てた**（came took wrote bought brought caught taught met ran gave found heard slept sang の14語）。Unit 9 の `has`、Unit 14 の `doing` と同じ解き方で、語数の確保にもなる。`IRREGULAR` に既にある went had did said got saw ate made は見出し語に立てず、単語帳の末尾に22語の「原形と過去形」表を置いた。
3. **`tools/check.py` を3点直した**（冒頭の説明にも追記した）。
   - 短縮形の表に `didn't`（→ do not）を足した。`wasn't` `weren't` と同じ扱い
   - `lemma` に、`-ied` → `-y`（studied → study）と、子音字を重ねた `-ed`（stopped → stop）を足した。前回の申し送りで予告されていた穴で、`-ing` 側（running → run）には既に同じ処理があった
   - 語の網羅チェックで、`-ed` `-ght` のような**ハイフンで始まる語尾の表記**を語として数えないようにした。解説で「-ed のつけ方」を説明すると `ed` が未収録語として NG になるため。`well-known` のような語中のハイフンには影響しない
   どれも判定をゆるめる方向だけの変更で、Unit 1〜4・15 を再実行して NG 0件のまま。
4. **PLAN の注意事項どおり、不規則動詞の一覧表（22語・例文つき）を解説に置いてから出題した。** 問題に出る不規則動詞はすべて表にある。表の過去形は一般動詞の色（橙、`gen-w`）にした。
5. **「なぜ形を変えるか」は Unit 15 と同じ言い回し**（英語はいつのことかを文の動詞の形で示す）にし、一般動詞の文では一般動詞が文の動詞なので一般動詞を過去形にする、と書いた。**did のうしろを原形に戻す理由**は「過去の印は did が引き受けているので、動詞まで過去形にすると過去を2回示すことになる」とし、Unit 9 の does と結びつけた。比喩は使っていない。
6. **-ed の綴りのルール表**（ふつう／e で終わる／子音字＋y／母音字＋y／子音字を重ねる）と、**-ed の読み方3通り**（［ド］［ト］［イド］）の表を置いた。y→i は Unit 9 の studies、子音字を重ねるのは Unit 14 の running と同じ理由だと書いた。誤った綴り `stoped` は `strike` で示した。
7. **Unit 15 の申し送り「was のうしろに一般動詞を置かない」を回収した。** 境界事例「was と did を取りちがえない」で `I was play tennis.` → `I played tennis yesterday.`、`Were you watch TV?` / `Did you busy?` を扱い、A5・C4 でも問うた。
8. **疑問詞が主語の文**（`Who made this cake? —— My mother did.` / `What happened last night?`）は、Unit 10・15 と同じ手順で「did を使わず動詞をそのまま過去形にする」と説明した。
9. **読解はユウタの日記（93語）。** 一般動詞の過去形が使えるようになったので、Unit 14・15 の対話ではなく README の「日記・手紙・対話」のうち日記にした。人名の所有格は `check.py` の固有名詞判定が拾えないため使っていない。
10. **見出し語は29語。** 動詞19（不規則動詞の過去形14＋arrive learn borrow invite happen）、名詞5（diary ticket aquarium dolphin souvenir）、前置詞1（before）、熟語4（have a good time / for the first time / on the way home / get to 〜）。関連語・対義語は v-note 内に置き、見出し語に立てていない（`bought ↔ brought` `before ↔ after` `get to 〜 ＝ arrive at 〜` など）。

### 気になった点（申し送り）

- **これで全16単元がそろった。** PLAN の「まだ決めていないこと」にある `basic-words.html`（基本語リスト）と `word-index.html`（総索引）は未作成のまま。総索引は `master-vocab.json`（Unit 1〜16、479語）から機械生成できる。次回の実行が Unit 1 から判定し直すと全単元 OK になり、作るものが無くなるので、次の作業を指示文か PLAN に書き足してください。
- 単語帳のテンプレート（`tpl-vocab.html`）には `table.rule` の CSS が無く、末尾の表（Unit 15 の be動詞の表、今回の不規則動詞の表）は罫線なしで表示される。崩れや横スクロールはないが、見た目を整えるならテンプレート側の変更が要る（今回は「CSS は触らない」に従い変えていない）。
- Drive からの復元・照合は前回と同じく、セッション記録の JSONL と `tool-results/*.txt` を python で走査して base64 を復号する方法で行った。アップロード後、`unit16_general-past.html` と `vocab16_general-past.html` は Drive から落とし直してローカルと `cmp` で1バイト残らず一致を確認。`index.html` `check.py` `master-vocab.json` `STATUS.md` は Drive の `fileSize` とローカルのバイト数の一致で照合した。
- `master-vocab.json` は前回と同じく改行なしの1行でアップロードした。中身は同じで、次に `check.py` を走らせると字下げ付きに戻る。
- リポジトリへの反映は 09-15 以降止まったままです。人が反映してください。

### 飛ばした操作

- なし（承認待ちで止まった操作はありません）。
- Drive の重複ファイルは作業前の時点で0件でした（ルート・units・tools の3フォルダを一覧し、同名ファイルなし）。

### 次回の対象

**全16単元が新基準で完成。** 次回の機械判定では対象が見つからないはずです。基本語リスト・総索引など、次の作業の指示が必要です。

### 所要時間

開始 16:03（UTC）、終了 16:22（UTC）ごろ。所要およそ19分。対象判定（Unit 1〜15 の復元と検査）と制作・検証が約10分、Drive へのアップロードと照合が約9分でした。

## 2026-09-22（夜）　Unit 15「be動詞の過去形」を新規作成

### やったこと

| ファイル | 種別 | Drive |
|---|---|---|
| `units/unit15_be-past.html` | 新規作成（48,669 バイト） | units へアップロード |
| `units/vocab15_be-past.html` | 新規作成（34,071 バイト） | units へアップロード |
| `tools/master-vocab.json` | 変更（Unit 15 の28語を追加。累計450語） | tools へアップロード、旧版はゴミ箱 |
| `index.html` | 変更（Unit 15 の「準備中」をリンクに差し替え） | ルートへアップロード、旧版はゴミ箱 |
| `STATUS.md` | 変更（分割して新しく立て、この節を記録） | ルートへアップロード。旧版はゴミ箱ではなく `STATUS-archive-2026-09-22.md` にリネーム |

`README.md` `PLAN.md` `REVISION-PLAN.md` と `tools/` の他の4ファイル（`build.py` `check.py` `tpl-workbook.html` `tpl-vocab.html`）は復元して読んだだけで、内容は変えていません。

### 検証結果

`python tools/check.py 15`（playwright あり）で **17項目中 NG 0件**。

- 設問数 30問（A5／B6／C5／D7／E5／F2）＝ Unit 1〜14 と同じ構成
- 解答 30問、並べ替えの語群・語数とも一致（1語不要は2問、`data-extra="1"` と問題文の「1語不要」を両方つけた）、A・C・E に和訳なし
- 見出し語 28語（めやす 25〜40語）、重複なし、ワークブックの語の未収録 0語、例文の不一致 0件
- 読解本文 117語（めやす 80〜120語）
- スマホ幅 375px で横スクロールなし（実測 375px）、印刷は A4 でワークブック15ページ・単語帳4ページ
- ［参考］解説に出ていない出題語 10語（`all` `aya` `brother` `club` `family` `friday` `math` `member` `saturday` `soccer`。すべて既出語か固有名詞）
- **後続単元の文法が混ざっていないことを機械的に確認した。** 英文を全文走査し、`-ed` で終わる語は `bed` `tired`（Unit 2 の形容詞）だけ、`will` `did` `went` `had` `going` は0件。`there` は副詞（`How was the weather there?`）だけです。過去進行形（was ＋ -ing形）も使っていません。
- 図解2つ（was の文・Were の疑問文）と単語帳の項目は、スマホ幅でスクリーンショットを撮って崩れがないことを確認した。
- Unit 14 も `check.py 14 --no-render` で NG 0件を再確認した（master-vocab.json の Unit 1〜14 は変わっていない）。

### 自分で判断したこと

1. **対象判定は、Unit 14 を機械チェックし、Unit 1〜13 は Drive の状態と前回までの記録で判定した。** units フォルダの一覧で Unit 1〜14 が2本ずつそろい、`unit15_*.html` が無かった。Unit 1〜13 は前回までの実行で NG 0件が確認済みで、その後 Drive 上で更新されていない。Unit 14 は見本として落としたので `check.py 14 --no-render` を走らせ、ワークブック・単語帳とも NG 0件。以上から Unit 15 を対象と決めた（前回までと同じ判断）。
2. **「なぜ形を変えるか」は、「英語はいつのことかを文の動詞の形で示す。be動詞の文では be動詞が文の動詞なので、be動詞を過去の形にする」と書いた。** 日本語が文末の「でした」で過去を示すこととの対比です。比喩は使っていません。
3. **「現在は3つ、過去は2つ」を表で示した。** am と is はどちらも was、are だけが were。you は1人でも were であることを、Unit 1 の you are と結びつけました。
4. **過去を示す語を1節立てた**（yesterday / last 〜 / 〜 ago / then / at that time）。境界として **`last` の前に `on` `in` をつけない理由**（last そのものが「いつの」を示す）と、**`ago` は時間の長さのうしろ**を書き、誤文訂正にも `on last Sunday` を入れた。
5. **`Were you 〜? —— Yes, I was.` の答え方を独立して説明した。** 入試の対話問題で頻出で、Unit 2 の `Are you 〜? —— Yes, I am.` と同じしくみだと書きました。誤文訂正（`Yes, I were.`）と選択（A3）でも問うています。
6. **「was のうしろに一般動詞を置かない」を境界事例に入れたが、正しい形（一般動詞の過去形）は書いていない。** Unit 16 の内容を先に使わないためで、「Unit 16 で学ぶ」とだけ書きました。誤文 `I was play tennis.` も、よくある間違いや設問には入れていません（正答を示せないため）。
7. **「学校を休む」「学校に遅れる」を be動詞の熟語（be absent from 〜 / be late for 〜）として立てた。** 一般動詞の過去形を使わずに入試頻出の過去の文を書ける形で、「日本語では動作のように言うが、英語ではようすとして言う」と説明しました。`late` は Unit 2 の既出語です。
8. **疑問詞は How was 〜?（感想・ようす）を中心にした。** 会話で最もよく使うためです。Who が主語の文（`Who was absent from school yesterday? —— Ken was.`）は Unit 10・14 と同じ手順で説明しました。
9. **読解は月曜の朝のアヤとエマの会話（対話、117語）。** 日記・手紙は一般動詞の過去形なしでは不自然になるため、be動詞だけで書ける対話にしました（Unit 14 と同じ判断）。人名の所有格は、`check.py` の固有名詞判定が拾えないため使っていません。
10. **見出し語は28語。** 名詞11（week month weather trip vacation concert test temple elementary school fun）、形容詞11（last sick sad angry nervous full empty dirty cloudy windy exciting great）、副詞2（yesterday ago）、熟語4（at that time / all day / be absent from 〜 / be late for 〜）。`was` `were` `wasn't` `weren't` は `check.py` の基本語・短縮形の表にあるので見出し語に立てず、単語帳の末尾に「be動詞の現在形と過去形」の表を置きました。
11. **`elementary school` は並べ替え（B6）で `elementary / school` の2語に分けた。** `check.py` の複合語の例外リストに無いためです。見出し語は `elementary school`（名詞）1つです。
12. **`exciting` は -ing で終わるが形容詞であることを単語帳に書いた。** Unit 14 の -ing形と混同しないためです。
13. **単語帳の関連語・対義語は v-note 内に置き、見出し語に立てていない**（`full ↔ empty` `dirty ↔ clean` `sad ↔ happy` `yesterday / today / tomorrow` `week → month → year` など）。
14. **STATUS.md を分割した**（冒頭の注記のとおり）。旧版は trash_file ではなく `update_file` で `STATUS-archive-2026-09-22.md` に改名しました。中身を書き写す量（約52KB）を減らし、書き写しでずれる危険をなくすためです。
15. **`REVISION-PLAN.md` は今回は復元して読んだ。** 内容は README の難度基準に反映済みで、今回の制作で新たに従うべき点はありませんでした。変更していないのでアップロードもしていません。

### 気になった点（申し送り）

- **Drive からの復元は、今回はすべて python で行い、手での書き写しをなくした。** `download_file_content` の結果は、大きいものはツール出力ファイル（`tool-results/*.txt`）に、小さいものは会話に直接返りますが、**会話に直接返った結果もセッション記録（`/root/.claude/projects/-home-claude/<セッションID>.jsonl`）に残っている**ので、その JSONL を python で走査し、`{"content","id","title"}` の形の結果を `base64` で復号してファイルに書き出しました（抽出スクリプトは作業用で、Drive には置いていません）。全ファイルが Drive の `fileSize` と一致しました。前回までのような書き写しのずれは起きません。次回もこの方法が使えるはずです。
- **アップロードは、これまでと同じく本文を引数に書き写す方式。アップロード後の照合は全ファイルで中身まで行った。** `unit15_be-past.html` `vocab15_be-past.html` `index.html` は Drive から落とし直し、上と同じ方法で復号して、ローカルと1バイト残らず一致することを `cmp` で確認した。`master-vocab.json` は中身（JSON として）が一致。
- **`master-vocab.json` は改行・字下げなしの1行の JSON でアップロードした**（4,041 バイト）。書き写す量を減らすためで、中身は同じです。`check.py` は次に走らせたときに字下げ付き（`indent=1`）で書き直すので、次回以降は元の形に戻ります。
- この `STATUS.md` は Drive の `fileSize` とローカルのバイト数で照合した。
- 次の Unit 16（一般動詞の過去形）は新規単元で、全16単元の最後です。PLAN の注意事項どおり **不規則変化の一覧表を解説に置いてから出題すること。** `check.py` の `IRREGULAR` には `went` `had` `did` `said` `got` `saw` `ate` `made` しか入っていないので、`came` `took` `wrote` `bought` などを使うと未収録語として NG になります。見出し語側に立てるか（Unit 9 の `has`、Unit 14 の `doing` と同じ解き方）、`check.py` を直すかの判断が要ります。規則変化の `-ed` は `lemma` が `-ed` と `-d` を落とすので `played` `lived` は通るはずですが、`studied`（y→ied）と `stopped`（子音重ね）は寄らない可能性があります。先に確かめてください。
- Unit 15 で `yesterday` `last` `ago` `week` `month` を立てたので、Unit 16 では過去を示す語を新出語に数えられません。語数が足りないときは、不規則動詞の過去形を見出し語に立てることで補えます。
- リポジトリへの反映は 09-15 以降止まったままです。人が反映してください。

### 飛ばした操作

- なし（承認待ちで止まった操作はありません）。
- Drive の重複ファイルは作業前の時点で0件でした（ルート・units・tools の3フォルダを一覧し、同名ファイルなし）。

### 次回の対象

**Unit 16（`general-past`／一般動詞の過去形）の新規作成。** `master-vocab.json` は Unit 1〜15 の450語を持っています（Unit 15 で28語追加）。

### 所要時間

開始 11:01（UTC）、終了 11:18（UTC）ごろ。所要およそ17分。制作（ワークブック・単語帳・検証）が約7分、Drive へのアップロードと照合が約10分でした。
