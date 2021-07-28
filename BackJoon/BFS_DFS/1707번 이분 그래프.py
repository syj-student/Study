import sys

# input
n = int(sys.stdin.readline())

# dfs
def dfs(a):
	for i in range(1, a + 1):
		stack = list()
		if not check[i]:
			stack.append(i)
			check[i] = 1
		else:
			stack.append(i)
		while stack:
			nt = stack.pop()
			for j in tmp[nt]:
				if check[j] == 0:
					stack.append(j)
					if check[nt] == 1:
						check[j] = 2
					elif check[nt] == 2:
						check[j] = 1
				elif check[nt] == check[j]:
					return print('NO')
	return print('YES')

# make graph
for __ in range(n):
	a, b = map(int, sys.stdin.readline().split())
	tmp = {i : [] for i in range(1, a + 1)}
	check = [0] * (a + 1)
	for __ in range(b):
		x, y = map(int, sys.stdin.readline().split())
		tmp[x].append(y)
		tmp[y].append(x)
	dfs(a)