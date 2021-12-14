class Solution:
	def reverse(self, x: int) -> int:
		sign = 1
		if x < 0:
			sign = -1
			x *= -1
		answer = sign * int(''.join(reversed(str(x))))
		if -2 ** 31 <= answer <= (2 ** 32) - 1:
			return answer
		return 0
a = Solution()
a.reverse(100)