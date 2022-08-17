import bisect

lst = [1]
lst.pop()
idx = bisect.bisect_left(lst, 2, 0, 1)
print(idx)
idx = bisect.bisect_right(lst, 1)
print(idx)
