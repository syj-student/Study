import sys
import itertools

n = int(sys.stdin.readline())
table = list()
for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    table.append(l)


def check(case):
    ret = 0
    for i in range(len(case)):
        tmp = table[case[i-1]][case[i]]
        if tmp == 0 or ret >= answer:
            return False
        ret += tmp
    return ret


lst = [i for i in range(n)]
answer = float('inf')
cases = itertools.permutations(lst, n)
for c in cases:
    tmp = check(c)
    if tmp:
        answer = min(answer, tmp)
print(answer)
