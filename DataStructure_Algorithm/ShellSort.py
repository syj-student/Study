import random
import copy

# make random list
ret = list()
for __ in range(10):
	ret.append(random.randrange(-100, 101))
print(f'Before : {ret}')

# compare
comp = copy.deepcopy(ret)
length = len(comp)
cnt = 0
for idx in range(length):
	while idx + 1 < length:
		if comp[idx] > comp[idx + 1]:
			cnt += 1
			comp[idx], comp[idx + 1] = comp[idx + 1], comp[idx]
		idx += 1
print(f'After  : {comp}')
print(cnt)

# Shell Sort
length = len(ret)
gap = length // 2
if not (gap % 2): gap += 1
flag = False
cnt = 0
while 1:
	if gap == 1:
		flag = True
	for idx in range(length):
		while idx + gap < length:
			if ret[idx] > ret[idx + gap]:
				cnt += 1
				ret[idx], ret[idx + gap] = ret[idx + gap], ret[idx]
			idx += gap
	if flag:
		break
	gap //= 2
	if not (gap % 2): gap += 1
print(f'After  : {ret}')
print(cnt)