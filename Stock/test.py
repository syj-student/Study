n = 11

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


print(stack)

