import sys
import heapq
from collections import defaultdict


def dijkstra(departure, graph, size):
    ret = [float('inf')] * (size + 1)
    ret[departure] = 0
    visited = [0] * (size + 1)
    heap = [(0, departure)]
    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if not visited[now_node]:
            visited[now_node] = 1
            for next_cost, next_node in graph[now_node]:
                total_cost = next_cost + now_cost
                if not visited[next_node] and total_cost < ret[next_node]:
                    ret[next_node] = total_cost
                    heapq.heappush(heap, (total_cost, next_node))
    return ret[1:]


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = defaultdict(list)
for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((c, e))

answer = list()
for i in range(1, n+1):
    answer.append(dijkstra(i, graph, n))

for row in answer:
    print(*map(lambda x: 0 if x == float('inf') else x, row))

# 입력을 받을 때 기존 start, end가 같을 때 cost가 더 적으면 받고 아니면 무시한다. (리펙토링 안함)