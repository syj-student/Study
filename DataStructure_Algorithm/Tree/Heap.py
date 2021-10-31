import collections


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.parent = None
		self.left = left
		self.right = right


class heap:
	def __init__(self):
		self.tree = [None]
	
	def __len__(self):
		return len(self.tree) - 1

	def __str__(self):
		if len(self) == 0:
			return "None"
		return str(self.tree[1:])

	def insert(self, val):
		self.tree.append(val)
		child_index = len(self.tree) - 1
		parent_index = child_index // 2
		while parent_index:
			if self.tree[parent_index] > self.tree[child_index]:
				self.tree[parent_index], self.tree[child_index] = self.tree[child_index], self.tree[parent_index]
			child_index //= 2
			parent_index = child_index // 2

	def pop(self):
		if len(self) == 0:
			return
		if len(self) == 1:
			return self.tree.pop()
		ret = self.tree[1]
		self.tree[1] = self.tree.pop()
		index = 1
		while True:
			left, right = index*2, index*2 + 1
			smallest = index
			if left <= len(self) and self.tree[left] < self.tree[index]:
				smallest = left
			if right <= len(self) and self.tree[right] < self.tree[smallest]:
				smallest = right
			if smallest != index:
				self.tree[smallest], self.tree[index] = self.tree[index], self.tree[smallest]
				index = smallest
			else:
				break
		return ret
a = heap()
b = [10, 5, 8, 7, 7]
for i in b:
	a.insert(i)
print(a)
print(a.pop(), a)
print(a.pop(), a)
print(a.pop(), a)
print(a.pop(), a)
print(a.pop(), a)
