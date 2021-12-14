class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		merge_list = sorted(nums1 + nums2)
		mid = len(merge_list) // 2
		if len(merge_list) % 2:
			return merge_list[mid]
		return (merge_list[mid] + merge_list[mid - 1]) / 2