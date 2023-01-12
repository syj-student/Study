from collections import defaultdict
from sys import stdin
import heapq

input = stdin.readline

cities, roads, _ = map(int, input().split())
m = defaultdict(list)
for _ in range(roads):
    a, b, c = map(int, input().split())
    m[a].append((c, b))
interview_loc = set(map(int, input().split()))

# def find_way(x):
#     heap = [(0, x)]
#     visited = [False] * (cities+1)
#     cost = [float('inf')] * (cities+1)
#     while heap:
#         now_cost, now_loc = heapq.heappop(heap)
#         if now_cost > cost[now_loc]:
#             continue
#         if now_loc in interview_loc:
#             return now_cost
#         visited[now_loc] = True
#         cost[now_loc] = now_cost
#         for next_cost, next_loc in m[now_loc]:
#             new_cost = next_cost + now_cost
#             if new_cost < cost[next_loc] and not visited[next_loc]:
#                 heapq.heappush(heap, (new_cost, next_loc))
#                 cost[next_loc] = new_cost

# answer = [0, 0]
# for i in range(1, cities+1):
#     c = find_way(i)
#     if c > answer[1]:
#         answer[0] = i
#         answer[1] = c
# print(*answer, sep="\n")

heap = list()
for i in range(1, cities+1):
    heap.append((0, i, i))
visited = [[False] * (cities+1) for _ in range(cities+1)]
cost = [[float('inf')] * (cities+1) for _ in range(cities+1)]
while heap:
    now_cost, now_loc, start_point = heapq.heappop(heap)
    if now_cost > cost[start_point][now_loc]:
        continue
    visited[start_point][now_loc] = True
    cost[start_point][now_loc] = now_cost
    if now_loc in interview_loc:
        continue
    for next_cost, next_loc in m[now_loc]:
        new_cost = next_cost + now_cost
        if new_cost < cost[start_point][next_loc] and not visited[start_point][next_loc]:
            heapq.heappush(heap, (new_cost, next_loc, start_point))
            cost[start_point][next_loc] = new_cost

# print(*cost, sep="\n")
answer_loc = 0
answer_cost = 0
for i in range(1, cities+1):
    now_cost = float('inf')
    for j in interview_loc:
        now_cost = min(now_cost, cost[i][j])
    if now_cost > answer_cost:
        answer_loc = i
        answer_cost = now_cost
print(answer_loc)
print(answer_cost)
