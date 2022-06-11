import sys

input = sys.stdin.readline

int(input())
lst = sorted(map(int, input().split()), reverse=True)
print(lst)

acc = 0
answer = 0
while lst:
	cur = lst.pop()
	answer += cur + acc
	acc += cur
print(answer)