"""05 字典。衔接 py_LEARNING/练习/字典.py。"""

# 字典是键值对的集合，键必须是不可变类型（如字符串、整数、**元组**），值可以是任意类型。
gadget = {# 冒号左：键，冒号右：值
    "brand": "UNIKO",
    "model": "she",
    "year": "2026",
}
print("整份字典:", gadget)
print("get model:", gadget.get("model"))
print("没有的键 get:", gadget.get("color"))  # None，不报错
print("没有的键带默认值:", gadget.get("color", "unknown"))

# gadget["color"]  # 取消注释会 KeyError

gadget["year"] = 2026  # 改成整数，比较年份更方便
gadget["color"] = "teal" # 新增键值对或覆盖原值
print("更新后:", gadget)
print("年是整数吗?", isinstance(gadget["year"], int))

print("--- 遍历键值 ---")
for key, value in gadget.items():
    print(f"  {key} = {value}")

students = {
    "Alice": {"math": 92, "eng": 85},
    "Bob": {"math": 76, "eng": 88},
}
print("Alice 数学:", students["Alice"]["math"])

# 按姓名汇总：小工具 csv_summary 就是这个结构
by_name = {}
for name, subjects in students.items(): # for循环的in前面是两个变量，分别对应字典的键和值；其他写法同理，取决于右边的数据结构
    avg = sum(subjects.values()) / len(subjects)
    by_name[name] = avg
print("平均分:", by_name)
