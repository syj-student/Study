
from sys import stdin

input = stdin.readline
x, y = map(int, input().split())
lst = list(map(int, set(input().split())))
lst.sort()
x = len(lst)
if y == 0:
    exit(0)
def dfs(now=list(),start=0, depth=0):
    global x, y
    if depth == y:
        print(" ".join(map(str, now)))
        return
    for i in range(start, x):
        now.append(lst[i])
        dfs(now, i, depth+1)
        now.pop()

dfs()