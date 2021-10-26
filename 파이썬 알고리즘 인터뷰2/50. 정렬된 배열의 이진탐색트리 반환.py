# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def bstInsert(val):
		
	def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
		mid = len(nums) // 2
		left_nums = nums[:mid]
		right_nums = nums[mid:]