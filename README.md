# Desktop File Organizer 📁✨

デスクトップやダウンロードフォルダのファイルを自動的に整理するPythonアプリケーションです。

散らかったテキストメモファイルや画像、ドキュメントを、たった1コマンドですっきり整理！

## ✨ 特徴

- 🔍 デスクトップ、ダウンロードフォルダのファイルを自動スキャン
- 📂 ファイルタイプごとに自動分類（画像、ドキュメント、テキストファイルなど）
- 🚀 適切なフォルダに自動移動
- 📝 テキストメモファイルを専用フォルダ（TextNotes）に整理
- 💾 ダウンロードフォルダ専用のスクリプトも付属
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

**デスクトップを整理する場合:**
```bash
# Windowsの場合
python organizer.py --dry-run

# Mac/Linuxの場合
python3 organizer.py --dry-run
```

**ダウンロードフォルダを整理する場合:**
```bash
# 方法1: organizerスクリプトを使う
python organizer.py --downloads --dry-run

# 方法2: ダウンロード専用スクリプトを使う
python downloads_organizer.py --dry-run
```

これで、実際にファイルを移動せずに、どう整理されるか確認できます。

### 3. 問題なければ実行！

**デスクトップを整理:**
```bash
# Windowsの場合
python organizer.py

# Mac/Linuxの場合
python3 organizer.py
```

**ダウンロードフォルダを整理:**
```bash
# 方法1
python organizer.py --downloads

# 方法2
python downloads_organizer.py
```

## 📖 詳しい使い方

**初めての方は、[初心者向けガイド（GUIDE_JA.md）](./GUIDE_JA.md)をご覧ください！**

ステップバイステップで、インストールから実行まで詳しく説明しています。

## 🎯 主な使い方

### プレビューモード（安全に確認）

```bash
# デスクトップ
python organizer.py --dry-run

# ダウンロードフォルダ
python organizer.py --downloads --dry-run
```

### ダウンロードフォルダを整理

```bash
# 方法1: --downloadsオプションを使う
python organizer.py --downloads

# 方法2: 専用スクリプトを使う
python downloads_organizer.py
```

### カスタムパスを指定

```bash
# デスクトップのパスを指定
python organizer.py --desktop /path/to/desktop

# ダウンロードフォルダのパスを指定
python downloads_organizer.py --path /path/to/downloads
```

### 詳細なログを表示

```bash
python organizer.py -v
python downloads_organizer.py -v
```

## 📁 整理後のフォルダ構造

実行すると、デスクトップまたはダウンロードフォルダ内に以下のフォルダが自動作成され、ファイルが移動します：

```
Desktop/ または Downloads/
├── TextNotes/       # 📝 テキストファイル (.txt, .md, .note など)
├── Images/          # 🖼️  画像ファイル (.jpg, .png, .gif など)
├── Documents/       # 📄 ドキュメント (.pdf, .docx, .xlsx など)
├── Videos/          # 🎬 動画ファイル (.mp4, .avi など)
├── Audio/           # 🎵 音声ファイル (.mp3, .wav など)
├── Archives/        # 📦 圧縮ファイル (.zip, .tar.gz など)
├── Code/            # 💻 コードファイル (.py, .js, .html など)
├── Executables/     # 🚀 実行ファイル (.exe, .dmg, .deb など)
└── Others/          # 📋 その他のファイル
```

**特に、散らかりがちなテキストメモは `TextNotes` フォルダに、ダウンロードした実行ファイルは `Executables` フォルダにまとめられます！**

## ❓ よくある質問

### 間違えて実行してしまった！元に戻せる？
ファイルは削除されていません。各フォルダから手動で元の場所に戻せます。

### 特定のファイルを整理したくない
隠しファイル（`.` で始まるファイル名）は自動的に除外されます。

### もっと詳しく知りたい
[初心者向けガイド（GUIDE_JA.md）](./GUIDE_JA.md)をご覧ください！

## 📝 ライセンス

MIT License
