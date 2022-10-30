from collections import deque

def solution(a):
    if len(a) == 1:
        return 0

    def checker_pass():
        nonlocal container
        tmp = {container[0], container[1]}
        if len(container) >= 2:
            for i in range(1, len(container), 2):
                if container[i-1] == container[i]:
                    return False
                tmp &= {container[i-1], container[i]}
                if not tmp:
                    return False 
        return True

    answer = float('-inf')
    container = deque()
    for i in range(len(a)):
        container.append(a[i])
        if len(container) % 2 == 0:
            if checker_pass():
                answer = max(answer, len(container))
                print(container)
            else:
                container.popleft()
    return answer

print(solution([0,3,3,0,7,2,0,2,2,0]))