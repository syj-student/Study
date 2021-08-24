a = ['cde', 'cfc', 'abc']
def fn(s):
	return s[0], s[-1]

print(sorted(a, key=len))