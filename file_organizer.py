"""
ファイルを整理して適切なフォルダに移動するモジュール
"""
import os
import shutil
from pathlib import Path
from typing import List, Dict, Tuple
from file_scanner import FileScanner
from file_classifier import FileClassifier


class FileOrganizer:
    """ファイルを整理するクラス"""

    def __init__(self, desktop_path: str = None, dry_run: bool = False):
        """
        Args:
            desktop_path: デスクトップのパス
            dry_run: True の場合、実際には移動しない（プレビューのみ）
        """
        self.scanner = FileScanner(desktop_path)
        self.classifier = FileClassifier()
        self.desktop_path = self.scanner.desktop_path
        self.dry_run = dry_run
        self.organized_folders = set()

    def organize(self) -> Dict[str, List[Tuple[Path, Path]]]:
        """
        ファイルを整理する

        Returns:
            カテゴリごとの移動情報の辞書
            {category: [(元のパス, 移動先のパス), ...]}
        """
        # ファイルをスキャン
        files = self.scanner.scan()

        # カテゴリごとにファイルを分類
        organized_files = {}

        for file_path in files:
            category = self.classifier.classify(file_path)

            if category not in organized_files:
                organized_files[category] = []

            # 移動先のパスを決定
            dest_dir = self.desktop_path / category
            dest_path = dest_dir / file_path.name

            # 同名ファイルが存在する場合の処理
            dest_path = self._get_unique_path(dest_path)

            organized_files[category].append((file_path, dest_path))

        # ファイルを実際に移動（dry_runでない場合）
        if not self.dry_run:
            for category, file_list in organized_files.items():
                self._move_files(category, file_list)

        return organized_files

    def _get_unique_path(self, path: Path) -> Path:
        """
        同名ファイルが存在する場合、ユニークなパスを生成

        Args:
            path: 元のパス

        Returns:
            ユニークなパス
        """
        if not path.exists():
            return path

        # ファイル名に番号を追加
        counter = 1
        stem = path.stem
        suffix = path.suffix
        parent = path.parent

        while True:
            new_name = f"{stem}_{counter}{suffix}"
            new_path = parent / new_name
            if not new_path.exists():
                return new_path
            counter += 1

    def _move_files(self, category: str, file_list: List[Tuple[Path, Path]]):
        """
        ファイルを移動

        Args:
            category: カテゴリ名
            file_list: 移動するファイルのリスト
        """
        if not file_list:
            return

        # カテゴリディレクトリを作成
        dest_dir = self.desktop_path / category
        dest_dir.mkdir(exist_ok=True)
        self.organized_folders.add(category)

        # ファイルを移動
        for src_path, dest_path in file_list:
            try:
                shutil.move(str(src_path), str(dest_path))
            except Exception as e:
                print(f"エラー: {src_path} を {dest_path} に移動できませんでした: {e}")

    def get_summary(self, organized_files: Dict[str, List[Tuple[Path, Path]]]) -> str:
        """
        整理結果のサマリーを取得

        Args:
            organized_files: 整理されたファイルの辞書

        Returns:
            サマリーの文字列
        """
        total_files = sum(len(files) for files in organized_files.values())

        summary = []
        summary.append("=" * 50)
        summary.append("ファイル整理の結果")
        summary.append("=" * 50)
        summary.append(f"合計ファイル数: {total_files}")
        summary.append("")

        for category, file_list in sorted(organized_files.items()):
            if file_list:
                summary.append(f"【{category}】 {len(file_list)} ファイル")
                for src_path, dest_path in file_list:
                    if self.dry_run:
                        summary.append(f"  {src_path.name} → {dest_path}")
                    else:
                        summary.append(f"  ✓ {src_path.name}")

        summary.append("")
        summary.append("=" * 50)

        if self.dry_run:
            summary.append("※ プレビューモード: ファイルは実際には移動していません")
            summary.append("  実際に移動するには --dry-run オプションを外して実行してください")

        return "\n".join(summary)
