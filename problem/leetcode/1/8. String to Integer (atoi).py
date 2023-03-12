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

class Solution:
    def myAtoi(self, s: str) -> int:
        answer = 0
        sign = 1
        i = 0
        while i < len(s) and s[i].isspace():
            i += 1
        while i < len(s):
            if s[i] == '-':
                sign *= -1
            elif s[i] == '+':
                i += 1
                continue
            else:
                break
            i += 1
        while i < len(s):
            if s[i].isdigit():
                answer = answer * 10 + int(s[i])
            else:
                break
            i += 1

        answer = sign * answer
        lhs, rhs = -2 ** 31, 2 ** 31 -1
        if lhs > answer: return lhs
        if rhs < answer: return rhs
        return answer
print(Solution().myAtoi("42"))