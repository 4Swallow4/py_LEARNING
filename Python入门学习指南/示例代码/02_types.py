"""02 变量和类型。"""

n = 4
x = 3.14
s = "python"
ok = True
empty = None

print("n =", n, "类型", type(n))
print("x =", x, "类型", type(x))
print("s =", s, "类型", type(s))
print("ok =", ok, "类型", type(ok))
print("empty =", empty, "类型", type(empty))

print("--- 转换 ---")
print(int("12"), float("3.5"), str(12), bool(0), bool("0"))

print("--- 运算 ---")
print("整数除法 7 // 2 =", 7 // 2) #跟C写法不同
print("余数 7 % 2 =", 7 % 2)
print("真除法 7 / 2 =", 7 / 2) #直接出小数

# 和你在 py_LEARNING/练习/1.py 里类似的写法
p = pp = 4
app = 2
print("p, pp, app =", p, pp, app)
print("p + app =", p + app)
