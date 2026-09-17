"""统计一个目录里各种后缀的文件数量。

默认只扫描本学习文件夹。

示例：
    py -3 file_counter.py
    py -3 file_counter.py --path .
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent.parent


def count_suffixes(root: Path) -> Counter[str]:
    if not root.exists():
        raise FileNotFoundError(f"路径不存在：{root}")
    if not root.is_dir():
        raise NotADirectoryError(f"不是文件夹：{root}")

    counter: Counter[str] = Counter()
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        suffix = path.suffix.lower() or "(无后缀)"
        counter[suffix] += 1
    return counter


def print_report(root: Path, counter: Counter[str]) -> None:
    print(f"目录: {root}")
    print(f"文件总数: {sum(counter.values())}")
    print()
    print(f"{'后缀':<12}{'数量':>8}")
    print("-" * 20)
    for suffix, n in counter.most_common():
        print(f"{suffix:<12}{n:>8}")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="按后缀统计文件数量")
    parser.add_argument(
        "--path",
        type=Path,
        default=DEFAULT_PATH,
        help="要扫描的文件夹，默认是本学习资料根目录",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.path.expanduser().resolve()
    try:
        counter = count_suffixes(root)
    except OSError as exc:
        print("错误:", exc, file=sys.stderr)
        return 1
    print_report(root, counter)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
