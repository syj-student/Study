def solution(arr):
    answer = []
    prev = -1
    for a in arr:
        if a == prev:
            continue
        prev = a
        answer.append(a)
    return answer