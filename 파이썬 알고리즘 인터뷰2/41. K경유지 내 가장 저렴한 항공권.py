# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import collections
import heapq

class Solution:
	def findCheapestPrice(self, n, flights, src: int, dst: int, k: int) -> int:
		graph = collections.defaultdict(list)
		visited = dict()
		for departure, arrival, cost in flights:
			graph[departure].append((cost, arrival))
		
		Q = [(0, src, 0)]
		while Q:
			cost, departure, via_cnt = heapq.heappop(Q)
			if departure == dst:
				return cost
			if via_cnt <= k:
				if departure not in visited or visited[departure] > via_cnt:
					visited[departure] = via_cnt
					for add_cost, new_departure in graph[departure]:
						heapq.heappush(Q, (cost + add_cost, new_departure, via_cnt + 1))
		return -1

a = Solution()
print(a.findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0,3,1))
print("sdgf")

class Solution:
	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
		graph = collections.defaultdict(list)
		for u, v, w in flights:
			graph[u].append([v, w])
		visit = {}
		Q = [(0, src, 0)]
		while Q:
			price, node, k = heapq.heappop(Q)
			if node == dst:
				return price
			if node not in visit or visit[node] > k:
				visit[node] = k
				for v, w in graph[node]:
					if k <= K:
						alt = price + w
						heapq.heappush(Q, (alt, v, k + 1))
		return -1