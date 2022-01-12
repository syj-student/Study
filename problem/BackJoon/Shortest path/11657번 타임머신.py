import sys
from collections import defaultdict, deque

n, m = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    if edge[u]:
        flag = True
        for i in range(len(edge[u])):
            if edge[u][i][0] == v:
                if edge[u][i][1] > w:
                    edge[u][i][1] = w
            flag = flag
            break
        if flag:
            edge[u].append([v, w])
    else:
        edge[u].append([v, w])


def SPFA():
    answer = [float('inf')] * (n + 1)
    cycle = [0] * (n + 1)
    in_queue = [0] * (n + 1)
    answer[1] = 0
    q = deque([1])
    while q:
        now = q.popleft()
        cost = answer[now]
        cycle[now] += 1
        if cycle[now] >= n:
            return False
        in_queue[now] = False
        for next_node, next_cost in edge[now]:
            total_cost = cost + next_cost
            if total_cost < answer[next_node]:
                answer[next_node] = total_cost
                if not in_queue[next_node]:

                    q.append(next_node)
                    in_queue[next_node] = True
    return answer[2:]


def answer_print(lst):
    if lst:
        for i in range(len(lst)):
            if lst[i] == float('inf'):
                lst[i] = -1
        return lst
    return [-1]

print(*answer_print(SPFA()), sep='\n', end='')
