import sys
import itertools

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
cases = itertools.permutations(lst, n)
answer = -sys.maxsize


def check(l):
    ret = 0
    for i in range(1, len(l)):
        ret += abs(l[i-1] - l[i])
    return ret


for case in cases:
    answer = max(answer, check(case))
print(answer)
