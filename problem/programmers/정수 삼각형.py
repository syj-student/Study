def solution(triangle):
	for i in range(len(triangle)-1):
		case = [0 for _ in range(len(triangle[i+1]))]
		for j in range(len(triangle[i])):
			case[j] = max(triangle[i][j] + triangle[i+1][j], case[j])
			case[j+1] = max(triangle[i][j] + triangle[i+1][j+1], case[j+1])
		triangle[i+1] = case
	return max(case)