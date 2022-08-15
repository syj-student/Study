import sys
sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline
n, b, c = map(int, input().split())
m = dict()
m[0] = 1
def solve(n, b, c):
    global m
    if n in m:
        return m[n]
    else:
        m[n] = solve(n//b, b, c) + solve(n//c, b, c)
        return m[n]
print(solve(n, b, c))