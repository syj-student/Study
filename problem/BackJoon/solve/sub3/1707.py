import sys
import collections

input = sys.stdin.readline

def dfs(start):
	q = collections.deque([start])
	color[start] = 1
	while q:
		cur = q.pop()
		visited[cur] = True
		for i in g[cur]:
			if not visited[i]:
				q.append(i)
				color[i] = -color[cur]
			elif color[i] == color[cur]:
				return False
	return True


n = int(input())
for _ in range(n):
	a, b = map(int, input().split())
	
	g = collections.defaultdict(list)
	for _ in range(b):
		q, w = map(int, input().split())
		g[q].append(w)
		g[w].append(q)
	
	visited = [False] * (a+1)
	color = [None] * (a+1)
	for i in range(1, a+1):
		if not visited[i]:
			if not dfs(i):
				print("NO")
				break
	else:
		print("YES")

