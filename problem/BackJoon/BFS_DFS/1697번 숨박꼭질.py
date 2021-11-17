from collections import deque
import sys

input = sys.stdin.readline

a, b = map(int, input().strip().split())

# BFS
q  = deque([(a, 0)])
visited = set()
ret = 100000
while q:
	x, cnt = q.popleft()
	if x == b and cnt < ret:
		ret = cnt
	if x not in visited:
		visited.add(x)
		if x * 2 <= 100000:
			q.append((x * 2, cnt + 1))
		if 0 <= x - 1:
			q.append((x - 1, cnt + 1))
		if x + 1 <= 100000:
			q.append((x + 1, cnt + 1))
		
# print answer
print(ret)