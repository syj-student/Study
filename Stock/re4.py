import collections
import copy

def solution(n, paths, gates, summits):
	t = collections.defaultdict(list)
	for p in paths:
		t[p[0]].append((p[2], p[1]))
		t[p[1]].append((p[2], p[0]))
	for k in t:
		t[k].sort()
	print(t)
	def find_way(start, end):
		dontgo = gates[:] + summits[:]
		dontgo.remove(end)

		intentsity = [float('inf')]
		def rec(now, itsy, visited=[False] * (n+1)):
			if now == end:
				intentsity[0] = min(intentsity[0], itsy)
				return
			visited[now] = True
			for cost, dest in t[now]:
				if not visited[dest] and not dest in dontgo:
					rec(dest, max(itsy, cost), copy.deepcopy(visited))
			else:
				return
		rec(start, 0)
		return intentsity[0]

	answer = [0, float('inf')]
	for g in gates:
		for s in summits:
			h = find_way(g, s)
			if answer[1] > h:
				answer[0] = s
				answer[1] = h
	return answer

print(solution(
7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]
))
