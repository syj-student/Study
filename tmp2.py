def solution(n, stations, w):
    answer = 0
    repeater = set(map(lambda x: x-1, stations))
    apt = [False] * n
    i = 0
    while i < n:
        if apt[i] == False:
            tmp = i+w
            print(tmp)
            if tmp not in repeater:
                answer += 1
            i = tmp + w + 1
        else:
            if i in repeater:
                i = i+w+1
            else:
                i += 1

    return answer

print(
    solution(
        16, [9], 2
    )
)