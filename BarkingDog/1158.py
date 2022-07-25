import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
m -= 1
l = deque([i for i in range(1, n+1)])
idx = m
answer = list()
while l:
    while idx >= len(l):
        idx -= len(l)
    answer.append(str(l[idx]))
    del l[idx]
    idx += m
answer = ", ".join(answer)
print(f'<{answer}>')