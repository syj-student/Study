# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def buildTree(self, preorder, inorder):
		inorder.reverse()
		def makeTree(elements):
			if not elements:
				return
			seq = inorder.pop()
			node = TreeNode(seq)
			node.left = makeTree(preorder[:elements.index(seq)])
			node.right = makeTree(preorder[elements.index(seq)+1:])
			return node
		return makeTree(preorder)