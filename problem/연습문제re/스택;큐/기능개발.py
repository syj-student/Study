from math import ceil

def solution(progresses, speeds):
    answer = []
    release_day = ceil((100-progresses[0])/speeds[0])
    acc = 0
    for i in range(len(progresses)):
        now = ceil((100-progresses[i])/speeds[i])
        if now <= release_day:
            acc += 1
        else:
            answer.append(acc)
            release_day = now
            acc = 1
    answer.append(acc)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
