from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())

tree = defaultdict(list)
for _ in range(n):
    x, y, z = map(int, input().split())
    tree[x].append((y, z))