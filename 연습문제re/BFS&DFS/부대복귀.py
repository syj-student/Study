from collections import defaultdict
import heapq

def solution(n, roads, sources, destination):
    m = defaultdict(set)
    for a, b in roads:
        m[a].add(b)
        m[b].add(a)
    
    answer = list()
    cost = [float('inf')] * (n+1)
    heap = [(0, destination)]
    while heap:
        now_cost, now = heapq.heappop(heap)
        if cost[now] < now_cost:
            continue
        cost[now] = now_cost
        for next_node in m[now]:
            next_cost = now_cost + 1
            if next_cost < cost[next_node]:
                cost[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))
    for i in sources:
        answer.append(
            cost[i] if cost[i] != float('inf') else -1
        )
    return answer

print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))