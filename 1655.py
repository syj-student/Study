import sys
import heapq

input = sys.stdin.readline

left_heap = list()
right_heap = list()

n = int(input())
for _ in range(n):
    x = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)
    else:
        heapq.heappush(right_heap, x)

    if right_heap and -left_heap[0] > right_heap[0]:
        a, b = -heapq.heappop(left_heap), -heapq.heappop(right_heap)
        heapq.heappush(left_heap, b)
        heapq.heappush(right_heap, a)
    
    print(-left_heap[0])
