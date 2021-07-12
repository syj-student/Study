import sys
import copy

input = sys.stdin.readline

n = int(input().strip())

## cut
# find min & max
def min_max(tmp):
	ret = [tmp[0][0], tmp[0][1]]
	for i in tmp:
		if i[0] < ret[0]:
			ret[0] = i[0]
		if i[1] > ret[1]:
			ret[1] = i[1]
	return ret

def recur(lst, depth, c, min, max):
	global answer
	if depth == c or min == max:
		if answer < len(lst):
			answer = len(lst)
			return 
	for x in range(min, max):
		tmp = copy.deepcopy(lst)
		for each in lst:
			if each[0] < x < each[1]:
				tmp.extend([[each[0], x],[x, each[1]]])
				del tmp[tmp.index(each)]
		recur(tmp, depth + 1, c, x + 1, max)

# parsing
stock = list()
stock_sub = list()
for m in range(n):
	stock_sub.append(list(map(int, input().strip().split())))
	tmp = list()
	for __ in range(stock_sub[m][0]):
		tmp.append(list(map(int, input().strip().split())))
	stock.append(tmp)

# main
answer = 0
j = 0
for i in stock:
	rg = min_max(i)
	recur(i, 0, stock_sub[j][1], rg[0] + 1, rg[1])
	print(f'Case #{j + 1}: {answer}')
	j += 1
