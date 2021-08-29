import sys
import collections

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
stack = collections.deque()
for x in range(m):
	for y in range(n):
		if graph[x][y] == 1:
			stack.append((x, y))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while stack:
	tmp = stack.popleft()
	for i in range(4):
		nx = dx[i] + tmp[0]
		ny = dy[i] + tmp[1]
		if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
			stack.append((nx, ny))
			graph[nx][ny] = graph[tmp[0]][tmp[1]] + 1
flag = 1
for x in range(m):
	for y in range(n):
		if graph[x][y] == 0:
			print(-1)
			exit()
ret = [max(i) for i in graph]
print(max(ret) - 1)