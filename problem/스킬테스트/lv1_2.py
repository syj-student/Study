from collections import Counter

def solution(X, Y):
    comb = Counter(X) & Counter(Y)
    if not comb:
        return "-1"
    answer = list()
    for i in range(9, -1, -1):
        i = str(i)
        if comb[i]:
            answer.append(comb[i] * i)
    if answer[0][0] == '0':
        return '0'
    return ''.join(answer)

print(solution(	"12321", "42531"))