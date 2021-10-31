class Codec:
	
	def serialize(self, root):
		queue = collections.deque([root])
		stack = ['#']
		while queue:
			node = queue.popleft()
			if node:
				queue.append(node.left)
				queue.append(node.right)
				stack.append(str(node.val))
			else:
				stack.append('#')
		return ' '.join(stack)
		

	def deserialize(self, data):
		if data == '# #':
			return
		node_values = data.split()
		root = TreeNode(int(node_values[1]))
		q = collections.deque([root])
		i = 2
		while q:
			node = q.popleft()
			if node_values[i] is not '#':
				node.left = TreeNode(int(node_values[i]))
				q.append(node.left)
			i += 1
			if node_values[i] is not '#':
				node.right = TreeNode(int(node_values[i]))
				q.append(node.right)
			i += 1
		return root