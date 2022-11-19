def solution(n, lost, reserve):
    new_lost, new_reserve = set(lost), set(reserve)
    lost, reserve = new_lost-new_reserve, new_reserve-new_lost
    answer = n-len(lost)
    for now in sorted(lost):
        if (x := now-1) in reserve or (x := now+1) in reserve:
            reserve.remove(x)
            answer += 1
    return answer

print(solution(
    13, [1, 2, 5, 6, 10, 12, 13], [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
))