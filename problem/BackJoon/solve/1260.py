from collections import defaultdict, deque
import sys

a, b, c = map(int, sys.stdin.readline().split())
table = defaultdict(list)
for _ in range(b):
    x, y = map(int, sys.stdin.readline().split())
    table[x].append(y)
    table[y].append(x)
for i in table:
    table[i].sort()
visited = [False] * (a + 1)


def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in table[n]:
        if not visited[i]:
            dfs(i)
# def dfs():
#     visited = [False] * (a + 1)
#     stack = deque([c])
#     while stack:
#         now = stack.pop()
#         if not visited[now]:
#             visited[now] = True
#             print(now, end=' ')
#             for n in table[now]:
#                 if not visited[n]:
#                     dfs


def bfs():
    visited = [False] * (a + 1)
    stack = deque([c])
    while stack:
        now = stack.popleft()
        if not visited[now]:
            visited[now] = True
            print(now, end=' ')
            for n in table[now]:
                if not visited[n]:
                    stack.append(n)


dfs(c)
print()
bfs()
