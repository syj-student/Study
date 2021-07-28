import sys
from itertools import combinations

# input
n = int(sys.stdin.readline())
table = list()
for __ in range(n):
	table.append(list(map(int, sys.stdin.readline().split())))

# solve
def TeamScore(lst_team):
	op = list(set(lst_member) - set(lst_team))
	sum = 0
	for i in lst_team:
		for j in lst_team:
			sum += table[i][j]
	for i in op:
		for j in op:
			sum -= table[i][j]
	return abs(sum)

lst_member = [i for i in range(n)]
ret = 1000000000
for lst in combinations(lst_member, n // 2):
	tmp = TeamScore(lst)
	if ret > tmp:
		ret = tmp

# print

print(ret)