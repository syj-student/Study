# https://leetcode.com/problems/largest-number/submissions/
import collections
class Solution:
	def largestNumber(self, nums) -> str:
		nums_dict = collections.defaultdict(list)
		for num in nums:
			nums_dict[len(str(num))].append(num)
		answer = ''
		for key in sorted(nums_dict.keys(), reverse=True):
			answer += ''.join(map(str, sorted(nums_dict[key], reverse=True)))
		return answer

a = Solution()
print(a.largestNumber([10, 11, 2]))