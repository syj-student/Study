import sys
import random
sys.setrecursionlimit(10 ** 6)


# input
n = int(input())
ret = list()
for __ in range(n):
	ret.append(int(sys.stdin.readline()))

ret.sort()
for i in ret:
	print(i)