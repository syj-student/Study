from pprint import pprint

def solution(rows, columns, queries):
    answer = []
    m = [[0]*columns for _ in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            m[i][j] = n
            n += 1

    for l in queries:
        a, b, x, y = map(lambda x: x-1, l)
        small = float('inf')
        prev = float('inf')
        for i in range(b, y+1):
            small = min(small, m[a][i])
            prev, m[a][i] = m[a][i], prev
        for i in range(a+1, x+1):
            small = min(small, m[i][y])
            prev, m[i][y] = m[i][y], prev
        for i in range(y-1, b-1, -1):
            small = min(small, m[x][i])
            prev, m[x][i] = m[x][i], prev
        for i in range(x-1, a-1, -1):
            small = min(small, m[i][b])
            prev, m[i][b] = m[i][b], prev
        answer.append(small)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))