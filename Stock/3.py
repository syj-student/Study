def solution(alp, cop, problems):
	answer = float('inf')
	eff_a = [0, 0, 1, 0, 1]
	eff_c = [0, 0, 0, 1, 1]
	for p in problems:
		tmp_alp, tmp_cop = alp, cop
		tmp_score = 0
		if tmp_alp < p[0]:
			tmp_score += p[0] - tmp_alp
			tmp_alp = p[0]
		if tmp_cop < p[1]:
			tmp_score += p[1] - tmp_cop
			tmp_cop = p[1]
		for pp in problems:
			if tmp_score >= answer:
				break
			if tmp_alp >= pp[0] and tmp_cop >= pp[1]:
				if eff_a[2] <= pp[2]
		answer = min(answer, tmp_score)
	return answer
print(solution(
10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))