import sys

cnt, target = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
left = 0
answer = sys.maxsize
total, flag = 0, 0
for right in range(cnt):
    total += lst[right]
    while total >= target:
        answer = min(answer, right - left + 1)
        if answer == 1:
            flag = 1
            break
        total -= lst[left]
        left += 1
    if flag:
        break

print(0 if answer == sys.maxsize else answer)
