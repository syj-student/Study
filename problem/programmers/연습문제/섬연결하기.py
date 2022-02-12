def solution(n, costs):
	def check_parent(n):
		while linked[n] != n:
			n = linked[n]
		return n

	linked = [i for i in range(n)]
	answer = 0
	bridges = 0
	costs.sort(reverse=True, key=lambda x : x[2])
	while costs:
		d, a, c = costs.pop()
		parent_d = check_parent(d)
		parent_a = check_parent(a)
		if parent_a != parent_d:
			answer += c
			bridges += 1
			linked[parent_d] = parent_a
		print(parent_d, parent_a, linked)
	print(linked)
	return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))