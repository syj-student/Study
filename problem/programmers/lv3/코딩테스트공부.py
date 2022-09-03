from collections import defaultdict
from copy import deepcopy
import heapq

def solution(alp, cop, problems):
    class v():
        value = float('inf')

    problems = list(map(tuple, problems))
    visited = defaultdict(v)
    max_alp = max_cop = 0
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])

    def check(a, c):
        for p in problems:
            if not (p[0] <= a and p[1] <= c):
                return False
        return True

    heap = [(0, alp, cop)]
    while heap:
        t, now_alp, now_cop = heapq.heappop(heap)
        if check(now_alp, now_cop):
            return t

        tmp_alp = min(now_alp+1, max_alp)
        if visited[(tmp_alp, now_cop)].value > t+1:
            visited[(tmp_alp, now_cop)].value = t+1
            heapq.heappush(heap, (t+1, tmp_alp, now_cop))

        tmp_cop = min(now_cop+1, max_cop)
        if visited[(now_alp, tmp_cop)].value > t+1:
            visited[(now_alp, tmp_cop)].value = t+1
            heapq.heappush(heap, (t+1, now_alp, tmp_cop))

        for p in problems:
            next_time = t+p[4]
            next_alp = min(now_alp+p[2], max_alp)
            next_cop = min(now_cop+p[3], max_cop)
            if now_alp >= p[0] and now_cop >= p[1] and visited[(next_alp, next_cop)].value > next_time:
                visited[(next_alp, next_cop)].value = next_time
                heapq.heappush(heap, (next_time,next_alp , next_cop))