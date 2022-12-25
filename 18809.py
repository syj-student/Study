import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
from pprint import pprint

input = sys.stdin.readline

a, b, c, d = map(int, input().split())
graph = [list() for _ in range(a)]
can_ground = list()
answer = 0
for i in range(a):
    graph[i] = list(map(int, input().split()))
    for j in range(b):
        if graph[i][j] == 2:
            can_ground.append((i, j))



move = ((1, 0), (-1, 0), (0, 1), (0, -1))
def dfs(dq=set(), start=0, red_cnt=0, green_cnt=0):
    global answer, move, c, d, can_ground
    if red_cnt == c and green_cnt == d:
        # print(dq, red_cnt, green_cnt)
        new_graph = deepcopy(graph)
        new_answer = 0
        in_dq = dq.copy()
        mydq = deque(dq)
        while mydq:
            x, y, val, turn = mydq.popleft()
            if (x, y, val, turn) not in in_dq:
                continue
            if new_graph[x][y] in (1, 2):
                new_graph[x][y] = (val, turn)
            elif new_graph[x][y] in ((True, turn), (False, turn)):
                new_answer += 1
                new_graph[x][y] = f'flower {turn}'
                continue
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < a and 0 <= ny < b and new_graph[nx][ny] in (1, 2):
                    tmp = (nx, ny, val, turn+1)
                    if tmp not in in_dq:
                        if (nx, ny, not val, turn+1) in in_dq:
                            new_graph[nx][ny] = f'FLOWER {turn+1}'
                            in_dq.remove((nx, ny, not val, turn+1))
                            new_answer += 1
                            continue
                        in_dq.add(tmp)
                        mydq.append(tmp)
        # if new_answer == 6:
        #     for l in new_graph:
        #         for k in l:
        #             print("{0:<10}".format(str(k)), end='')
        #         print()
        answer = max(answer, new_answer)
        return
    
    for i in range(start, len(can_ground)):
        for letter in (True, False):
            x, y = can_ground[i]
            if letter == True and red_cnt < c:
                dq.add((x, y, letter, 0))
                dfs(dq, i+1,red_cnt+1, green_cnt)
                dq.discard((x, y, letter, 0))
            elif letter == False and green_cnt < d :
                dq.add((x, y, letter, 0))
                dfs(dq, i+1,red_cnt, green_cnt+1)
                dq.discard((x, y, letter, 0))


    
dfs()


print(answer)