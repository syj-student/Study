import sys

input = sys.stdin.readline

x, y = map(int, input().split())
lans = list()

for _ in range(x):
    x = int(input())
    lans.append(x)
left, right = 1, max(lans)
answer = 0
while left < right:
    mid = (left + right) // 2
    tmp = 0
    for i in lans:
        tmp += i // mid
    if tmp < y:
        right = mid-1
    elif tmp >= y:
        left = mid+1
        answer = max(answer, mid)
print(answer)


