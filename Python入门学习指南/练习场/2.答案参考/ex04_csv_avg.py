"""题 4 参考答案：读 CSV 求每人平均。"""

import csv
from collections import defaultdict
from pathlib import Path

csv_path = Path(__file__).resolve().parent.parent.parent / "数据样例" / "sample_scores.csv"
by_name = defaultdict(list)

with csv_path.open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        by_name[row["姓名"]].append(float(row["分数"]))

for name in sorted(by_name):
    scores = by_name[name]
    avg = sum(scores) / len(scores)
    print(f"{name} {avg:.1f}")
