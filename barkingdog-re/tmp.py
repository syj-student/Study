from sys import stdin

input = stdin.readline

n = int(input())
info = list(map(int, input().split()))
info.sort()

a = [1, 2, 3]
while a:
    n = a.pop()
    if n == 2:
        break
