from collections import deque
from copy import deepcopy

def solution(n, info):
    ret_gap = 0
    ret = [-1]
    info.reverse()
    def dfs(answer = [0]*11, start=0, depth=0, info=info):
        nonlocal ret_gap, ret
        if depth == n:
            ryon = pitch = 0
            for i in range(11):
                if answer[i] != 0 or info[i] != 0:
                    s = answer[i] - info[i]
                    if s > 0:
                        ryon += i
                    else:
                        pitch += i
            gap = ryon - pitch
            if ret_gap < gap:
                ret_gap = gap
                ret = deepcopy(answer)
            return
        for i in range(start, 11):
            answer[i] += 1
            dfs(answer, i, depth+1, info)
            answer[i] -= 1
    dfs()
    ret.reverse()
    return ret

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))