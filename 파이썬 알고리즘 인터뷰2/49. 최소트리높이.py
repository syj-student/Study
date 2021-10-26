# https://leetcode.com/problems/minimum-height-trees/
import collections

class Solution:
	def findMinHeightTrees(self, n, edges):
		if n <= 1:
			print(n, edges)
			return [0]
		graph_map = collections.defaultdict(list)
		for f, t in edges:
			graph_map[f].append(t)
			graph_map[t].append(f)

		leafs = list()
		for key in graph_map.keys():
			if len(graph_map[key]) == 1:
				leafs.append(key)

		while n > 2:
			n -= len(leafs)
			tmp_leafs = list()
			for leaf in leafs:
				neighbnor = graph_map[leaf].pop()
				graph_map[neighbnor].remove(leaf)
				if len(graph_map[neighbnor]) == 1:
					tmp_leafs.append(neighbnor)
			leafs = tmp_leafs

		return leafs
a = Solution()
print(a.findMinHeightTrees(11, [[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9], [6, 0]]
))