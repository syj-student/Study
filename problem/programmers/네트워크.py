def solution(n, computers):
	answer = 0
	visited = [False] * n
	for i in range(n):
		if visited[i]:
			continue
		stack = [i]
		visited[i] = True
		while stack:
			node = stack.pop()
			for j in range(n):
				if computers[node][j] and visited[j] == False:
					visited[j] = True
					stack.append(j)
		answer += 1
	return answer