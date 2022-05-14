import sys
import collections

input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))

q = collections.deque()
answer = [0] * m

for i in range(m):
	while q and q[-1][0] > arr[i]:
		q.pop()
	while q and q[0][1] < i-n+1:
		q.popleft()
	q.append((arr[i], i))
	print(q[0][0], end=" ")
