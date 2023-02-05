from itertools import product

a = [1, 2]
b = [3, 4]
print(*list(product(a, b)), sep="\n")