scores = [92, 85, 76, 61, 40, 88]
passed = [s for s in scores if s >= 60]
print("及格分数:", passed)
print(" ".join(str(s) for s in passed)) # 用空格隔开的写法
print("及格人数:", len(passed))
print("平均分:", sum(scores)/len(scores))