# https://leetcode.com/problems/array-partition-i/

class Solution:
	def arrayPairSum(self, nums: List[int]) -> int:
		return sum(nums.sort()[::2])
