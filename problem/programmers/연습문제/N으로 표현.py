def solution(N, number):
	dp_table = [set() for _ in range(9)]
	for i in range(1, 9):
		dp_table[i].add(int(str(N) * i))
		for k in range(1, i):
			if k <= i - k:
				y = i - k
				for x in dp_table[k]:
					for j in dp_table[y]:
						dp_table[i].add(j + x)
						dp_table[i].add(j - x)
						dp_table[i].add(j * x)
						dp_table[i].add(x - j)
						if x != 0:
							dp_table[i].add(j // x)
						if j != 0:
							dp_table[i].add(x // j)
		if number in dp_table[i]:
			return i
	return -1