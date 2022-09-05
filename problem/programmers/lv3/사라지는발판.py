

def solution(board, aloc, bloc):
    no_board = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                no_board.add((i, j))
    a_move = 0
    b_move = 0
    
    def a_moving():
        nonlocal a_move
        dist = float('inf')
        ret = None
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        can = list()
        for x, y in zip(dx, dy):
            nx = aloc[0] + x
            ny = aloc[1] + y
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in no_board:
                can.append((nx, ny))
        if not can:
            return True
        for x, y in can:
            tmp = (x-bloc[0])**2 + (y-bloc[1])**2
            if tmp < dist:
                ret = (x, y)
                dist = tmp
            elif tmp == dist:
                for k, p in no_board:
                    if (x-k)**2 + (y-p)**2 > (ret[0]-k)**2 + (ret[1]-p)**2:
                        ret = (x, y)
                        break
        no_board.add((aloc[0], aloc[1]))
        aloc[0] = ret[0]
        aloc[1] = ret[1]
        a_move += 1
        return False
        

    def b_moving():
        nonlocal b_move
        dist = float('-inf')
        ret = None
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        can = list()
        for x, y in zip(dx, dy):
            nx = bloc[0] + x
            ny = bloc[1] + y
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in no_board:
                can.append((nx, ny))
        if not can:
            return True
        for x, y in can:
            tmp = (x-bloc[0])**2 + (y-bloc[1])**2
            if tmp > dist:
                ret = (x, y)
                dist = tmp
            elif tmp == dist:
                for k, p in no_board:
                    if (x-k)**2 + (y-p)**2 > (ret[0]-k)**2 + (ret[1]-p)**2:
                        ret = (x, y)
                        break
        no_board.add((bloc[0], bloc[1]))
        bloc[0] = ret[0]
        bloc[1] = ret[1]
        b_move += 1
        return False
    

    while True:
        if a_moving():
            break
        print(set(bloc))
        if (bloc[0], bloc[1]) in no_board:
            break
        if b_moving():
            break
    
    return a_move + b_move

print(solution(
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    [1, 0], [1, 2]
))