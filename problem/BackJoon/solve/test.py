n = int(input())
number = [1] * (n+1)
r = int(len(number) ** 0.5) + 1
lst = list()
for i in range(2, r):
	if number[i] == 1:
		lst.append(i)
		for j in range(i, len(number), i):
			number[j] = 0
for i in range(r, len(number)):
	if number[i] == 1:
		lst.append(i)
left, answer, acc = 0, 0, 0
for i in range(len(lst)):
	acc += lst[i]
	if acc == n:
		answer += 1
	elif acc > n:
		while acc > n:
			acc -= lst[left]
			left += 1
		if acc == n:
			answer += 1
print(answer)