from sys import stdin
from bisect import bisect_left

input = stdin.readline

length = int(input())
lst = list(map(int, input().split()))

a = [float('-inf')]
for n in lst:
    if a[-1] < n:
        a.append(n)
    else:
        i = bisect_left(a, n)
        a[i] = n
print(len(a)-1)