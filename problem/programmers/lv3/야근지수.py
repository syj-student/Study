import heapq
def solution(n, works):
    answer = 0
    heap = list()
    for w in works:
        heapq.heappush(heap, -w)
    while heap and n:
        now = heapq.heappop(heap)
        now += 1
        n -= 1
        if now != 0:
            heapq.heappush(heap, now)
    for w in heap:
        answer += w ** 2
    return answer