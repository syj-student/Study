import sys
from collections import defaultdict

member, n = map(int, sys.stdin.readline().split())
tree = defaultdict(list)
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
visited = [False] * member


def dfs(start, depth=0):
    if depth >= 4:
        print(1)
        exit(0)
    if not visited[start]:
        visited[start] = True
        for i in tree[start]:
            if not visited[i]:
                dfs(i, depth + 1)
        visited[start] = False


for i in range(member):
    dfs(i, 0)
print(0)
