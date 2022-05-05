import sys

i, j = map(int, input().split())
board = list()
for _ in range(i):
    board.append(list(input()))


def checker(n):
    n = int(n)
    r = int(n**0.5)
    if r * r == n:
        return True
    return False


answer = -1
for x in range(i):
    for y in range(j):
        for dx in range(-i, i):
            for dy in range(-j, j):
                if dx == 0 and dy == 0:
                    continue
                no = ""
                tx = x
                ty = y
                while 0 <= tx < i and 0 <= ty < j:
                    no += board[tx][ty]
                    if checker(no):
                        answer = max(answer, int(no))
                    tx += dx
                    ty += dy
print(answer)
