# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
	def maxSlidingWindow(self, nums, k):
		if not nums:
			return []
		def myMax(start, end):
			ret = nums[start]
			for i in range(start+1, end):
				if ret < nums[i]:
					ret = nums[i]
			return ret

		if len(nums) <= k:
			return [max(nums)]
		max_window = myMax(0, k)
		start, end, ret = 0, k, [max_window]
		while end < len(nums):
			if nums[start] == max_window:
				max_window = myMax(end+1-k, end+1)
			else:
				max_window = max_window if max_window >= nums[end] else nums[end]
			ret.append(max_window)
			start += 1; end += 1
		return ret

a = Solution()
print(a.maxSlidingWindow([-8,7,5,7,1,6,0], 4))
print()