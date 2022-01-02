class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		res = []

		def helper(num ,l , r):
			if len(num) == 2 * n:
				res.append(num)
				return
			if l < n:
				helper(num + '(', l + 1, r)
			if r < l:
				helper(num + ')', l, r + 1)
		helper('', 0, 0)
		return res
