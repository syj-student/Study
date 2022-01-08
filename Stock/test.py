def p(n):
    stack = list()

    def check(no):
        end = int(no ** 0.5)
        for x in stack:
            if x > end:
                break
            if no % x == 0:
                return
        stack.append(no)

    for j in range(2, n + 1):
        check(j)
    return stack


def ps(l):
    l = [0] + l
    ps = [0] * len(l)
    for i in range(1, len(l)):
        ps[i] = ps[i - 1] + l[i]
    return ps


a = int(input())
b = p(a)
c = ps(b)
ans = 0
l = 0
r = 1
if a == 1:
    print(0)
else:
    while r < len(c):
        d = c[r] - c[l]
        if d == a:
            ans += 1
            r += 1
        elif d < a:
            r += 1
        else:
            l += 1
    print(ans)