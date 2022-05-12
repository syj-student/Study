import sys

input = sys.stdin.readline

n = int(input())
b = list()
for _ in range(n):
	b.append(int(input()))

tmp = 0
stack = list()
for i in range(n):
	while stack and stack[-1] <= b[i]:
		stack.pop()
	tmp += len(stack)
	stack.append(b[i])
print(tmp)