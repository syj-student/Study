import sys
import collections

input = sys.stdin.readline().strip


def parse_list(l, x):
    if not x:
        return 0
    return collections.deque(l[1:-2].split(','))


n = int(input())
for _ in range(n):
    front = True
    cmd = input()
    x = int(input())
    lst = parse_list(input(), x)
    if not x:
        if 'D' in cmd:
            print('error')
        else:
            print('[]')
        continue
    for c in cmd:
        if c == 'D':
            if not lst:
                print('error')
                break
            if front:
                lst.popleft()
            else:
                lst.pop()
        elif c == 'R':
            front = not front
    if front:
        a = ','.join(lst)
        print(f'[{a}]')
    else:
        lst.reverse()
        a = ','.join(lst)
        print(f'[{a}]')
