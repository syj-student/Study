# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		start, end, maxSubstring = 0, 0, 0
		for c in s:
			if not c in s[start:end]:
				pass
			else:
				start = s[start:end].rindex(c) + start + 1
			end += 1
			maxSubstring = max(maxSubstring, end - start)
		return maxSubstring
