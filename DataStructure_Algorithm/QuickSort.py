import random

# make random list
ret = list()
for __ in range(10):
	ret.append(random.randrange(-100, 101))
print(f'Before : {ret}')

# Quick Sort
def quick_sort(mix):
	length = len(mix)
	if length <= 1:
		return mix
	bigger = list(); equal = list(); smaller = list()
	p = mix[length // 2]
	for x in mix:
		if x > p: bigger.append(x)
		elif x == p: equal.append(x)
		else: smaller.append(x)
	return quick_sort(smaller) + equal + quick_sort(bigger)
ret = quick_sort(ret)
print(f'After  : {ret}')