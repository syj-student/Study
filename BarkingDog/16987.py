import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    x = int(input())
    clothes = defaultdict(set)
    for _ in range(x):
        thing, kind = input().split()
        clothes[kind].add(thing)
    answer = 1
    for k in clothes:
        answer *= len(clothes[k])+1
    print(answer-1)