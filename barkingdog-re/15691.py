from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(200000000)
input = stdin.readline

x, y, z = map(int, input().split())
tree = defaultdict(list)
for _ in range(x-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

answer_table = [0] * (x+1)
def dfs(now, parent=0):
    global answer_table
    answer = 1
    for nxt in tree[now]:
        if parent == nxt:
            continue
        answer += dfs(nxt, now)
    answer_table[now] = answer
    return answer


dfs(y)
for _ in range(z):
    now = int(input())
    print(answer_table[now])