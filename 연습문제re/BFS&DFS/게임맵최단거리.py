import heapq

def solution(maps):
    m = [[float('inf')]*len(maps[0]) for _ in range(len(maps))]
    move = ((1, 0), (0, 1), (-1, 0), (0, -1))
    stack = [(1, 0, 0)]
    while stack:
        cost, x, y = heapq.heappop(stack)
        if cost > m[x][y]:
            continue
        m[x][y] = cost
        for a, b in move:
            nx = x + a
            ny = y + b
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                new_cost = cost + 1
                if new_cost < m[nx][ny]:
                    m[nx][ny] = new_cost
                    heapq.heappush(stack, (new_cost, nx, ny))
    if m[-1][-1] == float('inf'):
        return -1
    return m[-1][-1]

print(solution(
    [[1]]
))