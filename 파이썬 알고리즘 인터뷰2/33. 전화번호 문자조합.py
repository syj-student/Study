# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
	def letterCombinations(self, digits):
		def rec(digits, path="", depth=0, limit=len(digits)):
			if depth == limit:
				answer.append(path)
				return
			if digits[depth] in numberMap.keys():
				for c in numberMap[digits[depth]]:
					tmp = path
					path += c
					rec(digits, path, depth + 1)
					path = tmp

		answer = list()
		if not digits:
			return list()
		numberMap = {
			"2" : "abc",
			"3" : "def",
			"4" : "ghi",
			"5" : "jkl",
			"6" : "mno",
			"7" : "pqrs",
			"8" : "tuv",
			"9" : "wxyz"
		}
		rec(digits)
		return answer