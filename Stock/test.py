import itertools

a = 'abc'

for i in itertools.permutations(a, 3):
    print(''.join(i))
