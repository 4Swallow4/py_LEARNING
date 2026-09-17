"""07 循环。"""

print("--- for 列表 ---")
for name in ["Alice", "Bob", "Carol"]:
    print("你好,", name)

print("--- range ---")
for i in range(1, 4): 
    print("第", i, "次") # 输出1，2，3

print("--- enumerate ---")
files = ["a.py", "b.py"]
for i, name in enumerate(files, start=1): #enumerate() 函数可以同时获取索引和值，start=1 表示索引从 1 开始
    print(i, name)

print("--- list ---")
files = ["a.py", "b.py"]
for name in files:
    print(name)

print("--- while ---")
n = 3
while n > 0:
    print("倒计时", n)
    n -= 1

print("--- break / continue ---")
for n in range(8):
    if n % 2 == 0:
        continue
    if n > 5:
        break
    print("奇数", n)

print("--- 同时遍历两个列表 ---")
names = ["Alice", "Bob"]
maths = [92, 76]
for name, math in zip(names, maths):
    print(name, math)

print("--- 列表推导 ---")
# n默认为0；这里表示循环遍历0到5这六个数字，若n是偶数则输出n*n的值
print([n * n for n in range(6) if n % 2 == 0]) 

