from sys import stdin
from collections import deque
input = stdin.readline

for _ in range(int(input())):
    s = input().strip()
    left = deque()
    right = deque()
    for c in s:
        if c == '<':
            if left:
                right.appendleft(left.pop())
        elif c == '>':
            if right:
                left.append(right.popleft())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)
    print(''.join(left), ''.join(left))

