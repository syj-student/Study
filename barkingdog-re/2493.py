from sys import stdin
from collections import deque
input = stdin.readline


stack = deque()
x = int(input())
answer = [0] * x
lst = map(int, input().split())
for i, now in enumerate(lst):
    while stack and stack[-1][1] < now:
        stack.pop()
    if stack:
        answer[i] = stack[-1][0]+1
    stack.append((i, now))
print(*answer, sep=' ')