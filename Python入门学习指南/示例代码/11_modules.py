"""11 模块：import + 脚本入口。"""

import math
from pathlib import Path
from collections import Counter

print("pi 约", round(math.pi, 4))
print("sqrt(16) =", math.sqrt(16))

here = Path(__file__).resolve()
print("当前文件:", here.name)
print("上一级:", here.parent.name)

words = ["py", "code", "py", "list", "py"]
print("计数:", Counter(words))


def main():
    print("只有直接运行本文件时才会走进 main()")


if __name__ == "__main__":
    main()
