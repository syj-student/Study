from collections import deque
import random

# make random list
ret = list()
for __ in range(10):
	ret.append(random.randrange(-100, 101))
print(f'Before : {ret}')

# InsertionSort Sort
length = len(ret)
for i in range(1, length):
	for j in range(i):
		if ret[j] > ret[i]:
			ret[i], ret[j] = ret[j], ret[i]
			break
print(f'After  : {ret}')