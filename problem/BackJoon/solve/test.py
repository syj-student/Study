import itertools
import sys

lst = [i for i in range(10)]
con = itertools.permutations(lst, 10)
print(sys.getsizeof(con))
