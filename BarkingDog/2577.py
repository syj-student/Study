import sys
from collections import Counter

input = sys.stdin.readline
out = 1
for _ in range(3):
    out = out * int(input())
a = Counter(str(out))
for i in range(10):
    print(a[str(i)])