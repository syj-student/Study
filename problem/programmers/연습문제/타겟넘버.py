def dfs(numbers, target, prev_sum=0, depth=0):
	if not numbers:
		if prev_sum == target:
			return 1
		return 0
	prev_p = prev_sum + numbers[0]
	prev_m = prev_sum - numbers[0]
	next_numbers = numbers[1:]
	return dfs(next_numbers, target, prev_p, depth + 1) + dfs(next_numbers, target, prev_m, depth + 1)

def solution(numbers, target):
	return dfs(numbers, target)


print(solution([1, 1, 1, 1, 1], 3))