import sys
import bisect

input = sys.stdin.readline


problems = list()
problems_dict = dict()
for _ in range(int(input())):
    a, b = map(int, input().split())
    problems.append((b, a))
    problems_dict[a] = b
problems.sort()

tmp = list()
for _ in range(int(input())):
    cmd = tuple(input().split())
    if cmd[0] == "add":
        x, y = int(cmd[2]), int(cmd[1])
        idx = bisect.bisect_left(problems, (x, y))
        problems.insert(idx, (x, y))
        problems_dict[y] = x
    elif cmd[0] == "recommend":
        if cmd[1] == "1":
            tmp.append(problems[-1][1])
            print(problems[-1][1])
        else:
            tmp.append(problems[0][1])
            print(problems[0][1])
    else:
        y = int(cmd[1])
        x = problems_dict[y]
        idx = bisect.bisect_left(problems, (x, y))
        problems.pop(idx)

# print(tmp)