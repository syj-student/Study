import sys

A, B, C = map(int, sys.stdin.readline().strip().split())
print(
    (A+B) % C,
    ((A % C) + (B % C)) % C,
    (A*B) % C,
    ((A % C) * (B % C)) % C,
    sep='\n')
