"""12 标准库小拼盘：和后面的小工具同一套积木。"""

from collections import Counter
from datetime import datetime
from pathlib import Path
import random
import statistics
import string

ROOT = Path(__file__).resolve().parent.parent

print("现在:", datetime.now().strftime("%Y-%m-%d %H:%M"))

scores = [92, 85, 76, 88, 61]
print("平均", statistics.mean(scores), "中位数", statistics.median(scores))

alphabet = string.ascii_letters + string.digits
print("随机 8 位:", "".join(random.choice(alphabet) for _ in range(8)))

text = (ROOT / "数据样例" / "notes.txt").read_text(encoding="utf-8")
words = [w for w in text.replace("：", " ").split() if w]
print("词频 top3:", Counter(words).most_common(3))

py_files = list((ROOT / "示例代码").glob("*.py"))
print("示例脚本数量:", len(py_files))
