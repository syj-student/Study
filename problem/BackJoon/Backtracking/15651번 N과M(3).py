import sys

# input
n, m = map(int, sys.stdin.readline().split())

# solve
answer = set()
ret = list()
def dfs(n, depth, m):
	if depth == m:
		print(*ret)
		return
	for i in range(1, n + 1):
		ret.append(i)
		dfs(n, depth + 1, m)
		ret.pop()

# print
dfs(n, 0, m)