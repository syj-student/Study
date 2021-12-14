# import sys
# import heapq

# n = int(sys.stdin.readline())

# heap = list()
# for _ in range(n):
# 	x = int(sys.stdin.readline())
# 	if x == 0:
# 		if heap:
# 			print(heapq.heappop(heap))
# 		else:
# 			print(0)
# 	else:
# 		heapq.heappush(heap, x)

import sys
import heapq

n = int(sys.stdin.readline())

heap = list()
for _ in range(n):
	x = int(sys.stdin.readline())
	if x == 0 and heap:
		print(heapq.heappop(heap))
	elif x == 0 and not heap:
		print(0)
	else:
		heapq.heappush(heap, x)