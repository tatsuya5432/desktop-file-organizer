# Desktop File Organizer 使い方ガイド（初心者向け）

このガイドでは、デスクトップファイル整理ツールの使い方を、初心者の方でも分かるように一つずつ丁寧に説明します。

## 📋 目次

1. [必要なもの](#必要なもの)
2. [ステップ1: Pythonのインストール](#ステップ1-pythonのインストール)
3. [ステップ2: プログラムのダウンロード](#ステップ2-プログラムのダウンロード)
4. [ステップ3: 必要なパッケージのインストール](#ステップ3-必要なパッケージのインストール)
5. [ステップ4: プレビューモードで試す](#ステップ4-プレビューモードで試す)
6. [ステップ5: 実際にファイルを整理する](#ステップ5-実際にファイルを整理する)
7. [よくある質問](#よくある質問)

---

## 必要なもの

- パソコン（Windows、Mac、Linux のいずれか）
- Python 3.6 以上
- インターネット接続（初回のみ）

---

## ステップ1: Pythonのインストール

### Pythonが既にインストールされているか確認する

**Windows の場合:**
1. `Windows キー` を押す
2. 「cmd」と入力して `Enter` キーを押す
3. 黒い画面（コマンドプロンプト）が開いたら、以下を入力して `Enter` キーを押す：
   ```
   python --version
   ```

**Mac の場合:**
1. `Command + スペース` キーを押す
2. 「ターミナル」と入力して `Enter` キーを押す
3. 開いた画面で、以下を入力して `Enter` キーを押す：
   ```
   python3 --version
   ```

**Linux の場合:**
1. ターミナルを開く
2. 以下を入力して `Enter` キーを押す：
   ```
   python3 --version
   ```

### 結果の確認

- `Python 3.6.0` 以上のバージョンが表示されれば OK です！
- エラーが出た場合は、Pythonをインストールする必要があります

### Pythonのインストール方法（必要な場合のみ）

**Windows:**
1. https://www.python.org/downloads/ にアクセス
2. 「Download Python」ボタンをクリック
3. ダウンロードしたファイルを実行
4. **重要**: 「Add Python to PATH」にチェックを入れる
5. 「Install Now」をクリック

**Mac:**
1. https://www.python.org/downloads/ にアクセス
2. 「Download Python」ボタンをクリック
3. ダウンロードしたファイルを実行してインストール

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## ステップ2: プログラムのダウンロード

### 方法1: Gitを使う（推奨）

1. ターミナル（またはコマンドプロンプト）を開く
2. デスクトップに移動する：
   ```bash
   cd Desktop
   ```
3. プログラムをダウンロード：
   ```bash
   git clone https://github.com/あなたのユーザー名/desktop-file-organizer.git
   ```
4. ダウンロードしたフォルダに移動：
   ```bash
   cd desktop-file-organizer
   ```

### 方法2: ZIPファイルでダウンロード

1. GitHubのページにアクセス
2. 緑色の「Code」ボタンをクリック
3. 「Download ZIP」をクリック
4. ダウンロードしたZIPファイルを解凍
5. 解凍したフォルダをデスクトップに置く
6. ターミナルで、そのフォルダに移動：
   ```bash
   cd Desktop/desktop-file-organizer
   ```

---

## ステップ3: 必要なパッケージのインストール

プログラムを動かすために必要なパッケージをインストールします。

1. ターミナルで、プログラムのフォルダにいることを確認
   - `ls` (Macの場合は `ls`) と入力して、`organizer.py` が見えるはずです

2. 以下のコマンドを実行：

**Windows:**
```bash
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
pip3 install -r requirements.txt
```

3. インストールが完了するまで待ちます（数秒〜数十秒）

---

## ステップ4: プレビューモードで試す

**⚠️ 重要: 最初は必ずプレビューモードで試してください！**

プレビューモードでは、実際にはファイルを移動せず、どのように整理されるかだけを確認できます。

### 実行方法

**Windows:**
```bash
python organizer.py --dry-run
```

**Mac/Linux:**
```bash
python3 organizer.py --dry-run
```

### 結果の見方

画面に以下のような結果が表示されます：

```
デスクトップファイルを整理しています...
対象ディレクトリ: /Users/あなたの名前/Desktop

==================================================
ファイル整理の結果
==================================================
合計ファイル数: 15

【TextNotes】 5 ファイル
  メモ1.txt → /Users/あなたの名前/Desktop/TextNotes/メモ1.txt
  メモ2.txt → /Users/あなたの名前/Desktop/TextNotes/メモ2.txt
  TODO.md → /Users/あなたの名前/Desktop/TextNotes/TODO.md
  日記.txt → /Users/あなたの名前/Desktop/TextNotes/日記.txt
  アイデア.txt → /Users/あなたの名前/Desktop/TextNotes/アイデア.txt

【Images】 3 ファイル
  写真1.jpg → /Users/あなたの名前/Desktop/Images/写真1.jpg
  スクリーンショット.png → /Users/あなたの名前/Desktop/Images/スクリーンショット.png
  図.gif → /Users/あなたの名前/Desktop/Images/図.gif

【Documents】 2 ファイル
  レポート.pdf → /Users/あなたの名前/Desktop/Documents/レポート.pdf
  資料.docx → /Users/あなたの名前/Desktop/Documents/資料.docx

==================================================
※ プレビューモード: ファイルは実際には移動していません
  実際に移動するには --dry-run オプションを外して実行してください
```

### この結果を確認すること

- 各ファイルがどのフォルダに分類されるか
- 移動したくないファイルが含まれていないか
- 問題がなければ、次のステップへ進みます

---

## ステップ5: 実際にファイルを整理する

プレビューの結果を確認して問題なければ、実際にファイルを整理します。

### ⚠️ 実行前の注意事項

1. **重要なファイルはバックアップを取っておく**
2. プレビューモードの結果を確認済みであること
3. 移動したくないファイルがある場合は、事前に別の場所に移しておく

### 実行方法

**Windows:**
```bash
python organizer.py
```

**Mac/Linux:**
```bash
python3 organizer.py
```

### 実行後

デスクトップを確認すると、以下のようなフォルダが作成されています：

```
Desktop/
├── TextNotes/       ← テキストファイルがここに！
│   ├── メモ1.txt
│   ├── メモ2.txt
│   └── ...
├── Images/          ← 画像ファイルがここに！
├── Documents/       ← ドキュメントがここに！
├── Videos/
├── Audio/
└── ...
```

---

## よくある質問

### Q1: エラーが出ました！

**エラー: `python: command not found`**
- Pythonがインストールされていません
- [ステップ1](#ステップ1-pythonのインストール) に戻ってPythonをインストールしてください

**エラー: `デスクトップディレクトリが見つかりません`**
- デスクトップのパスを手動で指定してください：
  ```bash
  python organizer.py --desktop /path/to/your/desktop
  ```

**エラー: `ファイルへのアクセス権限がありません`**
- 管理者権限で実行してみてください（Windowsの場合、コマンドプロンプトを「管理者として実行」）

### Q2: 特定のファイルを整理したくない

整理したくないファイルは、事前に以下のいずれかを行ってください：
1. 別のフォルダに移動しておく
2. ファイル名の先頭に `.` をつける（隠しファイルになり、自動的に除外されます）

### Q3: 間違えて整理してしまった！元に戻せる？

ファイルは削除されていないので、手動で元の場所に戻すことができます。
各フォルダ（TextNotes、Imagesなど）を開いて、ファイルをデスクトップに戻してください。

### Q4: カスタムパスを指定したい

デスクトップ以外のフォルダを整理したい場合：
```bash
python organizer.py --desktop /path/to/folder
```

例：
```bash
# Windowsの場合
python organizer.py --desktop "C:\Users\YourName\Documents"

# Macの場合
python3 organizer.py --desktop ~/Documents
```

### Q5: もっと詳しいログが見たい

`-v` オプションをつけると、詳細な情報が表示されます：
```bash
python organizer.py -v
```

### Q6: テキストファイルだけを整理したい

現在のバージョンでは全ファイルが対象ですが、整理後に不要なフォルダを削除することで調整できます。

---

## 🎉 完了！

これでデスクトップがすっきり整理されました！

### 定期的な整理のコツ

1. 週に1回、このツールを実行する習慣をつける
2. ファイルをダウンロードしたら、その場で適切なフォルダに入れる
3. 不要なファイルは定期的に削除する

---

## 困ったときは

- GitHub Issuesで質問する
- README.mdの詳細情報を確認する
- プレビューモード（--dry-run）で何度でも安全に試せます

**Happy Organizing! 📁✨**
