import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n, m = map(int, input().split())
root = [i for i in range(n+1)]

def insert(x, y):
	x = rootchecker(x)
	y = rootchecker(y)
	if x < y:
		x, y = y, x
	root[x] = y

def rootchecker(x):
	if root[x] == x:
		return x
	root[x] = rootchecker(root[x])
	return root[x]
	

for _ in range(m):
	cmd, x, y = map(int, input().split())
	if cmd == 0:
		insert(x, y)
	else:
		print("YES" if rootchecker(x) == rootchecker(y) else "NO")