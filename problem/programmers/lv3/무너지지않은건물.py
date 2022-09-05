
def solution(board, skill):
    tmp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for l in skill:
        effect = l[5] * (-1 if l[0] == 1 else 1)
        tmp[l[1]][l[2]] += effect
        tmp[l[3]+1][l[2]] += -effect
        tmp[l[1]][l[4]+1] += -effect
        tmp[l[3]+1][l[4]+1] += effect

    for i in range(len(board)):
        for j in range(len(board[0])):
            tmp[i][j+1] += tmp[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            tmp[i+1][j] += tmp[i][j]

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            answer += 1 if board[i][j]+tmp[i][j] > 0 else 0
    return answer

a = solution(
    [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
    [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
)
print(a)