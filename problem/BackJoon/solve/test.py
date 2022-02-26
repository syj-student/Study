import itertools
import sys

n = int(sys.stdin.readline())
nums = [str(i) for i in range(10)]
es = sys.stdin.readline().strip().split()
a = nums[:n+1]
b = nums[-n-1:]
a = itertools.permutations(a)
b = itertools.permutations(b)
