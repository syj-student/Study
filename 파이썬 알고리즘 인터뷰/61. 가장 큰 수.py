# https://leetcode.com/problems/largest-number/submissions/
import collections
class Solution:
	def largestNumber(self, nums) -> str:
		def swap(a, b):
			a, b = str(a), str(b)
			return a + b if int(a + b) > int(b + a) else b + a
		answer = ''
		for i in nums:
			answer = swap(answer, i)
		return str(int(answer))

a = Solution()
print(a.largestNumber([10, 11, 2]))