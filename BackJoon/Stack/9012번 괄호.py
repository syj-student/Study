from collections import deque
import sys

input = sys.stdin.readline

# input times
N = int(input().strip())

# loop
stack = deque()
ret = list()
for __ in range(N):
	tmp = list(input().strip())
	flag = True
	for each in tmp:
		if each == '(':
			stack.append('(')
		elif not stack and each == ')':
			flag = False
			ret.append('NO')
			break
		else:
			stack.pop()
	if not stack and flag:
		ret.append('YES')
	elif flag:
		ret.append('NO')
	tmp.clear()
	stack.clear()

# print
for i in ret:
	print(i)