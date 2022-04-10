from pprint import pprint

a = [([0] * 10) for _ in range(10)]
a[0][0] = 1
pprint(a)
