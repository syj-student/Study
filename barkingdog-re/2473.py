from sys import stdin
from bisect import bisect_left
input = stdin.readline

n = int(input())
info = list(map(int, input().split()))
info.sort()

def checker(lst):
    global answer, degree

    if degree > (dg := abs(sum(lst))):
        answer = lst
        degree = dg


answer, degree = set(), float('inf')
for f in range(n):
    for s in range(f+1, n):
        left , right = s+1, n-1
        now = info[f] + info[s]
        while left <= right:
            mid = (left+right) // 2

            new_now = now + info[mid]
            if new_now == 0:
                print(info[f], info[s], info[mid])
                exit(0)
            elif new_now < 0:
                left = mid + 1
            else:
                right = mid - 1
        checker([info[f], info[s], info[mid]])
print(*answer)
            