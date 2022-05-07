import sys
import collections

input = sys.stdin.readline
n, m = map(int, input().split())
t = collections.defaultdict(list)
answer = [float('inf')] * (n+1)
in_q = [False] * (n+1)
chk_cycle = [0] * (n+1)
for _ in range(m):
	a, b, c = map(int, input().split())
	t[a].append((b, c))
def SPFA(start):
	answer[start] = 0
	in_q[start] = True
	q = collections.deque([start])
	while q:
		now = q.popleft()
		in_q[now] = False
		for arr, cost in t[now]:
			if answer[arr] > answer[now] + cost:
				answer[arr] = answer[now] + cost
				if not in_q[arr]:
					in_q[arr] = True
					q.append(arr)
					chk_cycle[arr] += 1
					if chk_cycle[arr] >= n:
						return False
	return True

o = SPFA(1)
if not o:
	print(-1)
else:
	for i in range(2, len(answer)):
		if answer[i] == float('inf'):
			print(-1)
		else:
			print(answer[i])
