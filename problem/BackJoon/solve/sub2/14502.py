import itertools
import sys
import copy
import collections

input = sys.stdin.readline

table = list()
n, m = map(int, input().split())
for _ in range(n):
	table.append(list(map(int, input().split())))
visited = [[False for _ in range(m)] for _ in range(n)]
def init_visited():
	for i in range(len(visited)):
		for j in range(len(visited[0])):
			visited[i][j] = False

def check_safe_zone(t):
	def bfs(i, j):
		dx = [0, 0, -1, 1]
		dy = [1, -1, 0, 0]
		dq = collections.deque([(i, j)])
		t[i][j] = -1
		while dq:
			x, y = dq.popleft()
			for k in range(4):
				nx = x + dx[k]
				ny = y + dy[k]
				if 0 <= nx < n and 0 <= ny < m and t[nx][ny] == 0:
					dq.append((nx, ny))
					t[nx][ny] = -1

	for i in range(n):
		for j in range(m):
			if t[i][j] == 2:
				bfs(i, j)


def choose_wall():
	ret = list()
	for i in range(n):
		for j in range(m):
			if table[i][j] == 0:
				ret.append((i, j))
	return ret

answer = 0
def counter(t):
	ret = 0
	for i in range(n):
		for j in range(m):
			if t[i][j] == 0:
				ret += 1
	return ret

for case in itertools.combinations(choose_wall(), 3):
	t = copy.deepcopy(table)
	for a, b in case:
		t[a][b] = 1
	check_safe_zone(t)
	answer = max(answer, counter(t))
print(answer)


