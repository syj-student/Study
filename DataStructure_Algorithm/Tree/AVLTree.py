class Node:
	def __init__(self, val):
		self.val = val
		self.height = 1
		self.left = None
		self.right = None

class AVLtree:
	def __init__(self):
		self.__root = None

	def insert(self, val):
		def getNodeHeight(node):
			return node.height if node else 0

		def getBalanceFactor(node):
			return getNodeHeight(node.left) - getNodeHeight(node.right)

		def setNodeHeight(node):
			return max(getNodeHeight(node.left), getNodeHeight(node.right)) + 1

		def LLrotation(node):
			node, node.right, node.right.left = node.left, node, node.left.right
			return node

		def LRrotation(node):
			tmp_l, tmp_r = node.left.right.left, node.left.right.right
			node, node.left, node.right = node.left.right, node.left, node
			node.left.right, node.right.left = tmp_l, tmp_r
			return node

		def RRrotation(node):
			node, node.left, node.left.right = node.right, node, node.right.left
			return node

		def RLrotation(node):
			tmp_l, tmp_r = node.right.left.left, node.right.left.right
			node, node.left, node.right = node.right.left, node, node.right
			node.left.right, node.right.left = tmp_l, tmp_r
			return node

		def balanceHeight(node):
			balance_factor = getBalanceFactor(node)
			if balance_factor <= -2:
				if getBalanceFactor(node.right) <= -1:
					node = RRrotation(node)
				else:
					node = RLrotation(node)
			elif balance_factor >= 2:
				if getBalanceFactor(node.left) >= 1:
					node = LLrotation(node)
				else:
					node = LRrotation(node)
			node.height = setNodeHeight(node)
			return node

		def searchPositionAndInsert(node):
			if node is None:
				node = Node(val)
			elif node.val > val:
				node.left = searchPositionAndInsert(node.left)
				node = balanceHeight(node)
			elif node.val < val:
				node.right = searchPositionAndInsert(node.right)
				node = balanceHeight(node)
			else:
				print("Exist same value")
			return node

		self.__root = searchPositionAndInsert(self.__root)

	def printRoot(self):
		print(self.__root.val, self.__root.left, self.__root.right)

	def preorder(self):
		def dfs(node, depth=0):
			if node is None:
				return
			dfs(node.right, depth + 1)
			print(f'{"    " * depth}{node.val}({node.height})')
			dfs(node.left, depth + 1)

		dfs(self.__root)

a = AVLtree()
a.insert(30)
a.insert(20)
a.insert(25)
a.insert(40)
a.insert(50)
a.insert(10)
a.insert(15)
a.printRoot()
print()
a.preorder()
