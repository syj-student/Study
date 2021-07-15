import random

# make random list
ret = list()
for __ in range(10):
	ret.append(random.randrange(-100, 101))
print(f'Before : {ret}')

## Binary Insertion Sort
# Binary Search
length = len(ret)
for i in range(1, length):
	pl = 0
	pr = i - 1
	while True:
		pc  = (pl + pr) // 2
		if ret[pc] < ret[i]:
			pl = pc + 1
		else:
			pr = pc - 1
		if pl > pr:
			break
	ret.insert(pl, ret.pop(i))
print(f'After  : {ret}')