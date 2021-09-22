# https://leetcode.com/problems/product-of-array-except-self/
import collections

class Solution:
	def productExceptSelf(self, nums: list) -> list:
		nums_left = [1]
		nums_right = collections.deque([1])
		ret = list()
		j = len(nums) - 1
		for i in range(len(nums)):
			nums_left.append(nums_left[-1] * nums[i])
			nums_right.appendleft(nums_right[0] * nums[j])
			j -= 1
		for i in range(len(nums)):
			ret.append(nums_left[i] * nums_right[i + 1])
		return ret

nums = [1,2,3,4]
tmp = Solution()
print(tmp.productExceptSelf(nums))
