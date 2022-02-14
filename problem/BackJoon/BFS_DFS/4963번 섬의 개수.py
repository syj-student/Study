import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

while True:
    x, y = map(int, input().split())
    if 0 == x == y:
        break

    island = 0
    table = list()
    for _ in range(y):
        table.append(list(map(int, input().split())))
    for i in range(y):
        for j in range(x):
            if table[i][j] == 1:
                stack = [[i, j]]
                while stack:
                    a, b = stack.pop()
                    table[a][b] = -1
                    for k in range(8):
                        da = a + dx[k]
                        db = b + dy[k]
                        if 0 <= da < y and 0 <= db < x and table[da][db] == 1:
                            stack.append([da, db])
                island += 1
    print(island)
