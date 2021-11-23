def solution(n, computers):
	answer = 0
	visited = [False] * n
	for i in range(n):
		if visited[i]:
			continue
		stack = [i]
		while stack:
			node = stack.pop()
			visited[node] = True
			for j in range(n):
				if computers[node][j] and visited[j] == False:
					stack.append(j)
		answer += 1
	return answer