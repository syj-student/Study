import heapq

from sys import stdin
from collections import deque

input = stdin.readline
x, y = map(int, input().split())
graph = dict()
for i in range(1, x+1):
    graph[i] = list()
connection = [0] * (x+1)
for _ in range(y):
    a, b = map(int, input().split())
    graph[a].append(b)
    connection[b] += 1

answer = list()
solved = [False] * (x+1)
for i in range(1, x+1):
    if not solved[i] and connection[i] == 0:
        heap = [i]
        while heap:
            now = heapq.heappop(heap)
            answer.append(now)
            solved[now] = True
            for nxt in graph[now]:
                connection[nxt] -= 1
                if connection[nxt] == 0:
                    heapq.heappush(heap, nxt)
print(*answer)