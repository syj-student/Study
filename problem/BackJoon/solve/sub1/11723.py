import sys

n = int(sys.stdin.readline())
ret = set()
for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            ret = set([i for i in range(1, 21)])
        else:
            ret = set()
    else:
        cmd, x = cmd
        x = int(x)
        if cmd == 'add':
            ret.add(x)
        elif cmd == 'remove':
            if x in ret:
                ret.discard(x)
        elif cmd == 'check':
            print(1 if x in ret else 0)
        elif cmd == 'toggle':
            if x in ret:
                ret.discard(x)
            else:
                ret.add(x)
