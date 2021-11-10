import heapq
graph = {
	'A': {'B': 8, 'C': 1, 'D': 2},
	'B': {},
	'C': {'B': 5, 'D': 2},
	'D': {'E': 3, 'F': 5},
	'E': {'F': 1},
	'F': {'A': 5}
}

def dijkstra(graph, start):
	d = {node : float('inf') for node in graph}
	d[start] = 0
	q = [(d[start], start)]
	while q:
		current_distance, current_destination = heapq.heappop(q)
		if d[current_destination] < current_distance:
			continue
		for new_destination, new_distance in graph[current_destination].items():
			distance = current_distance + new_distance
			if distance < d[new_destination]:
				d[new_destination] = distance
				heapq.heappush(q, [distance, new_destination])
	return d

print(dijkstra(graph, 'A'))