import random

a = 0
for _ in range(1, 10000):
	a += random.randint(0, 10)
print(a)
