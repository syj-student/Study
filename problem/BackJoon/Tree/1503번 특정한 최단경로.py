import collections
import heapq
import sys


graph = collections.defaultdict(list)
node_cnt, load_cnt = map(int, sys.stdin.readline().split())
for _ in range(load_cnt):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
via1, via2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    heap = [(0, start)]
    distance = [float('inf')] * (node_cnt + 1)
    visited = [1] * (node_cnt + 1)
    distance[start] = 0
    while heap:
        now_distance, now_location = heapq.heappop(heap)
        if visited[now_location]:
            visited[now_location] = 0
            for new_location, new_distance in graph[now_location]:
                total_distance = new_distance + now_distance
                if visited[new_location] and total_distance < distance[new_location]:
                    distance[new_location] = total_distance
                    heapq.heappush(heap, (total_distance, new_location))
    return distance


start_distance = dijkstra(1)
via1_distance = dijkstra(via1)
via2_distance = dijkstra(via2)
answer = min(
    start_distance[via1] + via1_distance[via2] + via2_distance[-1],
    start_distance[via2] + via2_distance[via1] + via1_distance[-1],
)
print(answer if answer < float('inf') else -1)
