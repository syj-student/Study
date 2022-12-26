
from bisect import bisect_left
a = [i for i in range(51)]
left, right = 0, 50
val = 51
while left <= right:
    mid = (left+ right) // 2
    if a[mid] < val:
        left = mid + 1
    else:
        right = mid - 1
print(mid, bisect_left(a, -1))
