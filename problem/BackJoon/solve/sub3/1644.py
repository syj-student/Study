n = int(input())
number = [1] * (n+1)
r = int(len(number) ** 0.5) + 1
prime = list()
for i in range(2, r):
	if number[i] == 1:
		prime.append(i)
		for j in range(i, len(number), i):
			number[j] = 0
for i in range(r, len(number)):
	if number[i] == 1:
		prime.append(i)
answer = 0
left = right = 0
s = 0
while True:
	if s == n:
		answer += 1
		if right == len(prime):
			break
		s += prime[right]
		right += 1
	elif s > n:
		s -= prime[left]
		left += 1
	else:
		if right == len(prime):
			break
		s += prime[right]
		right += 1
print(answer)