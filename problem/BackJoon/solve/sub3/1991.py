import sys
import collections

input = sys.stdin.readline

tree = dict()
n = int(input())
for _ in range(n):
	a, b, c = input().split()
	tree[a] = [b, c]

# 전위순회
def pre_order(now):
	print(now, end="")
	left, right = tree[now][0], tree[now][1]
	if left != ".":
		pre_order(left)
	if right != ".":
		pre_order(right)
pre_order("A")
print()

# 중위순회
def pre_order(now):
	left, right = tree[now][0], tree[now][1]
	if left != ".":
		pre_order(left)
	print(now, end="")
	if right != ".":
		pre_order(right)
pre_order("A")
print()

# 후위순회
def pre_order(now):
	left, right = tree[now][0], tree[now][1]
	if left != ".":
		pre_order(left)
	if right != ".":
		pre_order(right)
	print(now, end="")
pre_order("A")
print()