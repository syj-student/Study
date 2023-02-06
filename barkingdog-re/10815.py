from sys import stdin

input = stdin.readline

number_length = int(input())
number = set(map(int, input().split()))
_ = int(input())
answer = list()
for i in map(int, input().split()):
    answer.append(1 if i in number else 0)
print(*answer)
