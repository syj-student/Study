# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def mergeTrees(self, root1, root2):
		if root1 and root2:
			tmp = TreeNode(root1.val + root2.val)
			tmp.left = self.mergeTrees(root1.left, root2.left)
			tmp.right = self.mergeTrees(root1.right, root2.right)
			return tmp
		else:
			return root1 or root2

def printNode(root):
	if root is None:
		return
	print(root.val)
	printNode(root.left)
	printNode(root.right)

a = TreeNode(10)
a.left = TreeNode(20)
a.left.left = TreeNode(30)
a.left.right = TreeNode(31)

b = TreeNode(11)
b.right = TreeNode(22)

print(id(a))
printNode(a)
s = Solution()
c = s.mergeTrees(a, b)
print()
#a.left.val = 21

printNode(c)

