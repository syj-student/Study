import sys
import copy

input = sys.stdin.readline
n = int(input())
m = list()
for _ in range(n):
	m.append(list(input().strip()))
m2 = copy.deepcopy(m)
for i in range(len(m2)):
	for j in range(len(m2[0])):
		if m2[i][j] == "G":
			m2[i][j] = "R"

answer = list()

def solve(m):
	ret = 0
	for i in range(len(m)):
		for j in range(len(m[0])):
			if m[i][j] in "RGB":
				dfs(i, j, m)
				ret += 1
	answer.append(ret)

def dfs(i, j, m):
	c = m[i][j]
	dx = [0, 0, 1, -1]
	dy = [1, -1, 0, 0]
	stack = [(i, j)]
	m[i][j] = "A"
	while stack:
		x, y = stack.pop()
		for k in range(4):
			nx = x + dx[k]
			ny = y + dy[k]
			if 0 <= nx < len(m) and 0 <= ny < len(m[0]) and m[nx][ny] == c:
				stack.append((nx, ny))
				m[nx][ny] = "A"

solve(m)
solve(m2)
print(*answer)