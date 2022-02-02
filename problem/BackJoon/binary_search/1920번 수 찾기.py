from sys import stdin


stdin.readline()
x = set(stdin.readline().split())
stdin.readline()
answer = stdin.readline().split()
for c in answer:
    print(1 if c in x else 0)
