import sys
import heapq

input = sys.stdin.readline
k = int(input())
p = list()
n = list()
acc = 0
for _ in range(k):
    x = int(input())
    if x == 1:
        acc += 1
    elif x > 1:
        heapq.heappush(p, -x)
    else:
        heapq.heappush(n, x)


while p:
    first = heapq.heappop(p)
    if p:
        second = heapq.heappop(p)
        acc += first * second
    else:
        acc += -first

while n:
    first = heapq.heappop(n)
    if n:
        second = heapq.heappop(n)
        acc += first * second
    else:
        acc += first

print(acc)
