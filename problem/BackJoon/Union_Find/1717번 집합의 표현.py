import sys

n, m = map(int, sys.stdin.readline().split())
checker = [i for i in range(n+1)]

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

for _ in range(m):
	flag, a, b = map(int, sys.stdin.readline().split())
	if flag:
		print("YES") if myfind(a) == myfind(b) else print("NO")
	else:
		myunion(a, b)