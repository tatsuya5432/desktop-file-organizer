#!/usr/bin/env python3
"""
Downloads Organizer - ダウンロードフォルダ整理ツール

ダウンロードフォルダ内のファイルを自動的に整理します。
"""
import argparse
import sys
from pathlib import Path
from file_organizer import FileOrganizer


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description='ダウンロードフォルダのファイルを自動的に整理します',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
使用例:
  python downloads_organizer.py                    # ダウンロードフォルダを整理
  python downloads_organizer.py --dry-run          # プレビューのみ（実際には移動しない）
  python downloads_organizer.py --path ~/Downloads # カスタムパスを指定
        '''
    )

    parser.add_argument(
        '--path',
        type=str,
        help='ダウンロードフォルダのパス（デフォルト: ~/Downloads）'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='プレビューモード（実際にはファイルを移動しない）'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='詳細な出力を表示'
    )

    args = parser.parse_args()

    try:
        # FileOrganizerを初期化（downloadsモード）
        organizer = FileOrganizer(
            desktop_path=args.path,
            dry_run=args.dry_run,
            target_folder='downloads'
        )

        print("ダウンロードフォルダのファイルを整理しています...")
        print(f"対象ディレクトリ: {organizer.desktop_path}")
        print()

        # ファイルを整理
        organized_files = organizer.organize()

        # 結果を表示
        summary = organizer.get_summary(organized_files)
        print(summary)

        if not args.dry_run and organized_files:
            print()
            print("✓ 整理が完了しました！")

    except FileNotFoundError as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as e:
        print(f"エラー: ファイルへのアクセス権限がありません: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
