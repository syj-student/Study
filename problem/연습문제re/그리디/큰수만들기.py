from collections import deque

def solution(number, k):
    answer = deque()
    for c in number:
        while answer and answer[-1] < c and k > 0:
            answer.pop()
            k -= 1
        answer.append(c)
    while answer and k > 0:
        answer.pop()
        k -= 1
    return ''.join(answer)

        
print(solution("654321", 5))