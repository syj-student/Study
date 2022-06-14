import itertools
import sys

input = sys.stdin.readline

lst = input().rstrip()
if len(lst) == 0:
	print(0)
else:
	s = set()
	for i in range(1, len(lst)+1):
		start = 0
		end = i
		while end <= len(lst):
			s.add(lst[start:end])
			start += 1
			end += 1
	print(len(s))
