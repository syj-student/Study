class Codec:
	
	def serialize(self, root):
		q = collections.deque([root])
		result = ['#']
		while q:
			node = q.popleft()
			if node:
				q.append(node.left)
				q.append(node.right)
				result.append(str(node.val))
			else:
				result.append('#')
		return ' '.join(result)
		

	def deserialize(self, data):
		if data == '# #':
			return None
		nodes = data.split()
		root = TreeNode(int(nodes[1]))
		q = collections.deque([root])
		idx = 2
		while q:
			node = q.popleft()
			if nodes[idx] is not '#':
				node.left = TreeNode(int(nodes[idx]))
				q.append(node.left)
			idx += 1
			if nodes[idx] is not '#':
				node.right = TreeNode(int(nodes[idx]))
				q.append(node.right)
			idx += 1
		return root