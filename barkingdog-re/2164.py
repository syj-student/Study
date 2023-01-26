from sys import stdin
from collections import deque
input = stdin.readline

x = int(input())
dq = deque([i for i in range(1, x+1)])
while len(dq) > 1:
    dq.popleft()
    dq.rotate(-1)
print(dq[-1])