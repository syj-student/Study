# https://leetcode.com/problems/climbing-stairs/

class Solution:
	dp_table = collections.defaultdict(int)
	def climbStairs(self, n: int) -> int:
		if n <= 2:
			return n
		if self.dp_table[n]:
			return self.dp_table[n]
		self.dp_table[n] = self.climbStairs(n-1)+ self.climbStairs(n-2)
		return self.dp_table[n]