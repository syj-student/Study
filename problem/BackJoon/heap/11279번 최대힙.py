import sys
import heapq

n = int(input())

lst = list()
for _ in range(n):
	x = int(sys.stdin.readline())
	if x == 0:
		if lst:
			print(heapq.heappop(lst)[1])
		else:
			print(0)
	else:
		heapq.heappush(lst, (-x, x))