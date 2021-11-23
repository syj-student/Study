import itertools

def solution(numbers):
	return str(int(''.join(sorted(map(str, numbers),reverse=True, key=lambda x: 3*x))))