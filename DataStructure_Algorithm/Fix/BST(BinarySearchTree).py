###
# Class Node
###
class Node:
	def __init__(self, val):
		self.key = val
		self.left = None
		self.right = None

###
# Class Tree
###
class bstTree:
	def __init__(self):
		self.root = None
		self.height = None

	def insert(val):
		if self.root is None:
			self.root = Node(val)

a = bstTree()
a.insert(10)
print()