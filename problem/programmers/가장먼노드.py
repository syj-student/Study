import collections
import heapq

def dijkstra(graph, n, start_point=1):
	answer = [float('inf')] * (n + 1)
	answer[start_point] = answer[0] = 0
	heap = [(0, 1)]
	while heap:
		d, node = heapq.heappop(heap)
		if d > answer[node]:
			continue
		for distance, next_node in graph[node]:
			cost = distance + d
			if cost < answer[next_node]:
				answer[next_node] = cost
				heapq.heappush(heap, (cost, next_node))
	return answer

def solution(n, edge):
	graph = collections.defaultdict(list)
	for d, a in edge:
		graph[d].append((1, a))
		graph[a].append((1, d))
	distance = dijkstra(graph, n)
	print(distance)
	counter = collections.Counter(distance)
	return counter[max(counter)]

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))