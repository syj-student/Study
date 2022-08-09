import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)
answer, acc = 0, 0
for _ in range(n):
    now = heapq.heappop(heap)
    answer += acc + now
    acc += now
print(answer)