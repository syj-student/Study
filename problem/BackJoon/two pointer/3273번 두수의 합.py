import sys


sys.stdin.readline()
lst = sorted(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

left, right = 0, len(lst) - 1
answer = 0
while left < right:
    two_sum = lst[left] + lst[right]
    if two_sum == target:
        answer += 1
        left += 1
        right -= 1
    elif two_sum < target:
        left += 1
    else:
        right -= 1
print(answer)
