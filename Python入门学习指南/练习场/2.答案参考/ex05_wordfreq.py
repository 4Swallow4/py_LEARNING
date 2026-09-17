"""题 5 参考答案：词频统计小工具。"""

from __future__ import annotations

import argparse
import string
from collections import Counter
from pathlib import Path

DEFAULT = Path(__file__).resolve().parent.parent.parent / "数据样例" / "notes.txt"


def tokenize(text: str) -> list[str]:
    table = str.maketrans({ch: " " for ch in string.punctuation + "，。：；！？、"})
    cleaned = text.lower().translate(table)
    return [w for w in cleaned.split() if len(w) > 1]


def main() -> None:
    parser = argparse.ArgumentParser(description="统计文本词频 top 10")
    parser.add_argument("--file", type=Path, default=DEFAULT)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()
    if not args.file.exists():
        raise SystemExit(f"找不到文件：{args.file}")
    words = tokenize(args.file.read_text(encoding="utf-8"))
    print(f"来自 {args.file.name}，单词数 {len(words)}")
    for word, n in Counter(words).most_common(args.top):
        print(f"{n:4}  {word}")


if __name__ == "__main__":
    main()
