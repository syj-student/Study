def solution(n, computers):
    connect = [False] * n
    def dfs(start):
        nonlocal connect, computers

        stack = [start]
        while stack:
            now = stack.pop()
            connect[now] = True
            for nxt in range(n):
                if connect[nxt] or not computers[now][nxt]:
                    continue
                stack.append(nxt)

    answer = 0
    for i in range(n):
        if not connect[i]:
            dfs(i)
            answer += 1
    return answer
                
        
