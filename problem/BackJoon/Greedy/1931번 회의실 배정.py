import sys

n = int(input())
schedules = list()
for _ in range(n):
	start, end = map(int, sys.stdin.readline().strip().split())
	schedules.append((end, start))
schedules.sort()
answer = 1
end = schedules[0][0]
for i in range(1, len(schedules)):
	if schedules[i][1] >= end:
		answer += 1
		end = schedules[i][0]

print(answer)