# https://leetcode.com/problems/top-k-frequent-elements/#

class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		frequencyMap = collections.Counter(nums).most_common()
		answer = list()
		for i in range(k):
			answer.append(frequencyMap[i][0])
		return answer