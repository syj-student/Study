import sys

line = sys.stdin.readline()
line = line.split('-')
answer = sum(map(int, line.pop(0).split('+')))
for l in line:
	answer -= sum(map(int, l.split('+')))
print(answer)