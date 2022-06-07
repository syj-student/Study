import sys

input = sys.stdin.readline

n = int(input())
lst = set()
for _ in range(n):
	name, inout = input().split()
	if inout == "enter":
		lst.add(name)
	else:
		lst.remove(name)
lst = sorted(lst, reverse=True)
print(*lst, sep="\n")