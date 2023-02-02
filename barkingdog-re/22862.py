from sys import stdin
from collections import deque

input = stdin.readline

length, remove_count = map(int, input().split())
original_count = remove_count
lst = list(map(int, input().split()))
dq = deque()
answer = left = right = 0

def is_even(n):
    return False if n % 2 else True

while right < len(lst):
    isEven = is_even(lst[right])
    if isEven:
        dq.append(lst[right])
        right += 1
        answer = max(answer, len(dq) - (original_count - remove_count))
    else:
        if remove_count > 0:
            dq.append(lst[right])
            right += 1
            remove_count -= 1
        else:
            while dq:
                now = dq.popleft()
                isEven = is_even(now)
                if not isEven:
                    remove_count += 1
                    break

print(answer)
