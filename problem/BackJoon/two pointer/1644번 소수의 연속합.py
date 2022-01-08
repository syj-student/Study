import sys

num = int(sys.stdin.readline())


def range_prime(n):
    m = int(n ** 0.5) + 1
    s = [1] * (n + 1)
    for i in range(2, m):
        if s[i] == 1:
            for j in range(i + i, n + 1, i):
                s[j] = 0
    return [i for i in range(2, n + 1) if s[i] == 1]


left, answer, acc = 0, 0, 0
lst = range_prime(num)
for i in range(len(lst)):
    acc += lst[i]
    if acc == num:
        answer += 1
    elif acc > num:
        while acc > num:
            acc -= lst[left]
            left += 1
        if acc == num:
            answer += 1

print(answer)
