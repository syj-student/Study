import sys
import itertools


a, b = map(int, sys.stdin.readline().split())
container = [i for i in range(1, a + 1)]
answer = itertools.permutations(container, b)

for ret in answer:
    print(*ret)
