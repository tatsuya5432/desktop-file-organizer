# 使用例 📚

実際の使用例を画面の出力付きで紹介します。

## 例1: 散らかったデスクトップを整理

### 整理前のデスクトップ

```
Desktop/
├── メモ1.txt
├── メモ2.txt
├── TODO.md
├── 日記.txt
├── アイデア.txt
├── 写真1.jpg
├── スクリーンショット.png
├── レポート.pdf
├── 資料.docx
├── 音楽.mp3
└── 動画.mp4
```

テキストファイルがバラバラに散らかっていて見づらい状態です...

### ステップ1: プレビューで確認

まず、`--dry-run` オプションでどう整理されるか確認します：

```bash
python organizer.py --dry-run
```

### 出力結果

```
デスクトップファイルを整理しています...
対象ディレクトリ: /Users/yourname/Desktop

==================================================
ファイル整理の結果
==================================================
合計ファイル数: 11

【TextNotes】 5 ファイル
  メモ1.txt → /Users/yourname/Desktop/TextNotes/メモ1.txt
  メモ2.txt → /Users/yourname/Desktop/TextNotes/メモ2.txt
  TODO.md → /Users/yourname/Desktop/TextNotes/TODO.md
  日記.txt → /Users/yourname/Desktop/TextNotes/日記.txt
  アイデア.txt → /Users/yourname/Desktop/TextNotes/アイデア.txt

【Images】 2 ファイル
  写真1.jpg → /Users/yourname/Desktop/Images/写真1.jpg
  スクリーンショット.png → /Users/yourname/Desktop/Images/スクリーンショット.png

【Documents】 2 ファイル
  レポート.pdf → /Users/yourname/Desktop/Documents/レポート.pdf
  資料.docx → /Users/yourname/Desktop/Documents/資料.docx

【Audio】 1 ファイル
  音楽.mp3 → /Users/yourname/Desktop/Audio/音楽.mp3

【Videos】 1 ファイル
  動画.mp4 → /Users/yourname/Desktop/Videos/動画.mp4

==================================================
※ プレビューモード: ファイルは実際には移動していません
  実際に移動するには --dry-run オプションを外して実行してください
```

✅ **確認ポイント:**
- テキストファイル5個が `TextNotes` フォルダに整理される
- 画像、ドキュメント、音楽、動画もそれぞれのフォルダに分類される
- 問題なさそう！

### ステップ2: 実際に整理

問題なければ、実際に整理します：

```bash
python organizer.py
```

### 出力結果

```
デスクトップファイルを整理しています...
対象ディレクトリ: /Users/yourname/Desktop

==================================================
ファイル整理の結果
==================================================
合計ファイル数: 11

【TextNotes】 5 ファイル
  ✓ メモ1.txt
  ✓ メモ2.txt
  ✓ TODO.md
  ✓ 日記.txt
  ✓ アイデア.txt

【Images】 2 ファイル
  ✓ 写真1.jpg
  ✓ スクリーンショット.png

【Documents】 2 ファイル
  ✓ レポート.pdf
  ✓ 資料.docx

【Audio】 1 ファイル
  ✓ 音楽.mp3

【Videos】 1 ファイル
  ✓ 動画.mp4

==================================================

✓ 整理が完了しました！
```

### 整理後のデスクトップ

```
Desktop/
├── TextNotes/
│   ├── メモ1.txt
│   ├── メモ2.txt
│   ├── TODO.md
│   ├── 日記.txt
│   └── アイデア.txt
├── Images/
│   ├── 写真1.jpg
│   └── スクリーンショット.png
├── Documents/
│   ├── レポート.pdf
│   └── 資料.docx
├── Audio/
│   └── 音楽.mp3
└── Videos/
    └── 動画.mp4
```

**🎉 すっきり整理されました！テキストメモがすべて `TextNotes` フォルダにまとまっています！**

---

## 例2: ダウンロードフォルダを整理

ダウンロードフォルダも同じように整理できます。

```bash
# Windowsの場合
python organizer.py --desktop "C:\Users\yourname\Downloads" --dry-run

# Macの場合
python3 organizer.py --desktop ~/Downloads --dry-run
```

---

## 例3: 同名ファイルがある場合

すでに `TextNotes` フォルダに `メモ1.txt` がある状態で、デスクトップにも `メモ1.txt` がある場合：

```
デスクトップファイルを整理しています...
対象ディレクトリ: /Users/yourname/Desktop

==================================================
ファイル整理の結果
==================================================
合計ファイル数: 1

【TextNotes】 1 ファイル
  ✓ メモ1.txt → メモ1_1.txt （同名ファイルがあるため自動リネーム）

==================================================

✓ 整理が完了しました！
```

**同名ファイルは自動的に番号が付けられるので、上書きされることはありません！**

---

## 例4: 詳細ログを表示

何が起きているか詳しく知りたい場合は `-v` オプションを使います：

```bash
python organizer.py -v
```

より詳しい情報が表示されます。

---

## 💡 実用的な使い方

### 毎週日曜日の習慣にする

```bash
# 週に1回実行するだけ
python organizer.py --dry-run  # 確認
python organizer.py            # 実行
```

### 作業前後に整理

```bash
# 作業開始前
python organizer.py

# → すっきりした状態で作業開始！

# 作業終了後
python organizer.py

# → また散らかったファイルを整理！
```

---

## 🎯 まとめ

1. **必ず `--dry-run` で確認してから実行**
2. **テキストメモは `TextNotes` フォルダに自動整理**
3. **同名ファイルは自動リネームで安心**
4. **定期的に実行してデスクトップをきれいに保つ**

これで、もうデスクトップが散らかることはありません！ 🎉
