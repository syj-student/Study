import collections
import heapq

def solution(n, paths, gates, summits):
	t = collections.defaultdict(dict)
	for a, b, c in paths:
		t[a][b] = c
		t[b][a] = c

	def checker(start, end, x):
		dis = [float('inf')] * (n+1)
		c = [i for i in range(n+1)]
		dis[start] = 0
		dontgo = gates[:] + summits[:]
		dontgo.remove(x)

		visited = [False] * (n+1)
		visited[start] = True
		h = [[0, start, float('inf')]]
		while h:
			now_cost, now, prev_cost = heapq.heappop(h)
			visited[now] = True
			for nxt, nxt_cost in t[now].items():
				new_cost = nxt_cost + now_cost
				if not visited[nxt] and not nxt in dontgo and prev_cost < dis[nxt]:
					dis[nxt] = new_cost
					
					c[nxt] = now
					heapq.heappush(h, [new_cost, nxt])
		its = [0]
		def make_its(start, end):
			print(start, end=" ")
			if start == end:
				return
			its[0] = max(its[0], t[start][c[start]])
			make_its(c[start], end)
		make_its(end, start)

		print("|", start, end, dis)
		return its[0]

	answer = [float('inf'), float('inf')]
	for g in gates:
		for s in summits:
			h = checker(g, s, s)
			h2 = checker(s, g, g)
			print(h, h2)
			if min(h, h2) < answer[1]:
				answer[0] = s
				answer[1] = min(h, h2)
	return answer
print(solution(
6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]
))
