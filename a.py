def cut(lst, num):
	print(id(lst))
	if lst[0] < num < lst[1]:
		print("in")
		print("in", id(lst[0]))
		lst[0] = [lst[0], num]
		print("in", id(lst[0]))
		print("in")

a = [1, 4]
print(id(a[0]))
cut(a, 2)
print(id(a[0]))
print(a)