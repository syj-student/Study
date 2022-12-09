from sys import stdin

input = stdin.readline
x, y = map(int, input().split())
houses = list()
for i in range(x):
    houses.append(int(input()))

houses.sort()
start, end = 1, houses[-1]

answer = 0
while start <= end:
    gap = (start + end) // 2
    now = houses[0]
    cnt = 1
    for i in range(1, len(houses)):
        if houses[i] - now >= gap:
            cnt += 1
            now = houses[i]
    if cnt >= y:
        answer = max(answer, gap)
        start = gap + 1
    else:
        end = gap -1
print(answer)