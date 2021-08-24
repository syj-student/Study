# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
	def longestPalindrome(self, s: str) -> str:
		s_len = len(s)
		if s_len == 1 or s == s[::-1]:
			return s
		def range_expand(left: int, right: int) -> str:
			while left >= 0 and right < s_len and s[left] == s[right]:
				left -= 1
				right += 1
			return s[left + 1:right]
		ret = ""
		for i in range(s_len - 1):
			ret = max(ret, range_expand(i, i + 2), range_expand(i, i + 3), key=len)
		return ret
s = "babadadadada"
asd = Solution()
print(asd.longestPalindrome(s))