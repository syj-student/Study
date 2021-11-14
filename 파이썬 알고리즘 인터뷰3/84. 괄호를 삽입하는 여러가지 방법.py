# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
	def diffWaysToCompute(self, expression):
		operation_symbols = ['+', '-', '*']
		result = list()
		for i in range(len(expression)):
			if expression[i] in operation_symbols:
				s1 = self.diffWaysToCompute(expression[:i])
				s2 = self.diffWaysToCompute(expression[i+1:])
				for x in s1:
					for y in s2:
						result.append(eval(str(x)+expression[i]+str(y)))
		if not result:
			return [eval(expression)]
		return result

a = Solution()
print(a.diffWaysToCompute("11"))

class Solution:
	def diffWaysToCompute(self, expression):
		def compute(left, right, op):
			results = []
			for l in left:
				for r in right:
					results.append(eval(str(l)+op+str(r)))
			return results

		if expression.isdigit():
			return [int(expression)]
		results = []
		for idx, val in enumerate(expression):
			if val in "-+*":
				left = self.diffWaysToCompute(expression[:idx])
				right = self.diffWaysToCompute(expression[idx+1:])
				results.extend(compute(left, right, val))
		return results