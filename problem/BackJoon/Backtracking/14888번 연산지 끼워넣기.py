import sys

# input
len_num	= int(sys.stdin.readline())
lst_num	= list(map(int, sys.stdin.readline().split()))
lst_op	= list(map(int, sys.stdin.readline().split()))

# solve
max_result = -1000000001
min_result = 1000000001

def cal(tmp, i, depth):
	if i == 0:
		tmp += lst_num[depth]
	elif i == 1:
		tmp -= lst_num[depth]
	elif i == 2:
		tmp *= lst_num[depth]
	elif i == 3:
		if tmp < 0:
			tmp = -tmp // lst_num[depth]
			tmp *= -1
		else:
			tmp //= lst_num[depth]
	return tmp

def DFS(tmp, depth, limit):
	global max_result
	global min_result
	if depth == limit:
		max_result = max(max_result, tmp)
		min_result = min(min_result, tmp)
		return
	for i in range(4):
		if lst_op[i]:
			re_tmp = tmp
			lst_op[i] -= 1
			tmp = cal(tmp, i, depth)
			DFS(tmp, depth + 1, limit)
			lst_op[i] += 1
			tmp = re_tmp

# print
DFS(lst_num[0], 1, len_num)
print(max_result)
print(min_result)