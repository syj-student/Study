from collections import deque
import sys

# input n
n = int(sys.stdin.readline())

# solve
dq = deque()
for __ in range(n):
	ipt = list(sys.stdin.readline().split())
	if ipt[0] == 'push':
		tmp = int(ipt[1])
		dq.append(tmp)
	elif ipt[0] == 'pop':
		if not dq	: print(-1)
		else		: print(dq.popleft())
	elif ipt[0] == 'size':
		print(len(dq))
	elif ipt[0] == 'empty':
		if	dq	: print(0)
		else	: print(1)
	elif ipt[0] == 'front':
		if	not dq	: print(-1)
		else		: print(dq[0])
	elif ipt[0] == 'back':
		if	not dq	: print(-1)
		else		: print(dq[-1])