import itertools


def checker(l):
    vowel = set(['a', 'e', 'i', 'o', 'u'])
    l = set(l)
    sub = l - vowel
    if len(sub) >= 2 and len(sub) != len(l):
        return True
    return False


length, _ = map(int, input().split())
char = sorted(input().split())
cases = itertools.combinations(char, length)
for l in cases:
    if checker(l):
        print(''.join(l))
