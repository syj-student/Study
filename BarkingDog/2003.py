from sys import stdin

input = stdin.readline
x, y = map(int, input().split())
lst = list(map(int, input().split()))
# lst.sort()
answer = 0
acc = 0
left = 0
for i in range(x):
    acc += lst[i]
    while left <= i and acc >= y:
        if acc == y:
            answer += 1
        acc -= lst[left]
        left += 1
print(answer)