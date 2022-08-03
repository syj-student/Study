import sys
from collections import deque


input = sys.stdin.readline
x, y = map(int, input().split())
m = list()
for _ in range(x):
    m.append(list(map(int, input().split())))

def check_map():
    visited = [[False] * y for _ in range(x)]
    def dfs(a, b):
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dq = deque([(a, b)])
        while dq:
            k, z = dq.popleft()
            visited[k][z] = True
            for dk, dz in move:
                nk = dk + k
                nz = dz + z
                if 0 <= nk < x and 0 <= nz < y and not visited[nk][nz] and m[nk][nz] != 0:
                    visited[nk][nz] = True
                    dq.append((nk, nz))
        return 1
    
    island = 0
    for i in range(x):
        for j in range(y):
            if not visited[i][j] and m[i][j] != 0:
                island += dfs(i, j)
            if island >= 2:
                return False
    return True

def meltdown():
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    melt_points = deque()
    for i in range(x):
        for j in range(y):
            if m[i][j] != 0:
                p = 0
                for a, b in move:
                    nx = i + a
                    ny = j + b
                    if 0 <= nx < x and 0 <= ny < y and m[nx][ny] == 0:
                        p += 1
                melt_points.append((i, j, p))
    for i, j, p in melt_points:
        if m[i][j] <= p:
            m[i][j] = 0
        else:
            m[i][j] -= p
    return 1
answer = 0
while check_map():
    answer += meltdown()
print(answer)


