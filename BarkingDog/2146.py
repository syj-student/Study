import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = list()
for _ in range(n):
    m.append(list(map(int, input().split())))
cost_m = [[None] * n for _ in range(n)]
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def make_island():
    ret = deque()
    def bfs(x, y, nb):
        dq = deque([(x, y)])
        cost_m[x][y] = [0, nb]
        while dq:
            x, y = dq.popleft()
            for a, b in move:
                nx = x + a
                ny = y + b
                if 0 <= nx < n and 0 <= ny < n:
                    if m[nx][ny] == 1 and cost_m[nx][ny] == None:
                        dq.append((nx, ny))
                        cost_m[nx][ny] = [0, nb]
                    elif m[nx][ny] == 0:
                        ret.append((x, y))

    island_no = 1
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1 and cost_m[i][j] == None:
                bfs(i, j, island_no)
                island_no += 1
    return ret

# def solve():
#     for i in range(n):
#         for j in range(n):                


dq = make_island()
answer = sys.maxsize
while dq:
    x, y = dq.popleft()
    for a, b in move:
        nx = x + a
        ny = y + b
        if 0 <= nx < n and 0 <= ny < n:
            if cost_m[nx][ny] == None:
                dq.append((nx, ny))
                cost_m[nx][ny] = [cost_m[x][y][0] + 1, cost_m[x][y][1]]
            elif cost_m[x][y][1] != cost_m[nx][ny][1]:
                answer = min(answer, cost_m[x][y][0] + cost_m[nx][ny][0])
print(answer)