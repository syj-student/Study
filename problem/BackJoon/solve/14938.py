import sys
import heapq
import collections

input = sys.stdin.readline
a, b, c = map(int, input().split())
p = collections.defaultdict(list)
items = list(list(map(int, input().split())))
for _ in range(c):
	arrival, departure, cost = map(int, input().split())
	arrival -= 1
	departure -= 1
	p[arrival].append((departure, cost))
	p[departure].append((arrival, cost))
answer = 0
def dijkstra(start):
	global answer
	dis = [float('inf')] * a
	visited = [False] * a
	dis[start] = 0
	h = [(0, start)]
	while h:
		now_cost, now_node = heapq.heappop(h)
		if not visited[now_node]:
			visited[now_node] = True
			for next_node, next_cost in p[now_node]:
				new_cost = next_cost + now_cost
				if not visited[next_node] and new_cost < dis[next_node]:
					dis[next_node] = new_cost
					heapq.heappush(h, (new_cost, next_node))
	tmp = 0
	for i in range(a):
		if dis[i] <= b:
			tmp += items[i]
	answer = max(answer, tmp)

for i in range(a):
	dijkstra(i)

print(answer)