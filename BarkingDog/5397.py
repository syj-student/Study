import sys
import collections

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    t = input().rstrip()
    i = 0
    for c in t:
        if c in "<>-":
            i += 1
        else:
            break
    left = collections.deque()
    right = collections.deque()
    for k in range(i, len(t)):
        if t[k] == '<':
            if left:
                right.appendleft(left.pop())
        elif t[k] == '>':
            if right:
                left.append(right.popleft())
        elif t[k] == '-':
            if left:
                left.pop()
        else:
            left.append(t[k])
    print(''.join(left + right))