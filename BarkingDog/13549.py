import sys
import heapq
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
if n == m:
    print(0)
    exit(0)
board = [sys.maxsize] * (100001)
heap = [(0, n)]
board[n] = 0
while heap:
    cost, now = heapq.heappop(heap)
    if now == sys.maxsize:
        continue
    if now == m:
        print(cost)
        break
    b, f, t = now-1, now+1, now*2
    if 0 <= t < 100001 and cost < board[t]:
        board[t] = cost
        heapq.heappush(heap, (cost, t))
    if 0 <= b < 100001 and cost+1 < board[b]:
        board[b] = cost+1
        heapq.heappush(heap, (cost+1, b))
    if 0 <= f < 100001 and cost+1 < board[f]:
        board[f] = cost+1
        heapq.heappush(heap, (cost+1, f))
