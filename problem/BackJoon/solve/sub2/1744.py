import sys

input = sys.stdin.readline

m = int(input())
if m == 0:
	print(0)
	exit(0)
p = list()
n = list()
acc = 0
for _ in range(m):
	x = int(input())
	if x == 1:
		acc += 1
	elif x > 1:
		p.append(x)
	elif x <= 0:
		n.append(x)
p.sort(reverse=True)
n.sort()

def mysum(l):
	ret = 0
	if len(l) % 2:
		for i in range(0, len(l)-1, 2):
			ret += l[i] * l[i+1]
		ret += l[-1]
	else:
		for i in range(0, len(l), 2):
			ret += l[i] * l[i+1]
	return ret
acc += mysum(p)
acc += mysum(n)
print(acc)