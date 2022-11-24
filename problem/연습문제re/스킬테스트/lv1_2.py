from collections import Counter

def solution(X, Y):
    comb = Counter(X) & Counter(Y)
    if not comb:
        return "-1"
    answer = ''
    for i in range(9, -1, -1):
        i = str(i)
        if comb[i]:
            answer += comb[i] * i
    return str(int(answer))

print(solution(	"12321", "42531"))