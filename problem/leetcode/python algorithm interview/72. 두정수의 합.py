# https://leetcode.com/problems/sum-of-two-integers/

class Solution:
	def getSum(self, a: int, b: int) -> int:
		a, b = list(bin(a)[2:]), list(bin(b)[2:])

