import sys

stack = list()
while True:
	tmp = sys.stdin.readline().rstrip()
	if tmp == '.':
		break
	flag = True
	for i in tmp:
		if i == '(' or i == '[':
			stack.append(i)
		elif i == ')':
			if not stack or stack[-1] != '(':
				flag = False
				break
			else:
				stack.pop()
		elif i == ']':
			if not stack or stack[-1] != '[':
				flag = False
				break
			else:
				stack.pop()
	if flag == False or stack:
		print('no')
	else:
		print('yes')
	stack.clear()
