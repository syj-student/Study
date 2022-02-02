from sys import stdin
from collections import Counter

stdin.readline()
x = Counter(stdin.readline().split())
stdin.readline()
answer = stdin.readline().split()
for c in answer:
    print(x[c], end=' ')
