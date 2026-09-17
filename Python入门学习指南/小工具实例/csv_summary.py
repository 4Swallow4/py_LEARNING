"""读取成绩 CSV，按人汇总平均分。

示例：
    py -3 csv_summary.py
    py -3 csv_summary.py --csv ..\\数据样例\\sample_scores.csv
"""

from __future__ import annotations

import argparse
import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = ROOT / "数据样例" / "sample_scores.csv"


def load_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"找不到 CSV：{path}")
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def summarize(rows: list[dict[str, str]], min_score: float) -> None:
    by_name: dict[str, list[float]] = defaultdict(list)
    weak: list[tuple[str, str, float]] = []

    for row in rows:
        try:
            name = row["姓名"]
            subject = row["科目"]
            score = float(row["分数"])
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"行格式不对：{row}") from exc
        by_name[name].append(score)
        if score < min_score:
            weak.append((name, subject, score))

    print(f"{'姓名':<8}{'次数':>6}{'平均':>10}{'最低':>8}{'最高':>8}")
    print("-" * 40)
    for name in sorted(by_name):
        scores = by_name[name]
        print(
            f"{name:<8}{len(scores):>6}"
            f"{statistics.mean(scores):>10.1f}"
            f"{min(scores):>8.0f}{max(scores):>8.0f}"
        )

    print()
    if not weak:
        print(f"没有低于 {min_score:.0f} 分的记录。")
        return
    print(f"低于 {min_score:.0f} 分：")
    for name, subject, score in weak:
        print(f"  {name} {subject} {score:.0f}")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="汇总成绩 CSV")
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="CSV 路径")
    parser.add_argument("--min-score", type=float, default=60, help="及格线，默认 60")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        rows = load_rows(args.csv)
        if not rows:
            raise ValueError("CSV 是空的")
        summarize(rows, args.min_score)
    except (OSError, ValueError) as exc:
        print("错误:", exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
