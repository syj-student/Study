from pprint import pprint

def solution(rows, columns, queries):
    m = [[0]*columns for _ in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            m[i][j] = n
            n += 1
    pprint(m)
    answer = []
    for a, b, x, y in queries:
        pass
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))