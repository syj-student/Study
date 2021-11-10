def fractional_knapsack(cargo):
	capacity = 15
	pack = list()
	for c in cargo:
		pack.append((c[0]/c[1], c[0], c[1]))
	pack.sort(reverse=True)
	total_value: float = 0
	for p in pack:
		if capacity -p[2] >= 0:
			capacity -= p[2]
			total_value += p[1]
		else:
			fraction = capacity / p[2]
			total_value += p[1] * fraction
			break
	return total_value

cargo = [
	(20, 15),
	(3, 2),
	(3, 2),
	(3, 2),
	(3, 2),
	(3, 2),
	(3, 2),
	(3, 2)
]

print(fractional_knapsack(cargo))