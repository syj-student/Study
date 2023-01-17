import sys
from collections import Counter

input = sys.stdin.readline

left = Counter(input().strip())
right = Counter(input().strip())
answer = 0
for c in left.keys() | right.keys():
    answer += abs(left.get(c, 0)-right.get(c, 0))
print(answer)