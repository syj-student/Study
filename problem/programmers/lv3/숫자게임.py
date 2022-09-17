from collections import deque

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A= deque(A)
    B = deque(B)
    while A and B:
        if A[-1] < B[-1]:
            A.pop()
            B.pop()
            answer += 1
        else:
            A.pop()
            B.popleft()
    return answer