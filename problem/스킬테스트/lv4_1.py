import heapq

from collections import defaultdict
from itertools import combinations

def solution(n, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    costs = [[float('inf')] * (n+1) for _ in range(n+1)]
    def short_way(start):
        nonlocal costs
        costs[start][start] = 0
        heap = [(0, start)]
        while heap:
            now_cost, now = heapq.heappop(heap)
            if costs[start][now] < now_cost:
                continue
            for nxt in graph[now]:
                new_cost = 1 + now_cost
                if costs[start][nxt] > new_cost:
                    heapq.heappush(heap, (new_cost, nxt))
                    costs[start][nxt] = new_cost
    for i in range(1, n+1):
        short_way(i)

    print(*costs, sep="\n")
    answer, cases = 0, combinations(range(1, n+1), 3)
    for x, y, z in cases:
        answer = max(answer, costs[x][y] + costs[y][z] + costs[x][z])
    return answer // 3
print(solution(4, [[1, 2], [2, 3], [3, 4]]))