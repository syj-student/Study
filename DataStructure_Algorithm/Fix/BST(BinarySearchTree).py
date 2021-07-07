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

	def __init__(self):
		self.root = Node()
		self.height = None
		self.max = None
		self.min = None

	#
	def __sub_insert(self, node, insert_key):
		if insert_key >= node.key:
			if node.right == None:
				node.right = Node(key= insert_key, level= node.level + 1)
				if node.right.level > self.height:
					self.height = node.right.level
				return 
			self.__sub_insert(node.right, insert_key)
		else:
			if node.left == None:
				node.left = Node(key= insert_key, level= node.level + 1)
				if node.left.level > self.height:
					self.height = node.left.level
				return 
			self.__sub_insert(node.left, insert_key)

	def inset(self, insert_key):
		if self.root.key == None:
			self.root.key = insert_key
			self.height = 0
			self.max = self.root.key
			self.min = self.root.key
		else:
			self.__sub_insert(self.root, insert_key)
			if insert_key > self.max:
				self.max = insert_key
			elif insert_key < self.min:
				self.min = insert_key

	# pre 0, in 1, post 2
	def __pre_order(self, node):
		print(node.key, end=' ')
		if node.left == None:
			pass
		else:
			self.__pre_order(node.left)
		if node.right == None:
		else:
			self.__pre_order(node.right)

	def __in_order(self, node):
		if node.left == None:
			pass
		else:
			self.__in_order(node.left)
		print(node.key, end=' ')
		if node.right == None:
			pass
		else:
			self.__in_order(node.right)

	def __post_order(self, node):
		if node.left == None:
			pass
		else:
			self.__post_order(node.left)
		if node.right == None:
			pass
		else:
			self.__post_order(node.right)
		print(node.key, end=' ')

	def search(self, num):
		if num == 0:
			self.__pre_order(self.root)
		elif num == 1:
			self.__in_order(self.root)
		elif num == 2:
			self.__post_order(self.root)

	# def delete(self, del_key):

	def max_of_tree(self):
		print(self.max)

	def min_of_tree(self):
		print(self.min)

	def tree_height(self):
		print(self.height)

bst = Tree()
for i in [50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24]:
	bst.inset(i)

bst.search(0)
print()
bst.search(1)
print()
bst.search(2)
print()
bst.max_of_tree()
bst.min_of_tree()
bst.tree_height()

# search() true false
# while 재작성
# del 작성