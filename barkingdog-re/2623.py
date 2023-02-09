from sys import stdin
from collections import deque

input = stdin.readline

x, y = map(int, input().split())
connections = [0] * (x+1)
graph = dict()
for i in range(1, x+1):
    graph[i] = set()    

for _ in range(y):
    info = list(map(int, input().split()))
    for now in range(1, len(info)-1):
        if info[now+1] not in graph[info[now]]:
            graph[info[now]].add(info[now+1])
            connections[info[now+1]] += 1
queue = deque()
for i in range(1, x+1):
    if connections[i] == 0:
        queue.append(i)

answer = list()
while queue:
    now = queue.popleft()
    answer.append(now)
    for nxt in graph[now]:
        connections[nxt] -= 1
        if connections[nxt] == 0:
            queue.append(nxt)
if len(answer) == x:
    print(*answer, sep='\n')
else:
    print(0)