import sys
import heapq

input = sys.stdin.readline
n = int(input())
deck = list()
for _ in range(n):
	heapq.heappush(deck, int(input()))
if len(deck) == 1:
	print(0)
else:
	acc = 0
	while True:
		a, b = heapq.heappop(deck), heapq.heappop(deck)
		heapq.heappush(deck, a+b)
		acc += a+b
		if len(deck) == 1:
			print(acc)
			break