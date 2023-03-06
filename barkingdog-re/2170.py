from sys import stdin

input = stdin.readline

lines = list()
n = int(input())
for _ in range(n):
    l  = list(map(int, input().split()))
    lines.append(l)


new_lines = list()
while lines:
    l = lines.pop()
    for i in range(len(new_lines)):
        start, end = new_lines[i]
        if start <= l[0] <= end and start <= l[1] <= end:
            break
        elif start <= l[0] <= end or start <= l[1] <= end:
            p = new_lines.pop(i)
            n = [min(p[0], l[0]), max(p[1], l[1])]
            lines.append(n)
            break
    else:
        new_lines.append(l)

answer = 0
for start, end in new_lines:
    answer += end - start
print(answer)