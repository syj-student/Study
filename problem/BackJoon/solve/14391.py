import sys
import itertools


def get_sum(bit):
    tmp = list(bit)
    bit = [tmp[i:i+b] for i in range(0, len(tmp), b)]
    total_sum = 0
    for i in range(a):
        n = 0
        for j in range(b):
            if bit[i][j] == 1:
                n = 10 * n + container[i][j]
            if bit[i][j] == 0 or j == b - 1:
                total_sum += n
                n = 0
    for i in range(b):
        n = 0
        for j in range(a):
            if bit[j][i] == 0:
                n = 10 * n + container[j][i]
            if bit[j][i] == 1 or j == a - 1:
                total_sum += n
                n = 0
    return total_sum


a, b = map(int, sys.stdin.readline().split())
container = list()
for _ in range(a):
    container.append(list(map(int, ' '.join(sys.stdin.readline()).split())))
answer = 0
cases = itertools.product([0, 1], repeat=a*b)
for case in cases:
    answer = max(answer, get_sum(case))
print(answer)
