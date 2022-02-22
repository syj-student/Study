# https://leetcode.com/problems/house-robber/

class Solution:
	def rob(self, nums: List[int]) -> int:
		if not nums:
			return 0
		if len(nums) <= 2:
			return max(nums)
		dp = collections.defaultdict(int)
		dp[0], dp[1] = nums[0], max(nums[1], nums[0])
		for i in range(2, len(nums)):
			dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
		return dp.popitem()[1]