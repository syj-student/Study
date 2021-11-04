# https://leetcode.com/problems/sort-colors/#

class Solution:
	def sortColors(self, nums) -> None:
		a, b, c = 0, 0, len(nums)
		while b < c:
			if nums[b] < 1:
				nums[a], nums[b] = nums[b], nums[a]
				a, b = a + 1, b + 1
			elif nums[b] > 1:
				c = c - 1
				nums[b], nums[c] = nums[c], nums[b]
			else:
				b = b + 1

a = Solution()
b = [2, 0, 1]
a.sortColors(b)
print(b)
