import sys

input = sys.stdin.readline

# input
n, m = map(int, input().strip().split())

# make list
lst = [i for i in range(1, n + 1)]
print(lst)