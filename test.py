from collections import deque, defaultdict
import heapq

def solution(board):
    N = len(board)
    answer = float('inf')
    move = ((0, 1, 0), (1, 0, 1), (0, -1, 2), (-1, 0, 3))
    dq = [(0, 0, 0, 1), (0, 0, 0, 0)]
    dist = dict()
    while dq:
        cost, x, y, d = heapq.heappop(dq)
        if dist.get((x, y, d), float('inf')) <= cost:
            continue
        dist[(x, y, d)] = cost
        if x == N-1 and y == N-1:
            answer = min(answer, cost)
            continue
        for ax, ay, ad in move:
            nx = ax + x
            ny = ay + y
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                new_cost = cost
                if abs(ad-d) == 2 or ad == d:
                    new_cost += 100
                    heapq.heappush(dq, (new_cost, nx, ny, ad))
                else:
                    new_cost += 600
                    heapq.heappush(dq, (new_cost, nx, ny, ad))
    return answer

print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))