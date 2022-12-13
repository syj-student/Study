import sys
sys.setrecursionlimit(2*10**9)

def solution(beginning, target):
    answer = float('inf')
    change = lambda x: 0 if x else 1
    def dfs(start=0, depth=0):
        nonlocal beginning, target, answer, change
        if depth >= answer:
            return
        if beginning == target:
            answer = min(answer, depth)
            return
        for i in range(start, len(beginning)+start):
            for j in range(len(beginning[0])):
                beginning[i%len(beginning)][j] = change(beginning[i%len(beginning)][j])
            dfs(start+1, depth+1)
            for j in range(len(beginning[0])):
                beginning[i%len(beginning)][j] = change(beginning[i%len(beginning)][j])
        print("good")
        for i in range(start, len(beginning[0])+start):
            for j in range(len(beginning)):
                beginning[j][i%len(beginning[0])] = change(beginning[j][i%len(beginning[0])])
            dfs(start+1, depth+1)
            for j in range(len(beginning)):
                beginning[j][i%len(beginning[0])] = change(beginning[j][i%len(beginning[0])])
    dfs()
    print("good")
    return -1 if answer == float('inf') else answer

print(solution(
    [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], 
    [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
))