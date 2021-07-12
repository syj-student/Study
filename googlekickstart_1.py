import sys

input = sys.stdin.readline

n = int(input().strip())
graph = list()
for __ in range(n):
	graph.append([list(map(int, input().strip().split())) for __ in range(3)])

for m in range(n):
	ret = 0
	ret_max = 0
	x_list = set()
	if (graph[m][0][1] + graph[m][2][1]) % 2 == 0:
		x_list.add(int((graph[m][0][1] + graph[m][2][1]) / 2))

	if (graph[m][1][0] + graph[m][1][1]) % 2 == 0:
		x_list.add(int((graph[m][1][0] + graph[m][1][1]) / 2))

	if (graph[m][0][0] + graph[m][2][2]) % 2 == 0:
		x_list.add(int((graph[m][0][0] + graph[m][2][2]) / 2))

	if (graph[m][0][2] + graph[m][2][0]) % 2 == 0:
		x_list.add(int((graph[m][0][2] + graph[m][2][0]) / 2))

	if graph[m][0][0] - graph[m][0][1] ==  graph[m][0][1] - graph[m][0][2]:
		ret += 1
	if graph[m][0][0] - graph[m][1][0] ==  graph[m][1][0] - graph[m][2][0]:
		ret += 1
	if graph[m][2][0] - graph[m][2][1] ==  graph[m][2][1] - graph[m][2][2]:
		ret += 1
	if graph[m][0][2] - graph[m][1][1] ==  graph[m][1][1] - graph[m][2][2]:
		ret += 1
	for x in x_list:
		tmp = 0
		graph[m][1].insert(1, x)
		if graph[m][0][1] - graph[m][1][1] ==  graph[m][1][1] - graph[m][2][1]:
			tmp += 1
		if graph[m][1][0] - graph[m][1][1] ==  graph[m][1][1] - graph[m][1][2]:
			tmp += 1
		if graph[m][0][0] - graph[m][1][1] ==  graph[m][1][1] - graph[m][2][2]:
			tmp += 1
		if graph[m][0][2] - graph[m][1][1] ==  graph[m][1][1] - graph[m][2][0]:
			tmp += 1
		graph[m][1].pop(1)
		if ret_max < tmp:
			ret_max = tmp
	print(f'Case #{m + 1}: {ret + ret_max}')
