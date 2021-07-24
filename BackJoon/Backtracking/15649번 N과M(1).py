from collections import deque
import sys

input = sys.stdin.readline

# input
n, m = map(int, input().strip().split())

# make list
check = [True] * (n + 1)
ret = list()

def dfs(depth, n, m):
	if depth == m:
		print(*ret)
		return
	for i in range(1, n + 1):
		if check[i]:
			ret.append(i)
			check[i] = False
			dfs(depth + 1, n, m)
			check[i] = True
			ret.pop()

dfs(0, n, m)