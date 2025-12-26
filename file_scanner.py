"""
デスクトップファイルをスキャンするモジュール
"""
import os
from pathlib import Path
from typing import List, Dict


class FileScanner:
    """デスクトップのファイルをスキャンするクラス"""

    def __init__(self, desktop_path: str = None):
        """
        Args:
            desktop_path: デスクトップのパス。Noneの場合は自動検出
        """
        if desktop_path:
            self.desktop_path = Path(desktop_path)
        else:
            self.desktop_path = self._get_desktop_path()

    def _get_desktop_path(self) -> Path:
        """デスクトップのパスを取得"""
        home = Path.home()
        desktop = home / "Desktop"

        # Linuxの場合、デスクトップが存在しない場合は別のロケーションを試す
        if not desktop.exists():
            desktop = home / "デスクトップ"

        if not desktop.exists():
            raise FileNotFoundError("デスクトップディレクトリが見つかりません")

        return desktop

    def scan(self, exclude_dirs: List[str] = None) -> List[Path]:
        """
        デスクトップのファイルをスキャン

        Args:
            exclude_dirs: 除外するディレクトリ名のリスト

        Returns:
            ファイルパスのリスト
        """
        if exclude_dirs is None:
            exclude_dirs = []

        files = []

        for item in self.desktop_path.iterdir():
            # ディレクトリは除外（整理済みフォルダなど）
            if item.is_dir():
                continue

            # 隠しファイルは除外
            if item.name.startswith('.'):
                continue

            files.append(item)

        return files

    def get_file_info(self, file_path: Path) -> Dict:
        """
        ファイルの情報を取得

        Args:
            file_path: ファイルパス

        Returns:
            ファイル情報の辞書
        """
        stat = file_path.stat()

        return {
            'name': file_path.name,
            'path': file_path,
            'size': stat.st_size,
            'extension': file_path.suffix.lower(),
            'modified_time': stat.st_mtime
        }
