import sys
import collections

input = sys.stdin.readline

def All_replace(l, a, b):
	while a in l:
		l = l.replace(a, b)
	return l

n = int(input())
table = collections.defaultdict(int)
for _ in range(n):
	l = input().strip()
	for i in range(len(l)):
		table[l[i]] += 10**(len(l) -i-1)
t = sorted(table.values(), reverse=True)
answer = 0
num = 9
for k in t:
	answer += k * num
	num -= 1
print(answer)