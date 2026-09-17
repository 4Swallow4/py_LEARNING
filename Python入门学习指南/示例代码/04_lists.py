"""04 列表、元组、集合。"""

scores = [92, 85, 76]
print("原始:", scores)

scores.append(88)
print("append 88:", scores)

scores.insert(0, 100)
print("insert 100:", scores)

last = scores.pop()
print("pop 出", last, "剩下", scores)

print("第一个", scores[0], "最后一个", scores[-1])
print("切片 [1:3]", scores[1:3])
print("sum/max/min", sum(scores), max(scores), min(scores))
print("sorted 新列表", sorted(scores), "原来还是", scores)

# 遍历
total = 0
for s in scores:
    total += s
print("手写求和", total, "平均", total / len(scores))

point = (3, 4)
x, y = point
print("元组拆包", x, y)

letters = {"a", "b", "a", "c"}
print("集合去重", letters)
print("'a' in letters?", "a" in letters)

# 陷阱：两个名字指向同一列表
a = b = []
a.append(1)
print("a is b?", a is b, "b 现在是", b)
