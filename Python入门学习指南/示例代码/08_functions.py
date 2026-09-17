"""08 函数。"""


def average(nums):
    """返回非空数字序列的平均值；空序列返回 0.0。"""
    if not nums:
        return 0.0
    return sum(nums) / len(nums)


def greet(name, prefix="Hi"):
    return f"{prefix}, {name}"


def min_max(nums):
    return min(nums), max(nums)  # 返回元组


print(average([90, 80, 70]))
print(average([]))
print(greet("Tomo"))
print(greet("Tomo", prefix="Hello"))

lo, hi = min_max([92, 61, 88])
print("最低", lo, "最高", hi)

# 列表作为参数：函数里 append 会改到外面
def add_flag(xs):
    xs.append("changed")


data = ["ok"]
add_flag(data)
print("外面的 data:", data)


def add_flag_safe(xs):
    copy = list(xs)
    copy.append("changed")
    return copy


print("安全版本原列表:", ["ok"], "新列表:", add_flag_safe(["ok"]))
