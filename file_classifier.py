"""
ファイルをタイプごとに分類するモジュール
"""
from pathlib import Path
from typing import Dict, Set


class FileClassifier:
    """ファイルを拡張子に基づいて分類するクラス"""

    # ファイルタイプごとの拡張子マッピング
    FILE_CATEGORIES = {
        'Images': {
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico',
            '.webp', '.tiff', '.tif', '.raw', '.heic', '.heif'
        },
        'Documents': {
            '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt',
            '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.odp'
        },
        'TextNotes': {
            '.txt', '.md', '.markdown', '.note', '.log'
        },
        'Videos': {
            '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv',
            '.webm', '.m4v', '.mpg', '.mpeg', '.3gp'
        },
        'Audio': {
            '.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma',
            '.m4a', '.opus', '.aiff'
        },
        'Archives': {
            '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2',
            '.xz', '.tar.gz', '.tar.bz2', '.tgz'
        },
        'Code': {
            '.py', '.js', '.java', '.cpp', '.c', '.h', '.cs',
            '.php', '.rb', '.go', '.rs', '.swift', '.kt',
            '.html', '.css', '.scss', '.sass', '.json', '.xml',
            '.yaml', '.yml', '.sql', '.sh', '.bash'
        },
        'Executables': {
            '.exe', '.msi', '.dmg', '.app', '.deb', '.rpm', '.apk'
        }
    }

    def __init__(self, custom_categories: Dict[str, Set[str]] = None):
        """
        Args:
            custom_categories: カスタムカテゴリの辞書
        """
        self.categories = self.FILE_CATEGORIES.copy()

        if custom_categories:
            self.categories.update(custom_categories)

    def classify(self, file_path: Path) -> str:
        """
        ファイルを分類してカテゴリ名を返す

        Args:
            file_path: ファイルパス

        Returns:
            カテゴリ名（該当なしの場合は 'Others'）
        """
        extension = file_path.suffix.lower()

        # .tar.gz などの複合拡張子に対応
        if file_path.name.endswith('.tar.gz'):
            extension = '.tar.gz'
        elif file_path.name.endswith('.tar.bz2'):
            extension = '.tar.bz2'

        # 各カテゴリをチェック
        for category, extensions in self.categories.items():
            if extension in extensions:
                # TextNotesは優先度高く扱う（.txtがDocumentsとTextNotesで重複）
                if category == 'TextNotes':
                    return category
                # Documentsより先にTextNotesが見つかった場合はそちらを優先
                if extension in self.categories.get('TextNotes', set()):
                    continue
                return category

        return 'Others'

    def get_categories(self) -> list:
        """
        利用可能なカテゴリのリストを取得

        Returns:
            カテゴリ名のリスト
        """
        return list(self.categories.keys()) + ['Others']

    def add_custom_rule(self, category: str, extensions: Set[str]):
        """
        カスタム分類ルールを追加

        Args:
            category: カテゴリ名
            extensions: 拡張子のセット
        """
        if category in self.categories:
            self.categories[category].update(extensions)
        else:
            self.categories[category] = extensions
