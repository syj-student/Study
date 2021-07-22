import random

# make random list
ret = list()
for __ in range(10):
	ret.append(random.randrange(0, 101))
print(f'Before : {ret}')

# solve
def count_sort(lst):
	cnt = [0] * (max(lst) + 1)
	ret = [0 ]* len(lst)
	for i in lst:
		cnt[i] += 1
	for i in range(1, max(lst) + 1):
		cnt[i] += cnt[i - 1]
	for i in lst:
		ret[cnt[i] - 1] = i
		cnt[i] -= 1
	return ret

ret = count_sort(ret)
print(ret)