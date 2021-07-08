import random

# make random list
ret = list()
for __ in range(10):
	ret.append(random.randrange(-100, 101))
print(f'Before : {ret}')

# Binary Insertion Sort
n = len(ret)
for i in range(1, n):
	key = ret[i]
	pl = 0
	pr = i - 1
	while True:
		pc = (pl + pr) // 2
		if ret[pc] == key: break
		elif ret[pc] < key: pl = pc + 1
		else: pr = pc - 1
		if pl > pr: break
	if pl <= pr: pd = pc + 1
	else: pd = pr + 1
	for j in range(i, pd, -1):
		ret[j] = ret[j-1]
	ret[pd] = key
print(f'After  : {ret}')