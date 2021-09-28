import heapq
import random

head = list()

for _ in range(100):
	heapq.heappush(head, random.randrange(100))

print(type(head))