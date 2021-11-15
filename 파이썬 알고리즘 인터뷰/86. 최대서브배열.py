# https://leetcode.com/problems/maximum-subarray/

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		biggest = -sys.maxsize
		current_sum = 0
		for num in nums:
			current_sum = max(num, num + current_sum)
			biggest = max(current_sum, biggest)
		return biggest