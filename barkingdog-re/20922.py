from sys import stdin
from collections import defaultdict

input = stdin.readline
length, lim = map(int, input().split())
number = list(map(int, input().split()))
counter = defaultdict(int)
answer = start = 0

for end, now in enumerate(number):
    # Count each number
    counter[now] += 1
    # Check repeat limit
    if counter[now] <= lim:
        answer = max(answer, end - start + 1)
    else:
        while counter[now] > lim:
            counter[number[start]] -= 1; start += 1
    
    # Check Remain elements count
    if length - start <= answer:
        break

print(answer)
