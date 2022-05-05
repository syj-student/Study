import sys
import itertools

a, b = map(int, sys.stdin.readline().split())
container = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in range(1, a+1):
    cases = itertools.combinations(container, i)
    for case in cases:
        if sum(case) == b:
            answer += 1
print(answer)
