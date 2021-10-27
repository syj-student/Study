###
# Class Node
###
class Node:
	def __init__(self, val):
		self.val = val
		self.height = 1
		self.left = None
		self.right = None

###
# Class Tree
###
class bstTree:
	def __init__(self):
		self.root = None
		self.height = None

	def insert(self, val):
		def searchPositionAndInsert(node):
			while True:
				if node.val == val:
					print("exist same value node")
					return
				elif node.val < val:
					if node.right is None:
						node.right = Node(val)
						return
					node = node.right
				else:
					if node.left is None:
						node.left = Node(val)
						return
					node = node.left

		if self.root is None:
			self.root = Node(val)
		else:
			searchPositionAndInsert(self.root)

	def preorderPrint(self):
		def dfs(node):
			if node is None:
				return
			dfs(node.right)
			print(f"{node.val}")
			dfs(node.left)
			print()
		dfs(self.root)

a = bstTree()
a.insert(6)
a.insert(7)
a.insert(8)

a.preorderPrint()