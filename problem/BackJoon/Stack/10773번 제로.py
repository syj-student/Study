from collections import deque
import sys

input = sys.stdin.readline

# input times
N = int(input().strip())

# loop
stack = deque([])
for __ in range(N):
	x = int(input().strip())
	if x:
		stack.append(x)
	else:
		stack.pop()

# print
ret = 0
for i in stack:
	ret += i
print(ret)