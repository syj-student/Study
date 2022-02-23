class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = list()
        for i in range(1, n + 1):
            t = i % 3
            f = i % 5
            if t == f == 0:
                answer.append('FizzBuzz')
            elif t == 0:
                answer.append('Fizz')
            elif f == 0:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        return answer


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(i) for i in range(1, n+1)]
        x = 2
        while x < n:
            answer[x] = 'Fizz'
            x += 3
        x = 4
        while x < n:
            answer[x] = 'Buzz'
            x += 5
        x = 14
        while x < n:
            answer[x] = 'FizzBuzz'
            x += 15
        return answer
