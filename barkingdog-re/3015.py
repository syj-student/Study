from sys import stdin
from collections import deque
input = stdin.readline

stack = deque()
n = int(input())
answer = 0

for _ in n:
    now = int(input())
    
print(answer)