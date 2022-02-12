from collections import deque
from bisect import bisect_left

def solution(operations):
	dq = deque()
	for i in operations:
		op, num = i.split()
		num = int(num)
		if op == 'I':
			idx = bisect_left(dq, num)
			dq.insert(idx, num)
		elif dq and op == 'D':
			if num == 1:
				dq.pop()
			else:
				dq.popleft()
	if dq:
		return [dq[-1], dq[0]]
	return [0, 0]