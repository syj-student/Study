import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
a, b, c = map(int, input().split())
m = defaultdict(list)
for _ in range(b):
    x, y, z = map(int, input().split())
    m[x].append((z, y))

def solve(now):
    global m
    visited = [False] * (a+1)
    dist = [sys.maxsize] * (a+1)
    heap = [(0, now)]
    visited[now] = True
    dist[now] = 0
    while heap:
        cur_cost, cur = heapq.heappop(heap)
        if cur_cost > dist[cur]:
            continue
        visited[cur] = True
        for next_cost, next_node in m[cur]:
            new_cost = next_cost + cur_cost
            if new_cost < dist[next_node] and not visited[next_node]:
                heapq.heappush(heap, (new_cost, next_node))
                dist[next_node] = new_cost
    return dist


answer = solve(c)
ret = 0
for i in range(1, a+1):
    if i == c:
        continue
    ret = max(ret, answer[i] + solve(i)[c])
print(ret)