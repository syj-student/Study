import heapq

a = int(input())
heap = list()
for _ in range(a):
    x = int(input())
    heapq.heappush(heap, x)

answer = 0
while len(heap) > 1:
    now = heapq.heappop(heap)+heapq.heappop(heap)
    answer += now
    heapq.heappush(heap, now)

print(answer)