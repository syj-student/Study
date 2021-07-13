a = [1, 2, 3]
b = ['a', 'b', 'c']
def abc(a, x):
	if x == 3:
		return
	x += 1
	a[0], a[1] = a[1], a[0]
	abc(a, x)
abc(b, 1)
print(b)