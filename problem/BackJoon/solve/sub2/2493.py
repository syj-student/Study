import sys
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
goto = [0] * n
for i in range(n):
	now = tower[i]
	while stack and tower[stack[-1]] < now:
		stack.pop()
	if stack:
		goto[i] = stack[-1] + 1
	stack.append(i)
print(' '.join(list(map(str, goto))))