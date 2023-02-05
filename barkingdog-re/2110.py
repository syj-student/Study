from sys import stdin

input = stdin.readline

x, y = map(int, input().split())
info = [0] * x
for i in range(x):
    info[i] = int(input())
info.sort()

def is_valid_distance(distance):
    global info

    cnt = 1
    last_location = info[0]
    for i in range(1, len(info)):
        if info[i] - last_location  >= distance:
            cnt += 1
            last_location = info[i]
    return cnt

answer = 0
left, right = 0, info[-1] - info[0]
while left <= right:
    mid = (left + right) // 2
    if is_valid_distance(mid) < y:
        right = mid - 1
    else:
        answer = max(answer, mid)
        left = mid + 1
print(answer)

