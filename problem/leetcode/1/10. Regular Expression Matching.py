class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		s_idx = p_idx = 0
		while s_idx < len(s) and p_idx < len(p):
			if s[s_idx] == p[p_idx] or p[p_idx] == '.':
				s_idx += 1
				p_idx += 1
				continue
			if p[p_idx] == '*':
				return True
			return False
		return len(s) == len(p)