from sys import stdin
from collections import defaultdict
import heapq

input = stdin.readline

m = defaultdict(list)
a, b, c = map(int, input().split())
for _ in range(b):
    x, y, z = map(int, input().split())
    m[x].append((z, y))



def find_way(start):
    visited = [False] * (a+1)
    cost = [float('inf')] * (a+1)
    heap = [(0, start)]
    while heap:
        now_cost, now_loc = heapq.heappop(heap)
        if cost[now_loc] < now_cost:
            continue
        cost[now_loc] = now_cost
        visited[now_loc] = True
        for next_cost, next_loc in m[now_loc]:
            new_cost = next_cost + now_cost
            if new_cost < cost[next_loc] and not visited[next_loc]:
                heapq.heappush(heap, (new_cost, next_loc))
                cost[next_loc] = new_cost
    return cost


ret_home = find_way(c)
answer = 0
for i in range(1, a+1):
    if i == c:
        continue
    answer = max(answer, find_way(i)[c] + ret_home[i])
print(answer)
