# Python 入门学习指南（可继续编辑）

> 配套文件夹：桌面 `Python入门学习指南`  
> 适用程度：已经会 `print`、变量、`if/else`、字典和一点点 NumPy  
> 运行方式：`py -3 文件名.py`（本机默认 Python 3.14）  
> 配套代码：全部在 `示例代码/`，小工具在 `小工具实例/`

读法：**一章正文 → 跑同编号脚本 → 自己改一行再跑 → 做练习场对应题**。  
不要只看不敲。Python 是靠手记住的。

---

## 0. 这门语言到底用来干什么

Python 适合把「我脑子里的步骤」写成「电脑能重复执行的步骤」。常见用途：

| 方向 | 入门能做什么 | 再往后 |
| --- | --- | --- |
| 日常自动化 | 批量改文件名、统计文件夹、待办本 | 整理下载目录、定时备份 |
| 文本/表格 | 读 CSV、算平均分、过滤行 | pandas、Excel、报表 |
| 数据/科学计算 | 先把列表和文件搞懂 | NumPy、matplotlib（你已经碰过） |
| 网页/后端 | 先学会函数和文件 | Flask / FastAPI |
| 爬虫 | 先学会字符串和请求思路 | requests + 解析 HTML |
| 小游戏 | 猜数字、命令行冒险 | pygame |
| AI 相关 | **先把基础写稳** | 再碰模型库 |

现在最值钱的能力不是背语法，而是：

1. 把问题拆成输入 → 处理 → 输出。
2. 会查报错，而不是怕报错。
3. 会把重复代码收成函数，再收成小工具。

---

## 1. 环境、怎么运行、怎么看报错

### 1.1 三个常用入口

1. **VS Code**：打开本文件夹，点右上角运行，或终端里输入命令。
2. **终端（推荐养成）**：

```powershell
cd "$env:USERPROFILE\Desktop\Python入门学习指南"
py -3 --version
py -3 .\示例代码\01_hello.py
```

3. **交互模式**（临时试一句，不适合保存作业）：

```powershell
py -3
```

进入后可以输入 `2 + 3`，退出输入 `exit()`。

`python` 和 `py -3` 在你这台电脑上可能指向不同版本。本资料统一用 **`py -3`**。

### 1.2 脚本是什么

一个 `.py` 文件从上到下执行。注释用 `#`。三引号 `"""..."""` 常用来写较长说明。

```python
# 这是注释，电脑不执行
print("Hello, python")  # 你已经写过类似的
```

运行：`示例代码/01_hello.py`。

### 1.3 报错怎么读（比再看十页语法重要）

出错时从**最后几行**看：

```text
File "...\05_dicts.py", line 12, in <module>
    print(person["agee"])
KeyError: 'agee'
```

读法：

- `File`：哪个文件
- `line 12`：第几行
- 最后一行类型：`KeyError` / `NameError` / `SyntaxError` / `TypeError` ...
- 冒号后面是原因

常见对应关系：

| 报错 | 通常原因 | 先检查 |
| --- | --- | --- |
| `SyntaxError` | 括号、冒号、引号没配对 | 上一行是不是少了 `:` |
| `IndentationError` | 空格缩进乱了 | 同一层要对齐，推荐 4 空格 |
| `NameError` | 变量名写错或还没赋值 | 拼写、大小写 |
| `TypeError` | 类型不能这么用，比如 `"1" + 2` | 要不要 `int()` / `str()` |
| `KeyError` | 字典没有这个键 | `.get()` 或先 `in` 判断 |
| `IndexError` | 列表下标越界 | `len(xs)`，下标从 0 开始 |
| `FileNotFoundError` | 路径不对 | 当前工作目录、相对路径 |

配套：`示例代码/10_exceptions.py`。

---

## 2. 变量、类型、赋值（接你的 `1.py`）

你写过：

```python
p = pp = 4
app = 2
print(p, app)
```

这已经对了。补上「名字后面到底装着什么」。

### 2.1 值都有类型

```python
n = 4          # int 整数
x = 3.14       # float 小数
s = "python"   # str 字符串
ok = True      # bool 布尔，只能 True / False
empty = None   # 表示「没有值」
```

查看类型：`type(n)`。转换：

```python
int("12")      # 12
float("3.5")   # 3.5
str(12)        # "12"
bool(0)        # False，0、""、[]、{}、None 都算假
```

用户输入永远是字符串：

```python
age = int(input("年龄："))
```

`input()` 拿到的是 `"18"` 不是 `18`。要算数必须先 `int()` / `float()`。空回车会让 `int("")` 炸掉，后面第 10 章用 `try` 接住。

### 2.2 名字规则

- 只能用字母、数字、下划线，不能数字开头。
- 区分大小写：`App` 和 `app` 是两个名字。
- 不要用 `list`、`dict`、`str`、`print` 当变量名。
- 名字要说明含义：`score` 比 `p` 好。练习阶段用 `p` 没问题，小工具里不要这样。

### 2.3 先看再改

运行 `示例代码/02_types.py`。改一个变量再跑，观察输出变化。

---

## 3. 字符串：文本处理的基本功

几乎所有小工具都在处理文字：文件名、CSV 单元格、用户输入。

```python
name = "Tomo"
print(f"Hello, {name}")     # f-string，优先用这个
print("py" + "thon")        # 拼接
print("ha" * 3)             # hahaha
print(len("python"))        # 6
print("python"[0])          # p，下标从 0
print("python"[0:2])        # py，切片：含头不含尾
print("Python".lower())
print("a,b,c".split(","))   # ['a', 'b', 'c']
print("".join(["a", "b"]))  # ab
print("  hi  ".strip())     # 去掉两端空白
print("hello".replace("l", "L"))
```

判断：

```python
"py" in "python"          # True
"python".startswith("py")
"file.py".endswith(".py")
```

多行文本用三引号。路径在 Windows 上建议：

```python
from pathlib import Path
p = Path.home() / "Desktop" / "Python入门学习指南"
```

先别死记所有方法。记住：**字符串方法不改原字符串，而是返回新字符串**。

```python
s = "abc"
s.upper()
print(s)        # 还是 abc
s = s.upper()
print(s)        # ABC
```

运行：`示例代码/03_strings.py`。

---

## 4. 列表、元组、集合

字典你已经会了。列表是「按顺序排的一串东西」，小工具里比字典更常用。

### 4.1 列表 list

```python
nums = [92, 85, 76]
nums.append(88)       # 末尾加
nums.insert(0, 100)   # 指定位置插
last = nums.pop()     # 拿出最后一个
nums.remove(85)       # 按值删第一次出现
print(nums[0], nums[-1])  # 第一和最后
print(nums[1:3])      # 切片
print(len(nums))
print(sum(nums), max(nums), min(nums))
print(sorted(nums))   # 返回新列表，不改原来的
nums.sort()           # 原地排序
```

列表可以嵌套：`[[1, 2], [3, 4]]`，这就是你用 NumPy 之前看到的「二维」雏形。

**可变**：`nums[0] = 1` 可以改。后面函数章节会提到：把列表传进函数，函数里 `append` 会影响外面。

### 4.2 元组 tuple

```python
point = (3, 4)
x, y = point          # 拆包
```

元组一般不改。函数返回多个值时常常是元组：`return avg, total`。

### 4.3 集合 set

```python
seen = {"a", "b", "a"}
print(seen)           # {'a', 'b'} 去重
print("a" in seen)    # 很快
```

适合去重、成员判断。没有顺序，没有下标。

运行：`示例代码/04_lists.py`。

---

## 5. 字典再往下挖（接你的 `字典.py`）

你已经写过：

```python
thisdict = {"brand": "UNIKO", "model": "she", "year": "2026"}
x = thisdict.get("model")
```

`.get()` 用得很对：键不存在时默认返回 `None`，不会 `KeyError`。

继续常用操作：

```python
person = {"name": "Alice", "score": 92}

person["city"] = "Shanghai"     # 新增或覆盖
print(person.get("age"))        # None
print(person.get("age", 0))     # 缺省值 0
print("name" in person)         # True，查的是键

for key, value in person.items():
    print(key, value)

print(list(person.keys()))
print(list(person.values()))
```

嵌套（小工具里超常见）：

```python
students = {
    "Alice": {"math": 92, "eng": 85},
    "Bob": {"math": 76, "eng": 88},
}
print(students["Alice"]["math"])
```

JSON 文件读进来通常就是「列表套字典」或「字典套字典」。待办小工具就是这样存的。

运行：`示例代码/05_dicts.py`。

---

## 6. 判断与布尔（接你的 if/else）

你写过：

```python
if p > app:
    print("Oh,fucking great")
else:
    print("Oh,fucking bad")
```

结构完全正确。补充分支和组合条件。

```python
score = 88

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"
```

比较：`== != < > <= >=`。  
组合：`and`（同时）、`or`（其一）、`not`（取反）。

```python
if score >= 60 and score < 90:
    print("及格但不是优秀")
```

成员：

```python
if "py" in filename and filename.endswith(".py"):
    print("这是 python 文件")
```

注意：

- 相等是 `==`，一个 `=` 是赋值。
- `is` 用来比是不是同一个对象，新手比数字/字符串请用 `==`。
- 空列表 `[]`、空字符串 `""`、`0`、`None` 在 `if` 里都是假。

运行：`示例代码/06_if.py`。

---

## 7. 循环：让程序重复干活

没有循环，小工具做不成。

### 7.1 for：已知一串东西

```python
for n in [1, 2, 3]:
    print(n)

for i in range(3):        # 0, 1, 2
    print(i)

for i, name in enumerate(["a", "b"]):
    print(i, name)        # 同时要下标和值
```

### 7.2 while：不知道要转几次

```python
n = 3
while n > 0:
    print(n)
    n -= 1
```

必须有机会让条件变假，否则死循环。终端里 `Ctrl+C` 可打断。

### 7.3 break / continue

```python
for n in range(10):
    if n == 3:
        continue   # 跳过这次
    if n == 7:
        break      # 离开循环
    print(n)
```

### 7.4 列表推导（尝鲜即可）

```python
squares = [n * n for n in range(5) if n % 2 == 0]
# [0, 4, 16]
```

先会普通 `for`，再写这种浓缩写法。

运行：`示例代码/07_loops.py`。

---

## 8. 函数：把「会做的一件事」打包

看到同一段逻辑写了两次，就该收成函数。

```python
def average(nums):
    """返回非空数字列表的平均值。"""
    if not nums:
        return 0.0
    return sum(nums) / len(nums)

print(average([90, 80, 70]))
```

要点：

- `def` 定义，`return` 交回结果。没有 `return` 时函数返回 `None`。
- 参数是输入，返回值是输出。`print` 只是显示，不是返回。
- 默认参数：`def greet(name, prefix="Hi")`
- 类型注解可选，给人看的：`def add(a: int, b: int) -> int:`

参数传递：

- 数字、字符串传入后在函数里重新赋值，**外面的变量不变**。
- 列表、字典传入后，如果函数里 `append` / 改键，**外面会被改到**。

```python
def add_one(xs):
    xs.append(1)

data = [0]
add_one(data)
print(data)   # [0, 1]
```

想避免误伤，函数里先 `xs = list(xs)` 复制一份。

运行：`示例代码/08_functions.py`。

---

## 9. 文件读写：程序开始「记住」东西

脚本关掉变量就没了。要留下结果，写文件。

优先用 `pathlib` + `encoding="utf-8"`，避免 Windows 中文乱码。

```python
from pathlib import Path

root = Path(__file__).resolve().parent.parent
notes = root / "数据样例" / "notes.txt"

text = notes.read_text(encoding="utf-8")
print(text)

out = root / "练习场" / "notes_copy.txt"
out.write_text(text + "\n# copied\n", encoding="utf-8")
```

`Path(__file__)` 是「当前这个 `.py` 文件自己的位置」。  
相对路径不靠终端当时在哪个目录，小工具更稳。

CSV（逗号分隔表）：

```python
import csv

with open(path, encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row["姓名"], row["分数"])
```

JSON（嵌套数据）：

```python
import json
data = json.loads(path.read_text(encoding="utf-8"))
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
```

`ensure_ascii=False` 才能把中文原样写进去。

运行：`示例代码/09_files.py`。

---

## 10. 异常：失败时别直接崩溃

真实小工具会遇到：用户乱输入、文件不存在、CSV 缺列。

```python
try:
    n = int("十二")
except ValueError:
    print("不是合法整数")
```

原则：

- 只抓你知道怎么处理的错误。
- 不要空的 `except:` 把所有问题吞掉。
- 需要收尾（关文件）时用 `with`，它已经能自动关闭。
- 自己的函数遇到不可能继续的情况，可以 `raise ValueError("分数不能为负")`。

```python
def parse_score(text):
    try:
        score = float(text)
    except ValueError as exc:
        raise ValueError(f"无法把 {text!r} 当成分数") from exc
    if score < 0 or score > 100:
        raise ValueError("分数要在 0 到 100")
    return score
```

运行：`示例代码/10_exceptions.py`。

---

## 11. 模块、包、标准库

「模块」= 一个 `.py` 文件里的可复用代码。  
「标准库」= 安装 Python 时就已经有的模块，做小工具先榨干它，再谈第三方。

```python
import math
from pathlib import Path
from collections import Counter
```

自己的文件也可以被 import，但入门阶段用「直接运行脚本」就够。  
脚本底部常见写法：

```python
def main():
    print("从这里开始")

if __name__ == "__main__":
    main()
```

含义：这个文件被别人 `import` 时不要自动跑 `main()`，只有直接运行时才跑。四个小工具都用了这个结构。

第三方库（以后）：

```powershell
py -3 -m pip install numpy
```

你练习里的 `import numpy as np` 属于这一层。入门没装成功也不挡路：标准库足够做本文件夹所有工具。

运行：`示例代码/11_modules.py`。

---

## 12. 标准库速查（做小工具会反复用）

先混个脸熟，用到再查。

| 模块 | 干什么 |
| --- | --- |
| `pathlib` | 路径、列目录、读写文本 |
| `csv` | 表格 |
| `json` | 结构化存储 |
| `argparse` | 命令行参数：`--length 16` |
| `random` | 随机密码、抽样 |
| `datetime` | 日期时间 |
| `collections.Counter` | 计数 |
| `statistics` | 平均、中位数 |
| `textwrap` | 折行 |
| `sys` | `sys.argv`，退出码 |
| `re` | 正则，入门后期再上 |

更完整的演示：`示例代码/12_stdlib.py`。

---

## 13. 从「会语法」到「做出一个小工具」

任何小工具都按同一张草图：

```
用户怎么启动？     py -3 todo.py add 买牛奶
需要哪些输入？     命令、参数、文件
核心处理是什么？   读 JSON → 改列表 → 写回去
输出给人看什么？   打印一行结果，失败时说明原因
坏输入怎么办？     argparse + try/except
```

入门质量标准（够用就行）：

1. 能直接运行，不靠你手工改代码里的数字。
2. 路径用 `__file__` 定位，换目录也能跑。
3. 中文用 UTF-8。
4. 失败时有人话，而不是一堆英文 traceback 甩脸上（学习阶段保留 traceback 也行）。
5. `main()` 里组织流程，具体步骤拆成函数。

对照阅读：

- [`小工具制作指导.md`](./小工具制作指导.md)
- `小工具实例/password_generator.py` 随机 + 命令行
- `小工具实例/csv_summary.py` 读表 + 统计
- `小工具实例/file_counter.py` 扫描文件夹
- `小工具实例/todo.py` 读写 JSON 的完整 CRUD

---

## 14. 调试与良好习惯

1. 用 `print(repr(x))` 看真实内容，能看出隐藏空格和类型。
2. VS Code 在行号左侧点红点，F5 调试，单步看变量。
3. 一次只改一个地方再运行。
4. 函数短一点，名字像句子：`load_todos()`、`save_todos()`。
5. 不要把密码、密钥写进代码。本文件夹的密码生成器只在屏幕上打印。
6. 缩进只用空格，VS Code 右下角看是不是 Indent 4。

---

## 15. 4～8 周学习节奏（可按你速度压缩）

假设每天 45～90 分钟：

| 周 | 内容 | 验收 |
| --- | --- | --- |
| 第 1 周 | 第 1–6 章 + 示例 01–06 | 能解释变量/列表/字典区别，独立写 if |
| 第 2 周 | 第 7–8 章 | 能写带 `return` 的函数，不用复制粘贴同一段 |
| 第 3 周 | 第 9–11 章 | 能读 CSV，能处理错误输入 |
| 第 4 周 | 四个小工具各改一处 | 比如密码工具加 `--count` |
| 第 5–6 周 | 自己做第 5 个工具 | 例如「下载文件夹按后缀分类」 |
| 之后 | 按用途选方向 | 数据 / 自动化 / Web / 游戏 |

NumPy 先放着。等列表、循环、函数不卡以后，再把 `py_LEARNING/练习/2.py` 升级成「对一组分数求均值/标准差」。

---

## 16. 用途方向（学完本包之后怎么选）

### A. 桌面自动化（最快有成就感）

目标：让电脑替你点名、改名、筛选文件。  
下一课关键词：`pathlib`、`shutil`、`datetime`。  
项目：整理 `Downloads`，按后缀移动到子文件夹。

### B. 数据小分析

目标：表格进，统计出。  
下一课关键词：`csv` → 以后 `pandas`。  
项目：把 `数据样例/sample_scores.csv` 做成「每人平均分 + 不及格名单」。

### C. 命令行工具

目标：别人能 `py 工具.py --help` 使用。  
下一课关键词：`argparse`。  
项目：扩展 `todo.py` 增加 `due` 截止日期。

### D. 和网页打交道

目标：本地打开浏览器能用。  
下一课关键词：Flask。  
先决条件：函数 + 字典 + 文件必须熟。

### E. 科学计算 / AI 外围

目标：会用数组，而不是只会 `print(np.array(...))`。  
下一课关键词：NumPy 切片、广播、读 CSV 再转数组。  
先决条件：列表和循环。

---

## 17. 常见坑（对照你现在的代码）

1. **`p = pp = 4` 可以，但两个名字指向同一个不可变整数，没事；如果是列表就会互相影响。**  
   `a = b = []` 然后 `a.append(1)`，`b` 也会变。
2. **`input()` 是字符串。** `"12" > 10` 在 3.x 会 TypeError。
3. **字典键必须恰好相等。** `"2026"` 和 `2026` 不是同一个键。你现在的 `year` 存成了字符串，要比较年份先统一类型。
4. **Windows 控制台编码。** 写文件显式 `encoding="utf-8"`。
5. **脚本里的相对路径。** 终端如果在用户目录，`open("notes.txt")` 会找不到。用 `Path(__file__)`。
6. **NumPy 不是必须。** 一组分数用普通列表就能算平均：`sum(xs)/len(xs)`。

---

## 18. 练习怎么做

打开 [`练习场/练习题.md`](./练习场/练习题.md)。  
自己写的代码放到 `练习场/`，文件名自己定，例如 `ex01_sum.py`。  
答案在 `练习场/答案参考/`，**先自己写再看**。

每章对应的可运行示例：

| 章 | 文件 |
| --- | --- |
| 1 | `示例代码/01_hello.py` |
| 2 | `示例代码/02_types.py` |
| 3 | `示例代码/03_strings.py` |
| 4 | `示例代码/04_lists.py` |
| 5 | `示例代码/05_dicts.py` |
| 6 | `示例代码/06_if.py` |
| 7 | `示例代码/07_loops.py` |
| 8 | `示例代码/08_functions.py` |
| 9 | `示例代码/09_files.py` |
| 10 | `示例代码/10_exceptions.py` |
| 11 | `示例代码/11_modules.py` |
| 12 | `示例代码/12_stdlib.py` |

---

## 19. 快速自测（不看资料能不能答）

1. `"3" + "4"` 和 `3 + 4` 分别是什么？
2. 列表和字典哪一个靠下标、哪一个靠键？
3. `for` 和 `while` 分别什么时候用？
4. `print(x)` 和 `return x` 有什么不同？
5. 为什么写文件要写 `encoding="utf-8"`？
6. 字典没有某个键时，`d[k]` 和 `d.get(k)` 谁更安全？
7. 小工具为什么要用 `if __name__ == "__main__":`？

能答 5 个以上，就可以把注意力转到改小工具，而不是再刷语法。

---

下一步打开 [`小工具制作指导.md`](./小工具制作指导.md)。  
以后要在本文件夹续写，看 [`后续编辑说明.md`](./后续编辑说明.md)。
