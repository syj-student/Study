import collections

class TrieNode:
	def __init__(self):
		self.word = False
		self.children = dict()

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		node = self.root
		for c in word:
			if c not in node.children:
				node.children[c] = TrieNode()
			node = node.children[c]
		node.word = True

	def search(self, word):
		node = self.root
		for c in word:
			if c not in node.children:
				return False
			node = node.children[c]
		return node.word

	def startsWith(self, prefix):
		node = self.root
		for c in prefix:
			if c not in node.children:
				return False
			node = node.children[c]
		return True

