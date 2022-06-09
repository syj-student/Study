import collections
import heapq
import sys

input = sys.stdin.readline

# a: node, b: edge, c: start, d: end, e: cost
a, b, c, d, e = map(int, input().split())

m = collections.defaultdict(list)
for _ in range(b):
	x, y, z = map(int, input().split())
	m[x].append((y, z))
	m[y].append((x, z))

def dijkstra():
	visited = [False] * (a+1)
	dist = [float('inf')] * (a+1)
	dist[c] = 0
	h = [(0, e, c)]
	while h:
		cur_max_pay, remain_cost, cur_node = heapq.heappop(h)
		if cur_max_pay > dist[cur_node]:
			continue
		visited[cur_node] = True
		for next_node, next_cost in m[cur_node]:
			next_max_pay = max(cur_max_pay, next_cost)
			next_remain_cost = remain_cost - next_cost
			if not visited[next_node] and next_remain_cost >= 0 and next_max_pay < dist[next_node]:
				dist[next_node] = next_max_pay
				heapq.heappush(h, (next_max_pay, next_remain_cost, next_node))
	return -1 if dist[d] == float('inf') else dist[d]

print(dijkstra())