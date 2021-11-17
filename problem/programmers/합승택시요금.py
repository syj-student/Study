import collections
import copy
import heapq

def Dijkstra(graph, departure, arrival, n):
	if departure == arrival:
		return 0
	fares_table = [float('INF')] * (n + 1)
	fares_table[departure] = 0
	heap = [(fares_table[departure], departure)]
	while heap:
		fare, now_node = heapq.heappop(heap)
		if fares_table[now_node] < fare:
			continue
		for next_node, next_fare in graph[now_node].items():
			total_fare = fare + next_fare
			if total_fare < fares_table[next_node]:
				fares_table[next_node] = total_fare
				heapq.heappush(heap, (total_fare, next_node))
	return fares_table[arrival]

def solution(n, s, a, b, fares):
	# make graph
	fares_graph = collections.defaultdict(dict)
	for departure, arrival, f in fares:
		fares_graph[departure][arrival] = f
		fares_graph[arrival][departure] = f

	# each lowest fare
	min_fare = float('inf')
	for i in range(1, n+1):
		if not fares_graph[i]:
			continue
		total_fare = 0
		s_to_i = Dijkstra(fares_graph, s, i, n)
		if s_to_i == float('INF'):
			min_fare = min(Dijkstra(fares_graph, s, a, n) + Dijkstra(fares_graph, s, b, n), min_fare)
			continue
		total_fare += s_to_i
		i_to_a = Dijkstra(fares_graph, i, a, n)
		if i_to_a == float('INF'):
			min_fare = min(Dijkstra(fares_graph, s, a, n) + Dijkstra(fares_graph, s, b, n), min_fare)
			continue
		total_fare += i_to_a
		i_to_b = Dijkstra(fares_graph, i, b, n)
		if i_to_b == float('INF'):
			min_fare = min(Dijkstra(fares_graph, s, a, n) + Dijkstra(fares_graph, s, b, n), min_fare)
			continue
		total_fare += i_to_b
		min_fare = min(min_fare, total_fare)
	return min_fare








fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
fares2 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
fares3 = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
test = [[2,6,6], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print('solution : ', solution(7, 6, 6, 6, test))