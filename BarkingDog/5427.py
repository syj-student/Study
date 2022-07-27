import sys
from pprint import pprint
from collections import deque

input = sys.stdin.readline

def fire(m):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    dest = list()
    q = deque()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "*":
                q.appendleft((i, j, "*"))
                visited[i][j] = True
            elif m[i][j] == "@":
                m[i][j] = "."
                q.append((i, j, "@"))
                visited[i][j] = True
    ti = 0
    while q:
        ti += 1
        temp = deque()
        while q:
            x, y, c = q.popleft()
            for a, b in zip(dx, dy):
                nx = x + a
                ny = y + b
                if 0 <= nx < len(m) and 0 <= ny < len(m[0]):
                    if not visited[nx][ny] and m[nx][ny] == ".":
                        visited[nx][ny] = True
                        temp.append((nx, ny, c))
                elif c == "@":
                    return ti
        q = temp
    return "IMPOSSIBLE"
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    visited = [[False] * x for _ in range(y)]
    m = list()
    for i in range(y):
        m.append(list(input().rstrip()))
    print(fire(m))