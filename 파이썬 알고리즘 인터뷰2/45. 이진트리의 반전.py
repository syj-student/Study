# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		Q = collections.deque([root])

		while Q:
			node = Q.popleft()

			node.left, node.right = node.right, node.left
			