# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0
		max_depth = 0
		Q = collections.deque([(1, root)])
		while Q:
			depth, node = Q.popleft()
			if node.left:
				Q.append((depth + 1, node.left))
			if node.right:
				Q.append((depth + 1, node.right))

