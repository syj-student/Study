from sys import stdin
from bisect import bisect_left

input = stdin.readline

x, y = map(int, input().split())
down_up = list()
up_down = list()
for i in range(x):
    if i % 2:
        up_down.append(int(input()))
    else:
        down_up.append(int(input()))
down_up.sort()
up_down.sort()

answer = float('inf')
answer_cnt = 1

for height in range(1, y+1):
    crash = x - (bisect_left(down_up, height) + bisect_left(up_down, y+1 - height))
    if crash < answer:
        answer = crash
        answer_cnt = 1
    elif crash == answer:
        answer_cnt += 1




print(answer, answer_cnt)

