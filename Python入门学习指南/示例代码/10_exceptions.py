"""10 异常处理。"""


def parse_score(text):
    try:
        score = float(text)
    except ValueError as exc:
        raise ValueError(f"无法把 {text!r} 当成分数") from exc
    if score < 0 or score > 100:
        raise ValueError("分数要在 0 到 100 之间")
    return score


samples = ["92", "十二", "-1", "101", "80.5"]
for raw in samples:
    try:
        print(raw, "→", parse_score(raw))
    except ValueError as exc:
        print(raw, "失败:", exc)

print("--- 读不存在的文件 ---")
from pathlib import Path

missing = Path(__file__).resolve().parent / "no_such_file.txt"
try:
    missing.read_text(encoding="utf-8")
except FileNotFoundError:
    print("找不到", missing.name, "，检查路径或先创建文件。")
