from collections import deque
import sys

input = sys.stdin.readline

x, y, z = map(int, input().strip().split())

# graph
graph = list()
for __ in range(z):
	graph.append([list(map(int, input().strip().split())) for __ in range(y)])

# search start point
q = deque()
for i in range(z):
	for j in range(y):
		for k in range(x):
			if graph[i][j][k] == 1:
				q.append((k, j, i))

# DFS
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]
while q:
	a, b, c = q.popleft()
	for i in range(6):
		nX = a + dx[i]
		nY = b + dy[i]
		nZ = c + dz[i]
		if 0 <= nX < x and 0 <= nY < y and 0 <= nZ < z and graph[nZ][nY][nX] == 0:
			q.append((nX, nY, nZ))
			graph[nZ][nY][nX] = graph[c][b][a] + 1

# print answer
ret = graph[0][0][0]
for i in range(z):
	for j in range(y):
		for k in range(x):
			if graph[i][j][k] == 0:
				print(-1)
				exit()
			elif graph[i][j][k] > ret:
				ret = graph[i][j][k]
print(ret - 1)