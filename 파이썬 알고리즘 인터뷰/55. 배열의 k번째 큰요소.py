# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		if not nums:
			return None
		return sorted(nums, reverse=True)[k-1]