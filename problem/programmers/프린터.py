import collections

def solution(priorities, location):
	answer = 1
	priorities = collections.deque(list(enumerate(priorities)))
	while priorities:
		if priorities[0][1] >= max(priorities, key=lambda x:x[1])[1]:
			check = priorities.popleft()
			if check[0] == location:
				return answer
			else:
				answer += 1
		else:
			priorities.rotate(-1)