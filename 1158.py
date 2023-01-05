from sys import stdin

input = stdin.readline

x, y = map(int, input().split())
y -=1
lst = [i for i in range(1, x+1)]
answer =list()
now = y
answer.append(lst.pop(now))
while lst:
    now += y
    while now >= len(lst):
        now -= len(lst)
    answer.append(lst.pop(now))
print("<", end="")
print(*answer, sep=", ", end=">")