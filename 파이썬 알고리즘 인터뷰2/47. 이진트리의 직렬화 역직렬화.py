# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

	def serialize(self, root):
		stack = collections.deque()
		Q = collections.deque([root])
		while Q:
			node = Q.popleft()
			if node:
				stack.append(node.val)
				if node.left:
					Q.append(node.left)
				else:
					Q.append(None)
				if node.right:
					Q.append(node.right)
				else:
					Q.append(None)
			else:
				stack.append(None)
		return stack
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""


	def deserialize(self, data):
		print("dkafkjdafdfamk")
		print(data, "Hello world")
		root = TreeNode(data.popleft())
		Q = collections.deque([root])
		while data:
			node = Q.popleft()
			tmp = data.popleft()
			if tmp:
				node.left = TreeNode(tmp)
				Q.append(node.left)
			tmp = data.popleft()
			if tmp:
				node.right = TreeNode(tmp)
				Q.append(node.right)

		return root
		"""Decodes your encoded data to tree.

		:type data: str
		:rtype: TreeNode
		"""


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
