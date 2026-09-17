"""题 2 参考答案：列表过滤。"""

scores = [92, 85, 76, 61, 40, 88]
passed = [s for s in scores if s >= 60]
print("及格分数:", passed)
print("及格人数:", len(passed))
print(f"全部平均: {sum(scores) / len(scores):.1f}")
