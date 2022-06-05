import sys

input = sys.stdin.readline

m, n = map(int, input().split())
lst = list(map(int, input().split()))
left, right = 0, 0
s = 0
answer = float('inf')
while right <= len(lst):
	if s >= n:
		answer = min(answer, right - left)
		s -= lst[left]
		left += 1
	elif right == m:
		break
	else:
		s += lst[right]
		right += 1
print(answer if answer != float('inf') else 0)