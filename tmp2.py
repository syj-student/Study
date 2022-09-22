import bisect
from collections import deque

a = deque([0, 2, 2,3])
print(bisect.bisect_right(a, 2))
del a[1]
print(a)