from sys import stdin

input = stdin.readline

_ = input()
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = a - b
print(len(c), *sorted(c))