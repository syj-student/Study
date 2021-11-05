# https://leetcode.com/problems/binary-search/

#class Solution:
#	def search(self, nums, target) -> int:
#		left, right = 0, len(nums) - 1
#		while left <= right:
#			mid = (left + right) // 2
#			if nums[mid] < target:
#				left = mid + 1
#			elif nums[mid] > target:
#				right = mid - 1
#			else:
#				return mid
#		return -1

import bisect

class Solution:
	def search(self, nums, target) -> int:
		idx = bisect.bisect_left(nums, target)
		if idx < len(nums) and nums[idx] == target:
			return idx
		return -1
a = Solution()
a.search([-1,0,3,5,9,12, 24], -55456)