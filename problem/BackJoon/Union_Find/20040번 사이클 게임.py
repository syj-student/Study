import sys
sys.setrecursionlimit(10 ** 9)

def check_union(x):
	if x == table[x]:
		return x
	return check_union(table[x])

def insert_union_index(a, b):
	a = check_union(a)
	b = check_union(b)
	if a == b:
		return True
	elif a < b:
		table[a] = b
	else:
		table[b] = a
	return False


n, m = map(int, sys.stdin.readline().split())
table = [i for i in  range(n)]
for i in range(m):
	a, b = map(int, sys.stdin.readline().split())
	if insert_union_index(a, b):
		print(i+1)
		break
if i == m-1:
	print(0)
