def test():
	a = [1, 2]
	yield a
	return 1
a = test()
print(next(a))
print(next(a))