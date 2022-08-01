import sys
import heapq
from collections import deque

input = sys.stdin.readline
i, j = map(int, input().split())
m = list()
for _ in range(i):
    m.append(list(input().rstrip()))
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visited = [[[0, 0] for _ in range(j)] for _ in range(i)]
visited[0][0][0] = 1
h = [(1, 0, 0, 0)]
while h:
    _, z, x, y, = heapq.heappop(h)
    if x == i-1 and y == j-1:
        print(visited[x][y][z])
        break
    for a, b in move:
        dx = x + a
        dy = y + b
        if 0 <= dx < i and 0 <= dy < j:
            if m[dx][dy] == '1' and z == 0:
                visited[dx][dy][1] = visited[x][y][0] + 1
                heapq.heappush(h, (visited[x][y][0] + 1, 1, dx, dy,))
            elif m[dx][dy] == '0'  and visited[dx][dy][z] == 0:
                visited[dx][dy][z] = visited[x][y][z] + 1
                heapq.heappush(h, (visited[x][y][z] + 1, z, dx, dy))
else:
    print(-1)