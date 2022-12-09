from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.color = 'red'
        self.val = val
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self, val):
        self.root = Node(val)
        self.root.color = 'black'

    def Search(self, val):
        def dfs(node):
            nonlocal val
            if node.val == val:
                return True
            if node == None:
                return False
            if node.val > val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        return dfs(self.root)

    def find_parent(self):
        pass

    def find_grandparent(self):
        pass

    def Insert(self, val):
        def dfs(node):
            nonlocal val
            if node.val > val:
                if node.left == None:
                    node.left = Node(val)
                    return
                dfs(node.left)
            else:
                if node.right == None:
                    node.right = Node(val)
                    return
                dfs(node.right)
        dfs(self.root)

    def Delete(self, val):
        pass

    def show(self):
        stack = deque([self.root])
        while stack:
            now = stack.popleft()
            print(now.val)
            if now.left:
                stack.append(now.left)
            if now.right:
                stack.append(now.right)

root = RedBlackTree(10)
root.Insert(20)
root.Insert(1)
root.show()