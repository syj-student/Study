from collections import deque

# input
n = int(input())

# solve
if n == 1:
	print(1)
elif n == 3:
	print(2)
else:
	deq = deque([i * 2 for i in range(1, (n // 2) + 1)])
	if n % 2:
		while len(deq) > 1:
			deq.append(deq.popleft())
			deq.popleft()
	else:
		while len(deq) > 1:
			deq.popleft()
			deq.append(deq.popleft())
	print(deq[0])