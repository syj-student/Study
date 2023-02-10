import heapq

from collections import defaultdict

def solution(n, edge):

    def dfs(start=1):
        nonlocal graph
        costs = [float('inf')] * (n+1)
        heap = [(start, 0)]
        while heap:
            now, cost = heapq.heappop(heap)
            if costs[now] < cost:
                continue
            costs[now] = cost
            for nxt in graph[now]:
                new_cost = cost + 1
                if costs[nxt] > new_cost:
                    heapq.heappush(heap, (nxt, new_cost))    
                    costs[nxt] = new_cost
        return costs
    graph = defaultdict(list)
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    # find far node
    random, far, far_node = dfs(), 0, list()
    for i in range(1, n+1):
        if random[i] != float('inf'):
            if far < random[i]:
                far, far_node = random[i], [i]
            elif far == random[i]:
                far_node.append(i)

    # # farthest node
    # answer = 0
    # for node in far_node:
    #     farther = dfs(node)
    #     for cost in farther:
    #         if cost != float('inf'):
    #             answer = max(answer, cost)
    return len(far_node)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))