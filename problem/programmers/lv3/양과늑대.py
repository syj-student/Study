def solution(info, edges):
    visited = [0] *len(info)
    visited[0] = 1
    answer = 0
    def dfs(sheep, wolf):
        nonlocal answer
        if sheep > wolf:
            answer = max(answer, sheep)
        else:
            return 
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            isWolf = True if info[child] == 1 else False
            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep+(0 if isWolf else 1), wolf+(1 if isWolf else 0))
                visited[child] = 0
    dfs(1, 0)
    return answer