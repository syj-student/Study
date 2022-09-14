def solution(lottos, win_nums):
    mynumber = set()
    zero = 0
    for l in lottos:
        if l == 0:
            zero += 1
        else:
            mynumber.add(l)

    same = 0
    for num in win_nums:
        if num in mynumber:
            same += 1

    def out(n):
        if n < 2:
            return 6
        else:
            return 7 - n
    return [out(same+zero), out(same)]
    
def solution(lottos, win_nums):
    win_nums = set(win_nums)
    same = zero = 0
    for l in lottos:
        if l in win_nums:
            same += 1
        elif l == 0:
            zero += 1
    return list(map(lambda x: 6 if x < 2 else 7 - x, [same+zero, same]))