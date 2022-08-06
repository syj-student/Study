import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    g = list(map(int, input().split()))
    answer = 0
    now = g[-1]
    for i in range(n-2, -1, -1):
        if g[i] < now:
            answer += now - g[i]
        else:
            now = g[i]
    print(answer)