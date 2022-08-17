import sys
from collections import deque
import bisect

input = sys.stdin.readline
lst = deque()

def print_answer():
    l = len(lst)
    mid = l // 2
    if l % 2:
        return mid
    else:
        return mid if lst[mid] < lst[mid-1] else mid - 1

n = int(input())
answer = [0] * n
lst.append(int(input()))
answer[0] = lst[0]
for k in range(1, n):
    x = int(input())
    idx = bisect.bisect_left(lst, x)
    lst.insert(idx, x)
    answer[k] = lst[print_answer()]
print(*answer, sep="\n")
