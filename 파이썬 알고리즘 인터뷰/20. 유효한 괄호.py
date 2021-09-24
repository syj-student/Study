# https://leetcode.com/problems/valid-parentheses/

class Solution:
	def isValid(self, s):
		table = {')':'(', ']':'[', '}':'{'}
		stack = list()
		for c in s:
			if c in table.values():
				stack.append(c)
			elif c in table.keys():
				if not stack or not stack.pop() == table[c]:
					return False
		if stack:
			return False
		return True