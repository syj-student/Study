from collections import defaultdict

def solution(n, lighthouse):
    graph = defaultdict(set)
    for f, t in lighthouse:
        graph[f].add(t)
        graph[t].add(f)
    visited = {}
    cnt = 0
    while len(visited) < n:
        must_on = set()
        for i in graph.keys():
            if len(graph[i]) == 1:
                must_on.add(graph[i].pop())
                del graph[i]
        for now in must_on:
            for r in graph[now]:
                visited.add(r)
                del graph[r]
            visited.add(now)
            graph[now]
        cnt += len(must_on)
    return cnt

# print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))
# print(solution(4, [[1, 2], [2, 3], [3, 4]]))