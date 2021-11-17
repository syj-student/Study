# https://leetcode.com/problems/assign-cookies/

class Solution:
	def findContentChildren(self, g, s) -> int:
		g.sort()
		s.sort()
		g_i, s_i = 0, 0
		while g_i < len(g) and s_i < len(s):
			if g[g_i] <= s[s_i]:
				g_i += 1
			s_i += 1
		return g_i

a = Solution()
print(a.findContentChildren([1,2,3], [1,1]))