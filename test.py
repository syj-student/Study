from collections import deque

M,N = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
visited_graph = [[0 for _ in range(M)] for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

queue = deque([])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i,j])

while queue:
    y,x = queue.popleft()
    for i in range(4):
        nX = x + dx[i]
        nY = y + dy[i]

        if 0 <= nX < M and 0 <= nY < N:
            if graph[nY][nX] == 0:
                queue.append([nY,nX])
                graph[nY][nX] = graph[y][x] + 1


total = graph[0][0]
endFlag = False
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            total = max(graph[i][j], total)
        else:
            print(-1)
            endFlag = True
            break
        
    if endFlag:
        break

if not endFlag:
    print(total-1)