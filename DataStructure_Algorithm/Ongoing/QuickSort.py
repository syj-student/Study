import random

# make random list
ret = list()
for __ in range(10):
	ret.append(random.randrange(-100, 101))
print(f'Before : {ret}')

# Quick Sort

length = len(ret)
p0 = length // 2; pl = 0; pr = length - 1
while 1:
	while 