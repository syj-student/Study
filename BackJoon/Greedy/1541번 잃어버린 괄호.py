import sys

input = sys.stdin.readline

# parsing
prob = input().strip()
# casting
length = len(prob)
i = 0
ret = 0
tmp = 0
flag = False
while i < length:
	if prob[i] == '-':
		flag = True
	if '0' <= prob[i] <= '9':
		tmp = tmp * 10 + int(prob[i])
	else:
		if flag:
			ret -= tmp
		else:
			ret += tmp
		flag = False
		tmp = 0
	i += 1

print(ret)