import heapq

from collections import deque
from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    _, idx = map(int, stdin.readline().split())
    ordered = list(map(int, stdin.readline().split()))
    deq = deque(enumerate(ordered))
    ordered.sort()
    cnt = 1
    while True:
        no = ordered.pop()
        while deq[0][1] != no:
            deq.rotate(-1)
        x, y = deq.popleft()
        if x == idx:
            print(cnt)
            break
        cnt += 1
