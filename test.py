import heapq

def solution(alp, cop, problems):
    problems = list(map(tuple, problems))

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
        heapq.heappush(heap, (t+1, now_alp+1, now_cop))
        heapq.heappush(heap, (t+1, now_alp, now_cop+1))
        for p in problems:
            if now_alp <= p[0] and now_cop <= p[1]:
                heapq.heappush(heap, (t+p[4], now_alp+p[2], now_cop+p[3]))

print(solution(
    10, 10,
    [[10,15,2,1,2],[20,20,3,3,4]]
))