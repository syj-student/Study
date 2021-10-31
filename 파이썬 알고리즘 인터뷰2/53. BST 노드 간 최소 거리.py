# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def minDiffInBST(self, root: Optional[TreeNode]) -> int:
		min_gap = sys.maxsize
		node_value = list()
		stack = list()
		node = root
		while node or stack:
			while node:
				stack.append(node)
				node = node.left
			node = stack.pop()
			node_value.append(node.val)
			node = node.right
		for i in range(len(node_value)):
			for j in range(i+1, len(node_value)):
				min_gap = min(min_gap, abs(node_value[i] - node_value[j]))
		return min_gap