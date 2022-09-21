from collections import defaultdict

a = defaultdict(int)
print(len(a))
a["hello"] = 1
a["hello"] -= 1
print(len(a))