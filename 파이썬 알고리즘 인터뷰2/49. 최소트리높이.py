# https://leetcode.com/problems/minimum-height-trees/
import collections

class Solution:
	def findMinHeightTrees(self, n, edges):
		def dfs(start, depth, limit):
			print(depth, limit)
			if depth > limit:
				flag = True
				return
			if depth <= limit:
				min_node = depth
				answer.append(start)
				return
			print("check")
			for i in graph_map[start]:
				if i in graph_map:
					dfs(i, depth + 1, limit)
				

		graph_map = collections.defaultdict(list)
		for f, t in edges:
			graph_map[f].append(t)
		min_node = n
		flag = False
		answer = list()
		for i in sorted(graph_map, reverse=True):
			dfs(i, 0, min_node)
			print(flag, min_node, answer)
			if flag:
				return answer

a = Solution()
print(a.findMinHeightTrees(3, [[1,0],[1,2],[1,3]]))