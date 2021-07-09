from collections import deque
import sys

input = sys.stdin.readline

# parsing
N = int(input().strip())
info = list()

for __ in range(N):
	tmp = list()
	tmp.append(int(input().strip()))
	tmp.append(tuple(map(int, input().strip().split())))
	tmp.append(tuple(map(int, input().strip().split())))
	info.append(tmp)

###
## solve
# make graph
def make_graph(n):
	return [[0]*n for __ in range(n)]

# BFS
dx = [2, 2, -2, -2, -1, -1, 1, 1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

def bfs(n, start, end):
	global dx, dy
	graph = make_graph(n)
	q = deque([start])
	graph[start[0]][start[1]] = 1
	while q:
		x, y = q.popleft()
		for i in range(8):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
				graph[nx][ny] = graph[x][y] + 1
				q.append((nx, ny))
	return graph[end[0]][end[1]] - 1

# print
for i in range(N):
	print(bfs(info[i][0], info[i][1], info[i][2]))