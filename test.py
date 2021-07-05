###
# Class Node
###
class	Node:

	def __init__(self, key = None, left = None, right = None, level = 0):
		self.key = key
		self.left = left
		self.right = right
		self.level = level

	def make(self, key, left, right):
		self.key = key
		self.left = left
		self.right = right


###
# Class Tree
###
class	Tree:

	def __init__(self, key = None, level = 0, hight = None, max = None, min = None):
		self.root = Node()
		self.root.key = key
		self.level = 0
		self.hight = 0
		self.level = level
		self.hight = hight
		self.max = max
		self.min = min

	#
	def __sub_insert(self, node, insert_key):
		if insert_key >= node.key:
			if node.right == None:
				node.right = Node(key= insert_key, level= node.level + 1)
				return
			node = node.right
			self.__sub_insert(node, insert_key)
		else:
			if node.left == None:
				node.left = Node(key= insert_key, level= node.level + 1)
				return
			node = node.left
			self.__sub_insert(node, insert_key)

	def inset(self, insert_key):
		if self.root.key == None:
			self.root.key = insert_key
		else:
			self.__sub_insert(self.root, insert_key)

	# pre 0, in 1, post 2
	def __pre_order(self, node):
		print(node.key, end=' ')
		if node.left:
			node = node.left
			if node.left == None:
				return
			self.__pre_order(node)
		if node.right:
			node = node.right
			if node.right == None:
				return
			self.__pre_order(node)

	def search(self, num):
		if num == 0:
			self.__pre_order(self.root)
		elif num == 1:
			pass
		elif num == 2:
			pass

	# def delete(self):

	# def max_of_tree(self):

	# def min_of_tree(self):

	# def hight(self):
	
a = Tree()
b = Node()
print(a.root.key)
print(b.key)

bst = Tree()
for i in range(12):
	tmp = int(input())
	bst.inset(tmp)

bst.search(0)