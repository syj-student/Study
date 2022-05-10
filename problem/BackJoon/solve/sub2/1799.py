import sys
from pprint import pprint
import collections

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input())
m = list()
for _ in range(n):
	m.append(list(map(int, input().split())))

deck = collections.defaultdict(list)
bishop = collections.defaultdict(list)
answer = 0

for i in range(n):
	for j in range(n):
		if m[i][j] == 1:
			deck[i+j].append((i, j))


def check():
	t = collections.defaultdict(int)
	for k in bishop.values():
		for x, y in k:
			print(x, y)
			t[x-y] += 1
			if t[x-y] > 1:
				return -1
	return len(t)


def rec(dep=0):
	global answer
	if dep == (2*n-1):
		pprint(bishop)
		tmp = check()
		answer = max(answer, tmp)
		return
	if deck[dep]:
		for x, y in deck[dep]:
			bishop[dep].append((x, y))
			rec(dep+1)
			bishop[dep].remove((x, y))
	else:
		rec(dep+1)

rec()
print(answer)