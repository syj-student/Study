# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
		def dfs(nums_list):
			if not nums_list:
				return
			mid = len(nums_list) // 2
			node = TreeNode(nums_list[mid])
			node.left = dfs(nums_list[:mid])
			node.right = dfs(nums_list[mid + 1:])
			return node
		return dfs(nums)
