from sys import stdin
from itertools import combinations
from copy import deepcopy
from collections import deque

a, b, c, d = map(int, stdin.readline().split())
if c > d:
    c, d = d, c

move = ((0, -1), (0, 1), (-1, 0), (1, 0))
l = [0] * a
can_start = list()
answer = float('-inf')

checker = True

for i in range(a):
    l[i] = list(map(int, stdin.readline().split()))
    for j in range(b):
        if l[i][j] == 2:
            can_start.append((i, j))
for i in combinations(can_start, c+d):
    for j in combinations(i, c):
        copy_map = deepcopy(l)
        cases = set(i)
        answer_cnt = 0
        in_q = set()

        turn = 10
        for x, y in j:
            copy_map[x][y] = ('G', turn)
            cases.remove((x, y))
            in_q.add((x, y, 'G', turn))
        for x, y in cases:
            copy_map[x][y] = ('R', turn)
            in_q.add((x, y, 'R', turn))
        while in_q:
            tmp = set()
            while in_q:
                x, y, color, turn = in_q.pop()
                for dx, dy in move:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < a and 0 <= ny < b and copy_map[nx][ny] != 0:
                        if copy_map[nx][ny] in {1, 2}:
                            copy_map[nx][ny] = (color, turn)
                            tmp.add((nx, ny, color, turn+1))
                        elif copy_map[nx][ny][1] == turn:
                            if color == 'R' and copy_map[nx][ny][0] == 'G':
                                tmp.discard((nx, ny, 'G', turn+1))
                                tmp.discard((nx, ny, 'R', turn+1))
                                answer_cnt += 1
                                copy_map[nx][ny] = 0
                            elif color == 'G' and copy_map[nx][ny][0] == 'R': 
                                tmp.discard((nx, ny, 'R', turn+1))
                                tmp.discard((nx, ny, 'G', turn+1))
                                answer_cnt += 1
                                copy_map[nx][ny] = 0
            in_q = tmp
        # print(*copy_map, sep='\n')
        # print()

        answer = max(answer, answer_cnt)

print(answer)

