import sys
import heapq
from collections import defaultdict

node_size, load_size = map(int, sys.stdin.readline().split())
departure = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(load_size):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((cost, end))


def dijkstra(d):
    ret = [float('INF')] * (node_size + 1)
    visited = [0] * (node_size + 1)
    heap, ret[d] = [(0, d)], 0
    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if not visited[now_node]:
            visited[now_node] = 1
            for next_cost, next_node in graph[now_node]:
                total_cost = now_cost + next_cost
                if not visited[next_node] and ret[next_node] > total_cost:
                    ret[next_node] = total_cost
                    heapq.heappush(heap, (total_cost, next_node))
    return ret

answer = dijkstra(departure)
for i in range(1, node_size + 1):
    if answer[i] == float('inf'):
        print("INF")
    else:
        print(answer[i])
