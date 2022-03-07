from collections import defaultdict
import sys


def check(start):
    stack = [start]
    visited[start] = True
    while stack:
        now = stack.pop()
        for next_ in table[now]:
            if not visited[next_]:
                visited[next_] = True
                stack.append(next_)


n, m = map(int, sys.stdin.readline().split())
table = defaultdict(list)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    table[x].append(y)
    table[y].append(x)

answer = 0
visited = [False] * (n + 1)
for i in range(1, n+1):
    if not visited[i]:
        check(i)
        answer += 1
print(answer)
