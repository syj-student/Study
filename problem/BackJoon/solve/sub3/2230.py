import itertools
import sys

input = sys.stdin.readline
lst = list()
m, n = map(int, input().split())
for _ in range(m):
	lst.append(int(input()))
lst.sort()
answer = float('inf')
left = 0
right = 1
while right < len(lst):
	tmp = lst[right] - lst[left]
	if tmp == n:
		answer = tmp
		break
	elif tmp < n:
		right += 1
	else:
		left += 1
		answer = min(answer, tmp)
print(answer)