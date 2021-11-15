# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		heap = list()
		for x, y in points:
			length = x**2 + y**2
			heapq.heappush(heap, (length, [x, y]))
		answer = list()
		for _ in range(k):
			length, coord = heapq.heappop(heap)
			answer.append(coord)
		return answer