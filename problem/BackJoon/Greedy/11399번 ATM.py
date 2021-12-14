import sys
import collections

n = int(sys.stdin.readline())
input_ = list(map(int, sys.stdin.readline().split()))
input_.sort(reverse=True)

answer = 0
acc = 0
for _ in range(n):
	x = input_.pop()
	acc += x
	answer += acc
print(answer)