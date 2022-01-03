import sys

# parse
my_input = sys.stdin.readline
n = int(my_input())
Map = [list(map(int, my_input().split())) for _ in range(n)]


def rec(x, y, length):
    flag = 0
    for i in range(x, x+length):
        for j in range(y, y+length):
            if Map[x][y] != Map[i][j]:
                rec(x, y, length//2)
                rec(x, y+length//2, length//2)
                rec(x+length//2, y, length//2)
                rec(x+length//2, y+length//2, length//2)
                flag = 1
                break
        if flag:
            break

    if not flag:
        color[Map[x][y]] += 1


# calculate
color = [0, 0]
rec(0, 0, n)
print(color[0])
print(color[1])
