from itertools import permutations

def solution(n, count):
    building = [i for i in range(1, n+1)] * 2
    building.sort()
    answer = set()

    def dfs(stack=list(), block=0, prev=set(), depth=0, acc=count):
        nonlocal answer
        if depth == 2*n:
            if acc == 0:
                answer.add(tuple(stack))
                # print(stack)
            return
        
        for i in range(2*n):
            if i in prev:
                continue
            if block < building[i]:
                dfs(stack+[building[i]], building[i], prev|{i}, depth+1, acc-1)
            else:
                dfs(stack+[building[i]], block, prev|{i}, depth+1, acc)

    dfs()
    print(*answer, sep="\n")
    return len(answer) % 1000000007
print(solution(3, 3))