import bisect
from collections import deque
a = deque([1, 0])
print(bisect.bisect_right(a, 1))