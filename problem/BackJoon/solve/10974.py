import sys
import itertools

n = int(sys.stdin.readline())
lst = [i for i in range(1, n+1)]
cases = itertools.permutations(lst, n)
for i in cases:
    print(*i)
