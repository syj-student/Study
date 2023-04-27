import heapq
def solution(board):
    answer = float('inf')
    heap = [(0, 0, 0, 3), (0, 0, 0, 4)]
    m, n = len(board), len(board[0])
    visited = set()
    move = ((0, 1, 3), (0, -1, 1), (1, 0, 4), (-1, 0, 2))
    # 0 2 0
    # 1 0 3
    # 0 4 0
    while heap:
        now_cost, x, y, d = heapq.heappop(heap)

        if (x, y, d) in visited:
            continue
        visited.add((x, y, d))
        
        if x == (m-1) and y == (n-1):
            answer = min(answer, now_cost)
            continue

        for (dx, dy, nd) in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < m and 0 <= ny < n and not (nx, ny, nd) in visited and not board[nx][ny] == 1:
                if nd == d:
                    heapq.heappush(heap, (now_cost+100, nx, ny, nd))
                else:
                    heapq.heappush(heap, (now_cost+600, nx, ny, nd))
    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))