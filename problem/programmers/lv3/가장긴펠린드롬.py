def solution(s):
    def checker(left, right):
        nonlocal s
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right-1
        return True
    answer = 0
    for i in range(len(s)):
        left = i - answer
        while 0 <= left:
            if checker(left, i):
                answer = max(answer, i-left+1)
            left -= 1
    return answer
print(solution("abcdcba"))
print(solution("abacde"))