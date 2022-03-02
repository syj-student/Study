class Node:
    height = 1

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self, root: Node = None):
        self.root = root

    def __LLcase(self, node):
        now = node
        left = node.left
        left_left = node.left.left

    def __LRcase(self, node):
        now = node
        left = node.left
        left_right = node.left.right

    def __RRcase(self, node):
        now = node
        right = node.right
        right_right = node.right.right

    def __RLcase(self, node):
        now = node
        right = node.right
        right_left = node.right.left

    def __get_height(node):
        return node.height if node else 0

    def __get_balance_factor(node):
        return self.__get_height(node.left) - self.__get_height(node.right)

    def __set_height(node):
        return max(self.__get_height(node.left), self.__get_height(node.right)) + 1

    def __balancing(node):
        bf = self.__get_balance_factor(node)
        if bf < -1:
            if bf <= -1:
                node = self.__RLcase(node)
            else:
                node = self.__RRcase(node)
        elif bf > 1:
            if bf >= 1:
                node = self.__LRcase(node)
            else:
                node = self.__LLcase(node)
        node = self.__set_height(node)
        return node

    def dfs(node, val):
        if not node:
            node = Node(val)
        if node.val < val:
            node.right = self.dfs(node.right, val)
            node = self.__balancing(node)
        elif node.val > val:
            node.left = self.dfs(node.left, val)
            node = self.__balancing(node)

    def insert(self, val):
        # check if node in tree
        if not self.root:
            self.root = Node(val)
        else:
            pass

    def delete(self):
        pass

    def search(self, val):
        node = self.root
        while node:
            if node.val == val:
                return True
            elif node.val < val:
                node = node.right
            else:
                node = node.left
        return False
