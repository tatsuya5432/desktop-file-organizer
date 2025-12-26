# クイックリファレンス 🚀

すぐに使えるコマンド集です。コピー＆ペーストで使えます！

## 📌 最初にやること（1回だけ）

### Windows
```bash
# プログラムのフォルダに移動
cd Desktop\desktop-file-organizer

# 必要なパッケージをインストール
pip install -r requirements.txt
```

### Mac/Linux
```bash
# プログラムのフォルダに移動
cd Desktop/desktop-file-organizer

# 必要なパッケージをインストール
pip3 install -r requirements.txt
```

---

## 🎯 基本コマンド

### 1. プレビューで確認（おすすめ！）

実際にファイルを移動せず、どう整理されるか確認できます。

**Windows:**
```bash
python organizer.py --dry-run
```

**Mac/Linux:**
```bash
python3 organizer.py --dry-run
```

---

### 2. 実際に整理する

**Windows:**
```bash
python organizer.py
```

**Mac/Linux:**
```bash
python3 organizer.py
```

---

## 🛠️ 便利なオプション

### カスタムパスを指定

デスクトップ以外のフォルダを整理したい場合：

**Windows:**
```bash
python organizer.py --desktop "C:\Users\YourName\Documents"
```

**Mac/Linux:**
```bash
python3 organizer.py --desktop ~/Documents
```

---

### 詳細なログを表示

何が起きているか詳しく知りたい場合：

**Windows:**
```bash
python organizer.py -v
```

**Mac/Linux:**
```bash
python3 organizer.py -v
```

---

### プレビュー + 詳細ログ

組み合わせて使うこともできます：

**Windows:**
```bash
python organizer.py --dry-run -v
```

**Mac/Linux:**
```bash
python3 organizer.py --dry-run -v
```

---

## 📋 実行例

### 例1: 初めて使う場合

```bash
# ステップ1: プレビューで確認
python organizer.py --dry-run

# ステップ2: 問題なければ実行
python organizer.py
```

### 例2: ダウンロードフォルダを整理

```bash
# Windowsの場合
python organizer.py --desktop "C:\Users\YourName\Downloads"

# Macの場合
python3 organizer.py --desktop ~/Downloads
```

---

## ⚡ トラブルシューティング

### エラー: `python: command not found`

**解決策:**
- Windowsの場合: `python` を `py` に変更してみる
- Mac/Linuxの場合: `python` を `python3` に変更してみる

### エラー: `デスクトップディレクトリが見つかりません`

**解決策:**
```bash
# パスを直接指定する
python organizer.py --desktop /path/to/your/desktop
```

### エラー: `No module named 'yaml'`

**解決策:**
```bash
# 必要なパッケージを再インストール
pip install -r requirements.txt
```

---

## 💡 ヒント

1. **最初は必ず `--dry-run` で確認**
   - ファイルを実際に移動する前に、どう整理されるか確認しましょう

2. **定期的に実行**
   - 週に1回実行すると、デスクトップがいつもきれいに保てます

3. **重要なファイルはバックアップ**
   - 念のため、重要なファイルは別の場所にもコピーしておきましょう

---

## 🎉 これだけ覚えればOK！

```bash
# プレビュー
python organizer.py --dry-run

# 実行
python organizer.py
```

たった2つのコマンドです！

---

詳しくは [GUIDE_JA.md](./GUIDE_JA.md) をご覧ください。
