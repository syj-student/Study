def solution(array, commands):
	answer = list()
	for i, j, k in commands:
		answer.append(sorted(array[i-1:j])[k-1])
	return answer