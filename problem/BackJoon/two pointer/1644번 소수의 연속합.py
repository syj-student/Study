import sys

num = int(sys.stdin.readline())


def range_prime(n):
    stack = list()

    def check(no):
        end = int(no**0.5)
        for x in stack:
            if x > end:
                break
            if no % x == 0:
                return
        stack.append(no)

    for j in range(2, n + 1):
        check(j)
    return stack


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
