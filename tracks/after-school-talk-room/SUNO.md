# Suno制作情報 — 放課後トークルーム

2026-08-06 に ChatGPT（じぴ）側の履歴・ファイルから回収した情報で更新済み（`docs/PROMPT_GPT.md` の方式）。
「不明」は**両方のAIの記録になかった**項目です。憶測では埋めていません。

---

## 基本

| 項目 | 値 |
| --- | --- |
| 制作サービス | Suno |
| プラン | Pro / Premier 契約中（**どちらの契約だったかは不明**） |
| 生成日 | **2026-08-06**（v2: 09:13:49 UTC ＝ 18:13:49 JST） |
| モデルバージョン | 不明（「利用可能な最新モデル」を提案した記録のみ。選択したモデル名の記録なし） |
| アカウント名 | あっきー |
| 曲名 | 放課後トークルーム |
| 採用バージョン | **v2** |
| v2 の曲ID | `650f1687-bd5b-457a-b244-d964c2d84784` |
| v1 の曲ID | `eb5fa8c4-8c9b-422d-ad9d-d12cf8658883` |
| 曲URL | 不明（IDのみ記録） |
| 形式 | インストゥルメンタル |

### なぜプランの記録が重要か

Suno の商用利用可否は「**生成した時点で有料プランだったか**」で決まります。
本作は**有料プラン契約期間中の生成**であることは記録済み。Pro / Premier のどちらだったかが未確定なので、
Suno のアカウント設定や請求履歴で確認できたらここを更新してください。

---

## プロンプト

> ⚠️ 以下は**制作時にChatGPTが提示した文**として履歴に残っているもの。
> **実際にSunoへ貼り付けたことまでは確認できていない。** Sunoの作品ページで実入力値を確認できたら確定に格上げする。

### スタイルプロンプト（提示文）

```
Cute and friendly instrumental background music for livestream chatting and casual YouTube talk videos. Bright modern Japanese pop atmosphere, warm electric piano, soft marimba, gentle plucked synth, light pizzicato strings, subtle lo-fi drums, and rounded bass. 102 BPM, major key, simple repeating motif, low melodic density, stable relaxed energy, voice-friendly arrangement, clean polished mix, short gentle intro, seamless looping feel, cheerful after-school classroom atmosphere.
```

### 除外スタイル（提示文）

```
vocals, singing, spoken words, choir, rap, dramatic orchestral music, heavy bass, aggressive drums, distorted guitar, EDM drops, sudden transitions, tempo changes, intense solos, sound effects
```

### その他の設定（提示値）

| 項目 | 値 |
| --- | --- |
| Instrumental | オン |
| Weirdness | 25% |
| Style Influence | 75% |
| 希望尺 | 3〜4分（実際の出力は希望より短い） |

---

## バージョン比較

| | v1 | v2（採用） |
| --- | --- | --- |
| ファイル | 放課後トークルーム.mp3 | 放課後トークルーム2.mp3 |
| 長さ | 119.712秒 | 124.632秒 |
| Integrated loudness | -14.40 LUFS | -14.53 LUFS |
| True Peak | -0.39 dB | -1.18 dB |
| LRA（ラウドネスレンジ） | 2.00 | 1.70 |
| サイズ | 2,938,920 バイト | 3,057,984 バイト |
| 形式 | MP3 / 48kHz / stereo / 約196kbps | 同左 |

**v2 を採用した理由**：会話用BGMとして使いやすいと判断（履歴上の記録）。
LRAが小さく（展開が平坦で）、True Peak に余裕がある点も会話用途に合致。
v1 はオープニング用途として残す案が出ていた。編曲・メロディー面の差を文章化した記録は不明。

---

## 1時間化の方法

| 項目 | 値 |
| --- | --- |
| 元クリップ | v2（124.632秒） |
| ループ回数 | **31周** |
| 継ぎ目の処理 | **6秒クロスフェード**（具体的なフィルター式は不明） |
| 使用ツール | ffmpeg（コマンド全文・プリセットは不明） |
| 作業場所 | ChatGPT側の作業環境 |

### 制作中のトラブル（重要な記録）

最初に作った **59分59.97秒版に AAC破損** が確認された。
音声を作り直して破損のない3600秒版を作成し、最終MP4は映像のフレーム単位の都合で **3600.08秒** になった。

→ 教訓：**1時間化したら AAC の健全性と複数地点の継ぎ目を検査してから次工程へ**（`docs/PLAYBOOK.md` に反映済み）

---

## 音の設計メモ（この曲の狙い）

- **会話用**であることが最優先。声とぶつかる帯域を張らせない（voice-friendly arrangement）
- 102 BPM・メジャーキー・反復モチーフ・低い旋律密度で、1時間聴いても疲れない
- 放課後の教室の空気感。やさしく明るいが、テンションは上げすぎない
- ラウドネスは -14.6 LUFS / True peak -1.0 dBFS（YouTube基準に合わせ済み）

---

## 素材ファイルの所在

| ファイル | サイズ | 所在 |
| --- | --- | --- |
| 放課後トークルーム.mp3（v1） | 2,938,920 バイト | Drive ＋ ChatGPT作業領域 |
| 放課後トークルーム2.mp3（v2） | 3,057,984 バイト | Drive ＋ ChatGPT作業領域 |

> ChatGPTの作業領域は一時的なもの。**Drive側を正**とする。

---

## 次の曲へ引き継ぐこと

- [ ] Sunoの**モデル名・曲URL・実入力プロンプト・スライダー値を生成直後に保存**する（今回の最大の欠落）
- [ ] 採用理由を「印象」だけでなく、会話への干渉・音量・ピーク・展開の強さ（LRA）で記録する
- [ ] Pro / Premier のどちらで生成したかをその場で書く

## あっきーが確認できたら更新する項目

- [ ] 生成時のプラン（Pro か Premier か）→ Sunoの請求履歴
- [ ] モデルバージョン → Sunoの作品ページ
- [ ] 曲URL → 作品ページのURL（IDは記録済みなので照合できる）
- [ ] スタイルプロンプトの実入力値 → 作品ページ
