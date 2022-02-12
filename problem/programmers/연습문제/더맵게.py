import heapq

def solution(scoville, K):
	if len(scoville) < 1:
		return 0 if scoville and scoville[0] >= K else -1
	heapq.heapify(scoville)
	answer = 0
	while len(scoville) > 1 and  scoville[0] < K:
		a = heapq.heappop(scoville)
		aa = heapq.heappop(scoville)
		heapq.heappush(scoville, a + 2*aa)
		answer += 1
	if scoville[0] < K:
		return -1
	return answer