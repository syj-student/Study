# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1 = sorted(list(set(nums1)))
		nums2 = list(set(nums2))
		answer = list()
		for i in nums2:
			idx = bisect.bisect_left(nums1, i)
			if idx < len(nums1) and nums1[idx] == i:
				answer.append(nums1[idx])
		return answer
