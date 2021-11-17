# input
n = int(input())

# solve
ret = 0
check = [True] * n
answer = list()

def funcheck(n):
	for i in range(n):
		if abs(answer[i] - answer[n]) ==  n - i:
			return False
	return True

def dfs(n, depth):
	if depth == n:
		global ret
		ret += 1
		return
	for i in range(n):
		if check[i]:
			check[i] = False
			answer.append(i)
			if funcheck(depth):
				dfs(n, depth + 1)
			check[i] = True
			answer.pop()

# print
dfs(n, 0)
print(ret)

### re-code by C (Cause time out)