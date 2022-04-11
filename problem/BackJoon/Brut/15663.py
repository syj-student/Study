import sys
import itertools

n, m = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
cases = sorted(set(itertools.permutations(lst, m)))
for case in cases:
	print(*case)
