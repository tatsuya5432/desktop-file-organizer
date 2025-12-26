# Desktop File Organizer

デスクトップのファイルを自動的に整理するPythonアプリケーションです。

## 機能

- デスクトップ上のファイルを自動スキャン
- ファイルタイプごとに自動分類（画像、ドキュメント、テキストファイルなど）
- 適切なフォルダに自動移動
- テキストメモファイルを専用フォルダに整理

## インストール

```bash
pip install -r requirements.txt
```

## 使い方

### 基本的な使い方

```bash
python organizer.py
```

### オプション

```bash
# デスクトップのパスを指定
python organizer.py --desktop /path/to/desktop

# プレビューモード（実際には移動しない）
python organizer.py --dry-run

# カスタムルールファイルを使用
python organizer.py --config config.yaml
```

## フォルダ構造

整理後、以下のようなフォルダ構造になります：

```
Desktop/
├── Images/          # 画像ファイル (.jpg, .png, .gif など)
├── Documents/       # ドキュメント (.pdf, .docx, .xlsx など)
├── TextNotes/       # テキストファイル (.txt, .md など)
├── Videos/          # 動画ファイル (.mp4, .avi など)
├── Audio/           # 音声ファイル (.mp3, .wav など)
├── Archives/        # 圧縮ファイル (.zip, .tar.gz など)
├── Code/            # コードファイル (.py, .js, .html など)
└── Others/          # その他のファイル
```

## ライセンス

MIT License
