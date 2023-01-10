from sys import stdin
from collections import deque

input = stdin.readline
for _ in range(int(input())):
    reverse = True
    cmd = input().strip()
    input()
    ip = input().strip()[1:-1].split(",")
    if ip[0] == "":
        if "D" in cmd:
            print("error")
        else:
            print("[]")
        continue
    dq = deque(ip)
    for c in cmd:
        if c == "R":
            reverse = not reverse
        elif c == "D":
            if dq:
                if reverse:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                print("error")
                break
    else:
        if not reverse:
            dq.reverse()
        p =','.join(dq)
        print(f'[{p}]')