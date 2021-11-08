# https://leetcode.com/problems/minimum-window-substring/
import collections
import sys
class Solution:
	def minWindow(self, s: str, t: str) -> str:
		if not s or len(s) < len(t):
			return ""
		result = list()
		for i in range(len(s)):
			if s[i] in t:
				result.append(i)

		if not result or len(result) < len(t):
			return ""
		k = len(t)
		comp = collections.deque([s[result[i]] for i in range(k)])
		t = sorted(t)
		if sorted(comp) == t:
			min_length = result[k-1] - result[0]
			ret = (result[0], result[k-1])
		else:
			min_length = sys.maxsize
			ret = None
		start = 1
		for i in range(k, len(result)):
			tmp = result[i] - result[start]
			comp.popleft()
			comp.append(s[result[i]])
			if sorted(comp) == t and min_length > tmp:
				ret = (result[start], result[i])
				min_length = tmp
			start += 1
		if ret:
			return s[ret[0]:ret[1]+1]
		return ""
a = Solution()
print(a.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))
