# Desktop File Organizer 📁✨

デスクトップのファイルを自動的に整理するPythonアプリケーションです。

散らかったテキストメモファイルや画像、ドキュメントを、たった1コマンドですっきり整理！

## ✨ 特徴

- 🔍 デスクトップ上のファイルを自動スキャン
- 📂 ファイルタイプごとに自動分類（画像、ドキュメント、テキストファイルなど）
- 🚀 適切なフォルダに自動移動
- 📝 テキストメモファイルを専用フォルダ（TextNotes）に整理
- 👀 プレビューモードで安全に確認してから実行可能

## 🚀 クイックスタート（3ステップ）

### 1. 必要なパッケージをインストール

```bash
# Windowsの場合
pip install -r requirements.txt

# Mac/Linuxの場合
pip3 install -r requirements.txt
```

### 2. まずはプレビューで確認（推奨）

```bash
# Windowsの場合
python organizer.py --dry-run

# Mac/Linuxの場合
python3 organizer.py --dry-run
```

これで、実際にファイルを移動せずに、どう整理されるか確認できます。

### 3. 問題なければ実行！

```bash
# Windowsの場合
python organizer.py

# Mac/Linuxの場合
python3 organizer.py
```

## 📖 詳しい使い方

**初めての方は、[初心者向けガイド（GUIDE_JA.md）](./GUIDE_JA.md)をご覧ください！**

ステップバイステップで、インストールから実行まで詳しく説明しています。

## 🎯 主な使い方

### プレビューモード（安全に確認）

```bash
python organizer.py --dry-run
```

### デスクトップのパスを指定

```bash
python organizer.py --desktop /path/to/desktop
```

### 詳細なログを表示

```bash
python organizer.py -v
```

## 📁 整理後のフォルダ構造

実行すると、デスクトップに以下のフォルダが自動作成され、ファイルが移動します：

```
Desktop/
├── TextNotes/       # 📝 テキストファイル (.txt, .md, .note など)
├── Images/          # 🖼️  画像ファイル (.jpg, .png, .gif など)
├── Documents/       # 📄 ドキュメント (.pdf, .docx, .xlsx など)
├── Videos/          # 🎬 動画ファイル (.mp4, .avi など)
├── Audio/           # 🎵 音声ファイル (.mp3, .wav など)
├── Archives/        # 📦 圧縮ファイル (.zip, .tar.gz など)
├── Code/            # 💻 コードファイル (.py, .js, .html など)
└── Others/          # 📋 その他のファイル
```

**特に、散らかりがちなテキストメモは `TextNotes` フォルダにまとめられます！**

## ❓ よくある質問

### 間違えて実行してしまった！元に戻せる？
ファイルは削除されていません。各フォルダから手動で元の場所に戻せます。

### 特定のファイルを整理したくない
隠しファイル（`.` で始まるファイル名）は自動的に除外されます。

### もっと詳しく知りたい
[初心者向けガイド（GUIDE_JA.md）](./GUIDE_JA.md)をご覧ください！

## 📝 ライセンス

MIT License
