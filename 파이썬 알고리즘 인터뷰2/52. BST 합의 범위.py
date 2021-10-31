# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	nums_sum = 0
	def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
		if root is None:
			return
		self.rangeSumBST(root.left, low, high)
		self.rangeSumBST(root.right, low, high)
		if low <= root.val <= high:
			self.nums_sum += root.val
		return self.nums_sum

class Solution:
	def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
		stack = [root]
		nums_sum = 0
		while stack:
			node = stack.pop()
			if node:
				if node.val <= high:
					stack.append(node.right)
				if node.val >= low:
					stack.append(node.left)
				if low <= node.val <= high:
					nums_sum += node.val
		return nums_sum
