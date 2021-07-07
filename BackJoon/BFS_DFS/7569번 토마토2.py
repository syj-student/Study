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
				q.append((i, j, k))

# DFS
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]


for i in range(z):
	for j in range(y):
		print(graph[i][j])