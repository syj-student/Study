from sys import stdin
from collections import deque
input = stdin.readline

stack = deque()
answer = list()
n = int(input())
i = 1 
for _ in range(n):
    now = int(input())
    while i <= now:
        stack.append(i)
        answer.append("+")
        i+=1
    if stack and stack[-1] == now:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        break
else:
    print(*answer, sep="\n")