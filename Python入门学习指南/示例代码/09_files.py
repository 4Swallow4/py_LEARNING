"""09 文件读写。路径相对本脚本定位，不依赖终端当前目录。"""

from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parent.parent
SAMPLE = ROOT / "数据样例"
OUT = ROOT / "练习场"


def file_operations():
    notes = SAMPLE / "notes.txt"
    text = notes.read_text(encoding="utf-8")
    print("=== notes.txt ===")
    print(text)

    copy = OUT / "notes_copy.txt"
    copy.write_text(text + "\n# copied by 09_files.py\n", encoding="utf-8")
    print("已复制到", copy)

    csv_path = SAMPLE / "sample_scores.csv"
    print("=== CSV 前 3 行 ===")
    with csv_path.open(encoding="utf-8", newline="") as f:
        for i, row in enumerate(csv.DictReader(f)):
            print(row)
            if i >= 2:
                break

    todo_path = SAMPLE / "todo.json"
    todos = json.loads(todo_path.read_text(encoding="utf-8"))
    print("=== 未完成待办 ===")
    for item in todos:
        if not item["done"]:
            print("-", item["text"])

 # 只有直接运行本文件时才会走进 file_operations();
 #  __main__是 py 内置名，表示当前运行文件；如果被 import 进别的文件，则不会走进 if 语句块
if __name__ == "__main__":
    file_operations()
