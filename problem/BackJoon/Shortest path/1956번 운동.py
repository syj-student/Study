import sys
v, e = map(int, sys.stdin.readline().split())
inf = 100000000
dist = [[inf] * v for i in range(v)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    dist[a - 1][b - 1] = c
for k in range(v):
    for i in range(v):
        for j in range(v):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
result = inf
for i in range(v):
    result = min(result, dist[i][i])
if result == inf:
    print(-1)
else:
    print(result)