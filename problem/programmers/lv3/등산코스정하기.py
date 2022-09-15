from collections import defaultdict, deque
import heapq

def solution(n, paths, gates, summits):
    def low_way():
        smallest = float('inf')
        heap = [(0, i, i) for i in summits]
        answer = [0, float('inf')]
        visited = [False] * (n+1)
        while heap:
            ity, now, f = heapq.heappop(heap)
            if not visited[now]:
                visited[now] = True
                for next_cost, next_node in m[now]:
                    tmp = max(next_cost, ity)
                    if next_node in gates:
                        if tmp < answer[1]:
                            answer = [f, tmp]
                            smallest = tmp
                        elif tmp == answer[1] and f < answer[0]:
                            answer[0] = f
                    if not visited[next_node] and tmp < smallest:
                        heapq.heappush(heap, (tmp, next_node, f))
        return answer

    gates = set(gates)
    m = defaultdict(list)
    for a, b, c in paths:
        m[a].append((c, b))
        m[b].append((c, a))
    return low_way()