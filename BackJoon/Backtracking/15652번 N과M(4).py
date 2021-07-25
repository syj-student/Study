import sys

# input
n, m = map(int, sys.stdin.readline().split())

# solve
answer = set()
ret = list()
def dfs(n, depth, m, x=1):
	if depth == m:
		print(*ret)
		return
	for i in range(x, n + 1):
		ret.append(i)
		dfs(n, depth + 1, m, i)
		ret.pop()

# print
dfs(n, 0, m)