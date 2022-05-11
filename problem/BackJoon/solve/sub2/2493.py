import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
answer = [0] * n
big = [0] * n
big[-1] = lst[-1]
for i in range(n-2, -1, -1):
	big[i] = max(lst[i], big[i+1])
stack = list()
for i in range(n-1, 0, -1):
	stack.append(i)
	if big[i-1] > lst[i]:
		while stack:
			answer[stack.pop()] = i
print(" ".join(map(str, answer)))