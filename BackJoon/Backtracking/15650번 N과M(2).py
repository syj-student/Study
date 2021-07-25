import sys

# input
n, m = map(int, sys.stdin.readline().split())

# solve
answer = set()
ret = list()
check = [True] * (n + 1)
def dfs(n, depth, m):
	if depth == m:
		answer.add(tuple(sorted(ret)))
		return
	for i in range(1, n + 1):
		if check[i]:
			ret.append(i)
			check[i] = False
			dfs(n, depth + 1, m)
			check[i] = True
			ret.pop()

# print
dfs(n, 0, m)
for i in sorted(list(answer)):
	print(*i)