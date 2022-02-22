import copy
from collections import defaultdict
from sys import maxsize


def solution(n, start, end, roads, traps):
    og_graph = defaultdict(list)
    re_graph = defaultdict(list)
    traps = set(traps)
    for l in roads:
        og_graph[l[0]].append((l[1], l[2]))
        re_graph[l[1]].append((l[0], l[2]))
    toggle = {True: og_graph, False: re_graph}
    answer = maxsize
    stack = [(start, 0, defaultdict(int), True)]
    while stack:
        now, cost, visited, graph = stack.pop()
        if now == end:
            answer = min(answer, cost)
            continue
        visited[now] += 1
        for next_node, next_cost in toggle[graph][now]:
            if visited[next_node] < n:
                next_graph = not graph if next_node in traps and not (
                    visited[next_node] % 2) else graph
                stack.append((next_node, cost + next_cost,
                             copy.deepcopy(visited), next_graph))

    return answer


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
