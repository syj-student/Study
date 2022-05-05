import itertools
import sys
flag = False
while True:
    l = list(map(int, sys.stdin.readline().split()))
    l = l[1:]
    if len(l) == 1 and l[0] == 0:
        break
    if flag:
        print()
    cases = itertools.combinations(l, 6)
    for case in cases:
        print(*case)
    flag = True
