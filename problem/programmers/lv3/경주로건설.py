import heapq

def solution(board):
    N = len(board)
    answer = float('inf')

    def total_cost(lst):
        corner = 0
        for i in range(2, len(lst)):
            if abs(lst[i-2][0]-lst[i][0]) == abs(lst[i-2][1]-lst[i][1]):
                corner += 1
        return corner*500 + (len(lst)-1)*100

    def dfs():
        dist = [[float('inf')]*N for _ in range(N)]
        move = ((1, 0), (0, 1), (-1, 0), (0, -1))
        heap = [[0, 0, 0, [(0, 0)]]]
        while heap:
            cost, x, y, ways = heapq.heappop(heap)
            if cost > dist[x][y]:
                continue
            dist[x][y] = cost
            for dx, dy in move:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and (nx, ny) not in ways:
                    new_ways = ways + [(nx, ny)]
                    new_total_cost = total_cost(new_ways)
                    if new_total_cost <= dist[nx][ny]:
                        heapq.heappush(heap, [new_total_cost, nx, ny, new_ways])
        return dist[-1][-1]
    return dfs()

print(solution(	[[0, 0], [0, 0]]))