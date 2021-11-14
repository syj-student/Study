# https://leetcode.com/problems/fibonacci-number/

class Solution:
	def fib(self, n: int) -> int:
		if n <= 1:
			return n
		tmp1, tmp0 = 1, 0
		for i in range(1, n):
			tmp = tmp1 + tmp0
			tmp1, tmp0 = tmp, tmp1
		return tmp