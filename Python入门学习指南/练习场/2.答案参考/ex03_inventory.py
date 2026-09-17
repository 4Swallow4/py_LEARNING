"""题 3 参考答案：字典查询。"""

inventory = {"pen": 3, "book": 1, "cable": 2}


def count_item(stock, name):
    return stock.get(name, 0)


print("pen", count_item(inventory, "pen"))
print("ink", count_item(inventory, "ink"))
print("数量≥2:")
for name, n in inventory.items():
    if n >= 2:
        print("-", name, n)
