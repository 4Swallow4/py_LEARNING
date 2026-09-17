"""06 分支。"""


def grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 60:
        return "C"
    return "D"


for s in [95, 88, 61, 40]:
    # if/else 赋值语句
    status = "及格" if s >= 60 else "不及格"
    print(f"分数 {s:>3} → {grade(s)} ({status})") # s:>3 表示右对齐，占 3 个字符宽度

filename = "report.CSV"
# .lower()不会改变原值，.endwith()判断后缀
if filename.lower().endswith(".csv") and "report" in filename.lower():
    print("这是一份报表 csv")
else:
    print("这份不是报表文件")    

# 空容器在 if 里是假
pending = []
if not pending:
    print("没有待办")
