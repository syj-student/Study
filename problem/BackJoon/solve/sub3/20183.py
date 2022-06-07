import collections
import heapq
import sys

input = sys.stdin.readline

# a: node, b: edge, c: start, d: end, c: cost
a, b, c, d, e = map(int, input().split())

m = collections.defaultdict(list)
costs = list()
for _ in range(b):
	x, y, z = map(int, input().split())
	m[x].append((y, z))
	m[y].append((x, z))
	heapq.heappush(costs, -z)


def dijkstra(mid):
	answer = [float('inf')] * (a+1)
	visited = [False] * (a+1)
	answer[c] = 0
	h = [(0, c)]
	while h:
		now_cost, now_node = heapq.heappop(h)
		if not visited[now_node]:
			visited[now_node] = True
			for next_node, next_cost in m[now_node]:
				if next_cost > mid:
					continue
				new_cost = now_cost + next_cost
				if new_cost <= e and not visited[next_node] and new_cost < answer[next_node]:
					heapq.heappush(h, (new_cost, next_node))
					answer[next_node] = new_cost
	return False if answer[d] == float('inf') else True
L = 0
R = -heapq.heappop(costs)
answer = float('inf')
while L <= R:
	mid=(L+R)//2
	if dijkstra(mid):
		answer = min(mid, answer)
		R = mid - 1
	else:
		L = mid + 1
if answer == float('inf'):
	print(-1)
else:
	print(answer)