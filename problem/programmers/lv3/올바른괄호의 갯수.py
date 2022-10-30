import sys
from collections import deque

input = sys.stdin.readline


def solution(n):
    answer = 0
    dq = deque([(0, n, n)])
    while dq:
        now, left, right = dq.popleft()
        if left == 0 and right == 0:
            answer += 1
            continue
        if now == 0:
            dq.append((now+1, left-1, right))
        else:
            if right > 0:
                dq.append((now-1, left, right-1))
            if left > 0:
                dq.append((now+1, left-1, right))
    return answer

print(solution(2))