import random

# make random list
ret = list()
for __ in range(10):
	ret.append(random.randrange(-100, 101))
print(f'Before : {ret}')

# Select Sort
length = len(ret)
for i in range(length - 1):
	ret_min = i
	for j in range(i + 1, length):
		if ret[j] < ret[ret_min]:
			ret_min = j
	ret[i], ret[ret_min] = ret[ret_min], ret[i]
print(f'After  : {ret}')