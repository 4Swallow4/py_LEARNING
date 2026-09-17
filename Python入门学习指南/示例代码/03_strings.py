"""03 字符串常用操作。"""

name = "YanZ"
lang = "Python"

print(f"Hello, {name}. 正在学 {lang}.")
print("拼接:", "py" + "thon")
print("重复:", "ha" * 3)
print("长度:", len("python"))
print("下标 0:", "python"[0], "下标 -1:", "python"[-1])
print("切片 [0:3]:", "python"[0:3]) # 从第0个开始输出，不含第三个'h'

raw = "  Hello, Python  "
print("strip:", raw.strip())
print("lower:", lang.lower()) #全部小写
print("replace:", "hello".replace("l", "L"))
print("split:", "a,b,c".split(","))
print("join:", "_".join(["2026", "09", "12"]))

filename = "notes.txt"
print("是 txt 吗?", filename.endswith(".txt"))
print("'y' in lang?", "y" in lang)

# 字符串方法返回新值，不改原来的
s = "abc"
s.upper()
print("没接住返回值:", s)
s = s.upper() # 全部大写
print("接住了:", s)
