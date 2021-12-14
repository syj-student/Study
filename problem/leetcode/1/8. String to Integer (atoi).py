class Solution:
	def myAtoi(self, s: str) -> int:
		s = s.strip()
		print
		tmp = ''
		i = 0
		sign = 1
		if i < len(s) and (s[i] == '-' or s[i] == '+'):
			if s[i] == '-':
				sign *= -1
			i += 1
		while i < len(s) and s[i].isnumeric():
			tmp += s[i]
			i += 1
		if tmp:
			tmp = sign * int(tmp)
			if tmp < -2 ** 31:
				return -2 ** 31
			if tmp > 2 ** 31 -1:
				return 2 ** 31 - 1
			return tmp
		return 0