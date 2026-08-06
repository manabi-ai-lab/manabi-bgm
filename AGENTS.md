# AGENTS.md — このリポジトリで作業するAIエージェントへ

manabi-ai-lab のフリーBGMシリーズの公開リポジトリ。Codex・Claude など、どのエージェントがここで作業する場合も、この文書が標準指示。**まず `STATUS.md` を読んで現在地を把握してから動くこと。**

## 絶対に守るルール

1. **動画・音声の再エンコード、変換、圧縮、音量調整、メタデータ変更を一切しない。** このプロジェクトの最優先事項は画質・音質の保全。容量を減らしたい場合も分割（`scripts/split-for-backup.sh`）で対応する
2. **配布物の正当性は SHA-256 で判定する。** 期待値は `tracks/<slug>/CHECKSUMS.md`。一致しないファイルは結合にも Release にも YouTube にも使わない
3. **`*_スマホDrive版` と名の付くファイルは低画質の受け渡し用。** 配布・投稿には一切使わない
4. **MP4 / .bin を git にコミットしない**（.gitignore で除外済み。`-f` で入れない）。大容量配布は GitHub Release のアセットで行う
5. **Release のアセット名は ASCII にする。** GitHub は非ASCII文字を削除してファイル名を壊す（実例：`放課後…mp4` → `_1._.mp4`）。日本語名はReleaseノートで「リネームしてよい」と案内する
6. **認証情報を扱わない。** GitHub・YouTube 等のログインが必要になったら、自分で入力せずユーザー（あっきー）に操作を渡す
7. **想定外の状況では、回避策を自作せず停止して報告する。** 破壊的操作（削除・上書き・公開）の前は特に
8. 確認できないことは記録に「不明」と書く。それらしい値で埋めない

## 作業の型

- 大きな作業は**フェーズに分割**し、フェーズの終わりで停止してユーザーの確認を待つ（実例：`docs/PROMPT_CODEX.md` の2フェーズ構成）
- 報告には、実測値（サイズ・ハッシュ全文）・実行したコマンド・できなかったことと理由を含める
- 作業後は記録を更新する：`STATUS.md`（ログと**次の一歩**）、`tracks/<slug>/` の各記録欄
- 新しい曲の作業は `docs/PLAYBOOK.md` の工程順に従い、`templates/` から `tracks/<slug>/` を作る

## よくある依頼と参照先

| 依頼 | 参照 |
| --- | --- |
| 高画質版の復元・照合 | `docs/RESTORE.md` ＋ `scripts/restore-and-verify.sh` |
| Release 作成 | `docs/RELEASE.md` ＋ `scripts/create-release.sh`（照合込み） |
| 次作用の分割バックアップ | `scripts/split-for-backup.sh` |
| YouTube 投稿設定 | `docs/YOUTUBE.md`（手順）＋ `tracks/<slug>/YOUTUBE.md`（正本） |
| ショート制作 | `tracks/<slug>/SHORTS.md`（設計原則：ループ周期の整数倍＋冒頭フック） |
| 投稿用コピペ素材 | `tracks/<slug>/COPYPASTE.md`（実URL反映済み。無ければ作る） |

## 環境ごとの得意分野

| 環境 | 得意 | 苦手 |
| --- | --- | --- |
| Codex（あっきーのPC） | Google Drive からのダウンロード、`gh` での Release 操作、ローカルの大容量ファイル | — |
| Claude（リモート環境） | 文書・記録・検証、ショートのレンダ、TikTok代行投稿 | Drive接続不可・Releaseアセットのアップロード不可（Codexに依頼する） |

互いにできないことは、押し通さずにもう一方への依頼として報告に書くこと。
