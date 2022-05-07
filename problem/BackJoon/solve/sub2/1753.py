import sys
import collections
import heapq


input = sys.stdin.readline
m, n = map(int, input().split())
start = int(input())
t = collections.defaultdict(list)
for _ in range(n):
	a, b, c = map(int, input().split())
	t[a].append((b, c))
dis = [float('inf')] * (m+1)
visited = [False] * (m+1)

def dijkstra(start):
	dis[start] = 0
	h = [(0, start)]
	while h:
		now_cost, now = heapq.heappop(h)
		visited[now] = True
		for dest, cost in t[now]:
			new_cost = now_cost + cost
			if not visited[dest] and dis[dest] > new_cost:
				dis[dest] = new_cost
				heapq.heappush(h, (new_cost, dest))

dijkstra(start)

for i in range(1, len(dis)):
	if dis[i] == float('inf'):
		print("INF")
	else:
		print(dis[i])
