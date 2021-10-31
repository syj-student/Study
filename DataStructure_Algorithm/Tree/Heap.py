class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.parent = None
		self.left = left
		self.right = right


class heap:
	def __init__(self):
		self.root = None
		self.len = 0
	
	def __len__(self):
		return self.len

	def insert(self, val):
		if self.root is None:
			self.root = TreeNode(val)
			self.insert_position = self.root.left
			return
		