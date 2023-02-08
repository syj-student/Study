from sys import stdin
from collections import defaultdict

input = stdin.readline

def tree_check(tree, n):
    visited = [False] * (n+1)
    cnt = 0
    for start in range(1, n+1):
        if visited[start]:
            continue
        stack = [(start, 0)]
        circular = False
        while stack:
            now, prev = stack.pop()
            visited[now] = True
            for nxt in tree[now]:
                if nxt == now or nxt == prev:
                    continue
                if visited[nxt]:
                    circular = True
                    continue
                stack.append((nxt, now))
        if not circular:
            cnt += 1
    return cnt
i = 1
while True:

    n, y = map(int, input().split())
    if n == y == 0:
        exit(0)

    tree = defaultdict(list)
    for _ in range(y):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    count = tree_check(tree, n)
    if count == 0:
        print(f'Case {i}: No trees.')
    elif count == 1:
        print(f'Case {i}: There is one tree.')
    else:
        print(f'Case {i}: A forest of {count} trees.')
    i += 1
