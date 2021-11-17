# https://leetcode.com/problems/subsets/

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		result = list()
		for i in range(len(nums) + 1):
			result += itertools.combinations(nums, i)
		return result
