import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n, m = map(int, input().split())
costs = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    costs[a].append((b, c))
answer = [sys.maxsize] * (n+1)
answer[1] = 0

dq = deque([1])
cyc = [0] * (n+1)
inq = [False] * (n+1)
inq[1] = True
while dq:
    now = dq.popleft()
    inq[now] = False
    for v, w in costs[now]:
        if answer[v] > answer[now] + w:
            answer[v] = answer[now] + w
            if not inq[v]:
                dq.append(v)
                inq[v] = True
                cyc[v] += 1
            if cyc[v] == n:
                print(-1)
                exit(0)

for i in range(2, n+1):
    print(-1) if answer[i] == sys.maxsize else print(answer[i])