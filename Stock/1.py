def solution(survey, choices):
	score = {
		"R": 0, "T": 0,
		"C": 0, "F": 0,
		"J": 0, "M": 0,
		"A": 0, "N": 0,
	}
	for s, c in zip(survey, choices):
		if c == 4:
			continue
		if c <= 3:
			score[s[0]] += 4 - c
		else:
			score[s[1]] += c - 4
	answer = ""
	if score["R"] >= score["T"]:
		answer += "R"
	else:
		answer += "T"
	if score["C"] >= score["F"]:
		answer += "C"
	else:
		answer += "F"
	if score["J"] >= score["M"]:
		answer += "J"
	else:
		answer += "M"
	if score["A"] >= score["N"]:
		answer += "A"
	else:
		answer += "N"
	return answer