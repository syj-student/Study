import sys
import bisect

n = int(sys.stdin.readline())
lst = list()
for _ in range(n):
	x = int(sys.stdin.readline())
	i = bisect.bisect_left(lst, x)
	lst.insert(i, x)
	length = len(lst)
	if length % 2:
		print(lst[length//2])
	else:
		print(min(lst[length//2], lst[(length//2) - 1]))