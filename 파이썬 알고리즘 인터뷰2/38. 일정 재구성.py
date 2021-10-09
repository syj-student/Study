# https://leetcode.com/problems/reconstruct-itinerary/

class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		graph = collections.defaultdict(list)
		for a, b in sorted(tickets, reverse=True):
			graph[a].append(b)

		route = list()
		def dfs(a):
			while graph[a]:
				dfs(graph[a].pop())
			route.append(a)
		dfs('JFK')
		return reversed(route)