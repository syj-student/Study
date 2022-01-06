import sys

sys.stdin.readline()
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
left, right = 0, len(lst) - 1
concentration = sys.maxsize
answer = [0, 0]
while left < right:
    mixed = lst[left] + lst[right]
    if mixed == 0:
        answer = [lst[left], lst[right]]
        break
    if abs(mixed) < abs(concentration):
        answer, concentration = [lst[left], lst[right]], mixed
    if mixed < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])
