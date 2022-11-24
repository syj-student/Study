def rotate(a):
    row_length = len(a)
    column_length = len(a[0])
    
    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length-1-r] = a[r][c]
    
    return res
a = rotate([[0, 1, 0],[1, 1, 1]])
print(a)
a = rotate(a)
print(a)
a = rotate(a)
print(a)
a = rotate(a)
print(a)