import sys
import collections
import pprint

stock = collections.deque()
MAX_NUMBER = 0
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    stock.append(n)
    MAX_NUMBER = max(MAX_NUMBER, n)

board = [i for i in range(MAX_NUMBER)]

for i in range(2, MAX_NUMBER):
    if board[i]:
        step = i
        i += step
        while i < MAX_NUMBER:
            board[i] = False
            i += step
while stock:
    n = stock.popleft()
    for i in range(2, MAX_NUMBER):
        a = board[i]
        if a and board[n - a]:
            print(f'{n} = {a} + {board[n - a]}')
            break
