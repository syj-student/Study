import heapq
from copy import deepcopy

def solution(alp, cop, problems):
    prob = set()
    for p in problems:
        if not (p[0] <= alp and p[1] <= cop):
            prob.add(tuple(p))
            
    answer = 0
    heap = [(0, prob, alp, cop)]
    while heap:
        t, prob, alp, cop = heapq.heappop(heap)
        tmp = set()
        for p in prob:
            if p[0] <= alp and p[1] <= cop:
                tmp.add(p)
        prob -= tmp
        if not prob:
            return t
        heapq.heappush(heap, (t+1, deepcopy(prob), alp+1, cop))
        heapq.heappush(heap, (t+1, deepcopy(prob), alp, cop+1))
        for p in problems:
            if p[0] <= alp and p[1] <= cop:
                heapq.heappush(heap, (t+p[4], deepcopy(prob), alp+p[2], cop+p[3]))
    return answer

print(solution(
    10, 10,
    [[10,15,2,1,2],[20,20,3,3,4]]
))