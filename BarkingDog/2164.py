from collections import deque

n = int(input())
dq = deque([i for i in range(1, n+1)])
flag = -1
while len(dq) != 1:
    if flag == -1:
        dq.popleft()
    else:
        dq.append(dq.popleft())
    flag *= -1
print(dq[0])