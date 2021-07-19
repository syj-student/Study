from collections import deque
import random

# make random list
ret = list()
for __ in range(10):
	ret.append(random.randrange(-100, 101))
print(f'Before : {ret}')

def merge_sort(lst):
	n = len(lst)
	if n <= 1:
		return lst
	mid = n // 2
	g1 = merge_sort(lst[:mid])
	g2 = merge_sort(lst[mid:])
	result = list()
	while g1 and g2:
		if g1[0] <= g2[0]:
			result.append(g1.pop(0))
		else:
			result.append(g2.pop(0))
	while g1:
		result.append(g1.pop(0))
	while g2:
		result.append(g2.pop(0))
	return result

print(merge_sort(ret))