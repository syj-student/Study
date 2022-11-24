from collections import defaultdict
import heapq

def solution(X, Y):
    answer = ''
    x, y = sorted(X, reverse=True), sorted(Y, reverse=True)
    i, j = 0, 0
    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            answer += x[i]
            i, j = i+1, j+1
        elif x[i] > y[j]:
            i += 1
        else:
            j += 1
    if answer == '':
        return "-1"
    return str(int(answer))