# from collections import defaultdict
# import heapq

# def solution(tickets):
# 	route = []
# 	graph = defaultdict(list)
# 	for departure, arrival in tickets:
# 		heapq.heappush(graph[departure], arrival)
# 	stack = ['ICN']
# 	while stack:
# 		tmp = stack[-1]
# 		if not graph[tmp]:
# 			route.append(stack.pop())
# 		else:
# 			stack.append(heapq.heappop(graph[tmp]))
# 	route.reverse()
# 	return route

from collections import defaultdict
def solution(tickets):
    r = defaultdict(list)
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []
    while s:
        q = s[-1]
        if r[q] != []:
            s.append(r[q].pop())
        else:
            p.append(s.pop())
    return p[::-1]
print(solution([['ICN', 'AAA'], ['ICN', 'BBB'], ['BBB', 'TES']]))