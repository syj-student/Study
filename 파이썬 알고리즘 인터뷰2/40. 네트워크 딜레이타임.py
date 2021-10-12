# https://leetcode.com/problems/network-delay-time/#

class Solution:
	def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
		graph = collections.defaultdict(list)
		dist = collections.defaultdict(int)
		for start, dest, distance in times:
			graph[start].append((dest, distance))
		
		priority_Q = [(0, k)]
		while priority_Q:
			distance, node = heapq.heappop(priority_Q)
			if not node in dist:
				dist[node] = distance
				for next_node, add_distance in graph[node]:
					heapq.heappush(priority_Q, (distance + add_distance, next_node))

		if len(dist.keys()) == n:
			return max(dist.values())
		return -1