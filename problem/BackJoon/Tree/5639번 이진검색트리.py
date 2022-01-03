import sys
sys.setrecursionlimit(10 ** 9)

# class Node:
# 	def __init__(self, val, left=None, right=None):
# 		self.val = val
# 		self.left = left
# 		self.right = right
#
#
# class BinaryTree:
# 	def __init__(self, root=None):
# 		self.root = root
#
# 	def node_append(self, node):
# 		if not self.root:
# 			self.root = node
# 		else:
# 			location = self.root
# 			while location:
# 				if location.val < node.val:
# 					if location.right:
# 						location = location.right
# 					else:
# 						location.right = node
# 						break
# 				else:
# 					if location.left:
# 						location = location.left
# 					else:
# 						location.left = node
# 						break
#
#
# 	def postorder_print(self):
# 		def postorder(node):
# 			if node.left:
# 				postorder(node.left)
# 			if node.right:
# 				postorder(node.right)
# 			print(node.val)
#
# 		if self.root:
# 			postorder(self.root)
#
# binary_tree = BinaryTree()
# while True:
# 	try:
# 		binary_tree.node_append(Node(int(sys.stdin.readline())))
# 	except:
# 		break
#
# binary_tree.postorder_print()

nums = []
while True:
	try:
		nums.append(int(sys.stdin.readline()))
	except:
		break


def pre_to_post(nums_lst):
	if not nums_lst:
		return
	if len(nums_lst) == 1:
		print(nums_lst[0])
		return
	root_val = nums_lst[0]
	k = len(nums_lst)
	for i in range(1, len(nums_lst)):
		if root_val < nums_lst[i]:
			k = i
			break
	pre_to_post(nums_lst[1:k])
	pre_to_post(nums_lst[k:])
	print(root_val)

pre_to_post(nums)
