# https://leetcode.com/problems/majority-element/

class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		half = len(nums) // 2
		counter = collections.Counter(nums)
		return counter.most_common(1)[0][0]

class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		return sorted(nums)[len(nums) // 2]