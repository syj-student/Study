def turn_key(key):
    m = len(key)
    new_key = [[0] * m for _ in range(m)]
    i = m-1
    for l in key:
        for j, n in enumerate(l):
            new_key[j][i] = n
        i -= 1
    return new_key

def can_open(holes, checker_box, m):
    for x, y in holes:
        if checker_box[m+x][m+y] == 0:
            return False
    return True

def solution(key, lock):
    m, n = len(key), len(lock)
    check_box = [[0] * (m*2+n) for _ in range(m*2+n)]
    holes = set()
    for i in range(n):
        for j in range(n):
            check_box[i+m][j+m] = lock[i][j]
            if lock[i][j] == 0:
                holes.add((i, j))

    key_holes = set()
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                key_holes.add((i, j))

    for r in range(4):
        for x in range(1, m+n):
            for y in range(1, m+n):
                for i, j in key_holes:
                    point_x, point_y = x+i, y+j
                    if m <= point_x < m+n and m <= point_y < m+n:
                        if check_box[point_x][point_y] == 1:
                            break
                        check_box[point_x][point_y] = 1
                else:
                    if can_open(holes, check_box, m):
                        return True

                for o, p in holes:
                    check_box[o+m][p+m] = 0

        if r == 3:
            break
        key = turn_key(key)
        key_holes = set()
        for i in range(m):
            for j in range(m):
                if key[i][j] == 1:
                    key_holes.add((i, j))
    return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))