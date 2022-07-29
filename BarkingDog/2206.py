import sys
import heapq

input = sys.stdin.readline
i, j = map(int, input().split())
m = list()
for _ in range(i):
    m.append(list(input().rstrip()))
h = [(0, 0, 0)]
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visited = [[[0, 0]] * j for _ in range(i)]
visited[0][0][0] = 1
while h:
    x, y, z = heapq.heappop(h)
    if x == i-1 and y == j-1:
        print(visited[x][y][z])
        break
    for a, b in move:
        dx = x + a
        dy = y + b
        if 0 <= dx < i and 0 <= dy < j:
            if m[dx][dy] == '1' and not z == 0:
                visited[dx][dy][1] = visited[x][y][0] + 1
                heapq.heappush(h, (dx, dy, 1))
            elif m[dx][dy] == '0'  and visited[dx][dy][z] == 0:
                visited[dx][dy][z] = visited[x][y][z] + 1
                heapq.heappush(h, (dx, dy, z))
else:
    print(-1)