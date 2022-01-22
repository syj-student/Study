import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
checker = [i for i in range(n)]

def myfind(x):
	if checker[x] == x:
		return x
	return myfind(checker[checker[x]])

def myunion(x, y):
	x = myfind(x)
	y = myfind(y)
	if x > y:
		checker[y] = x
	elif x < y:
		checker[x] = y


table = list()
for _ in range(n):
	table.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
	for j in range(i, n):
		if table[i][j] == 1:
			myunion(i, j)


plan = set(map(lambda x: myfind(int(x)-1), sys.stdin.readline().split()))
if len(plan) == 1:
	print("YES")
else:
	print("NO")
