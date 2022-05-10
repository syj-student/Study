import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
dp = [0] * len(s2)
for i in range(len(s1)):
	cnt = 0
	for j in range(len(s2)):
		if cnt < dp[j]:
			cnt = dp[j]
		elif s1[i] == s2[j]:
			dp[j] = cnt + 1
print(max(dp))