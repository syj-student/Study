import sys

input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
dq = list()
answer = [0] * n
for i in range(n-1, -1, -1):
    while dq and lst[dq[-1]] <= lst[i]:
        answer[dq.pop()] = i+1
    dq.append(i)
print(*answer, sep=" ")