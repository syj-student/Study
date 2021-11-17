from collections import deque
import sys

# input n
n = int(sys.stdin.readline())

# solve
dq = deque()
for __ in range(n):
	ipt = list(sys.stdin.readline().split())
	if ipt[0] == 'push_back':
		tmp = int(ipt[1])
		dq.append(tmp)
	elif ipt[0] == 'push_front':
		tmp = int(ipt[1])
		dq.appendleft(tmp)
	elif ipt[0] == 'pop_front':
		if not dq	: print(-1)
		else		: print(dq.popleft())
	elif ipt[0] == 'pop_back':
		if not dq	: print(-1)
		else		: print(dq.pop())
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