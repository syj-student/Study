from collections import defaultdict
import sys

sys.setrecursionlimit(2*10**9)

def solution(a, edges):
    g = defaultdict(set)
    for e in edges:
        g[e[0]].add(e[1])
        g[e[1]].add(e[0])
    answer = 0
    visited = [False] * len(a)
    def dfs(now_node):
        nonlocal a, g, answer, visited
        visited[now_node] = True
        now_acc = a[now_node]
        for next_node in g[now_node]:
            if not visited[next_node]:
                now_acc += dfs(next_node)
        answer += abs(now_acc)
        return now_acc
    if dfs(0):
        return -1
    return answer

print(solution(	[-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))