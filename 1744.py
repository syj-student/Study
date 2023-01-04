from sys import stdin

input = stdin.readline

n, p = list(), list()

for i in range(int(input())):
    x = int(input())
    if x <= 0:
        n.append(x)
    elif x > 0:
        p.append(x)

answer, checker = 0, set()

n.sort()
p.sort(reverse=True)
for i in range(0, len(p), 2):
    if i + 1 < len(p):
        answer += p[i] * p[i+1]
    else:
        answer += p[i]


for i in range(0, len(n), 2):
    if i + 1 < len(n):
        answer += n[i] * n[i+1]
    else:
        answer += n[i]

print(answer)