import sys
n = int(input())
stack = list()
ret = list()
cnt = 1
flag = 0
for __ in range(n):
	x = (int(sys.stdin.readline()))
	while cnt <= x:
		stack.append(cnt)
		ret.append('+')
		cnt += 1
	if stack[-1] == x:
		stack.pop()
		ret.append('-')
	else:
		print('NO')
		flag = 1
		break

if flag == 0:
	for i in ret:
		print(i)