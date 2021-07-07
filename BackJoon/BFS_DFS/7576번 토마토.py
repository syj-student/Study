import sys
from collections import deque

input = sys.stdin.readline

# input
m, n = map(int, input().strip().split())

# graph
graph = [list(map(int, input().strip().split())) for __ in range(n)]

# search start_point
q = deque()
for i in range(n):
	for j in range(m):
		if graph[i][j] == 1:
			q.append((i, j))

# DFS
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
	x, y = q.popleft()
	for i in range(4):
		cx = x + dx[i]
		cy = y + dy[i]
		if  0 <= cx < n and 0 <= cy < m and graph[cx][cy] == 0:
			q.append((cx, cy))
			graph[cx][cy] = graph[x][y] + 1

# print answer
max = graph[0][0]
flag = True
for i in range(n):
	for j in range(m):
		if graph[i][j] == 0:
			print(-1)
			flag = False
			exit()
		elif graph[i][j] > max:
			max = graph[i][j]
if flag:
	print(max - 1)