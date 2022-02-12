def solution(n, k):
    def check_prime(num):
        if num <= 1:
            return 0
        i = num ** (0.5)
        x = 2
        while x <= i:
            if num % x == 0:
                return 0
            x += 1
        return 1

    nk = ''
    while n != 0:
        n, b = divmod(n, k)
        nk += str(b)
    nk_list = nk.split('0')
    answer = 0
    for num in nk_list:
        if num != '':
            answer += check_prime(int(num[::-1]))
            print(answer)
    return answer
