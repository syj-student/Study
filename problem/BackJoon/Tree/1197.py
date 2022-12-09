from collections import defaultdict
from sys import stdin
import heapq

input = stdin.readline
x, y = map(int, input().split())
g = defaultdict(list)
for _ in range(y):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
visited = [False] * (x + 1)
heap = [(0, 1)]
answer = 0
while heap:
    cost, now = heapq.heappop(heap)
    if not visited[now]:
        visited[now] = True
        answer += cost
        for b, c in g[now]:
            if not visited[b]:
                heapq.heappush(heap, (c, b))
print(answer)

