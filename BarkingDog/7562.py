from collections import deque
import sys

input = sys.stdin.readline

def bfs(start: list, dest: list) -> int:
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    m[start[0]][start[1]] = 0
    dq = deque([[0] + start])
    while dq:
        cost, x, y = dq.popleft()
        for a, b in zip(dx, dy):
            nx = x + a
            ny = y + b
            if 0 <= nx < l and 0 <= ny < l and cost + 1 < m[nx][ny]:
                if nx == dest[0] and ny == dest[1]:
                    return cost + 1
                dq.append((cost+1, nx, ny))
                m[nx][ny] = cost + 1
    return m[dest[0]][dest[1]]


n = int(input())
for _ in range(n):
    l = int(input())
    start = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    if start[0] == dest[0] and start[1] == dest[1]:
        print(0)
        continue
    m = [[sys.maxsize for _ in range(l)] for _ in range(l)]
    print(bfs(start, dest))