import collections
import heapq
import sys

while True:
	number = 1
	n = int(sys.stdin.readline().strip())
	if n == 0:
		break
	map_info = list()
	for _ in range(n):
		map_info.append(list(map(int, sys.stdin.readline().split())))
	dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
	money_map = [[sys.maxsize for _ in range(n)] for _ in range(n)]
	print(money_map)
	pq = collections.deque([(0, 0)])
	for x in range(n):
		for y in range(n):
			stack = list()
			for i in range(4):
				nx = x + dx[i]
				ny = y + dy[i]
				if 0 <= nx < n and 0 <= ny < n:
					stack.append((nx, ny))
			while stack:
				new_x, new_y = stack.pop()
	print(money_map)
	print(f'Problem {number}: {money_map[n-1][n-1]}')
	number += 1
	pq.clear()
