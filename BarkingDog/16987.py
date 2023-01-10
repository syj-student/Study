import sys

input = sys.stdin.readline


answer = 0
lst = list()
# [내구도, 무게]
for _ in range(int(input())):
    t = list(map(int, input().split()))
    t.append(True)
    lst.append(t)

def dfs(now=0):
    global answer, lst
    if now == len(lst):
        now_answer = 0
        for bk in lst:
            if bk[2] == False:
                now_answer += 1
        answer = max(answer, now_answer) 
        return
    if lst[now][2] == False:
        dfs(now+1)
    else:
        for op in range(len(lst)):
            if op == now or lst[op][2] == False:
                now_answer = 0
                for bk in lst:
                    if bk[2] == False:
                        now_answer += 1
                answer = max(answer, now_answer) 
                continue
            lst[now][0] -= lst[op][1]
            if lst[now][0] <= 0:
                lst[now][2] = False
            lst[op][0] -= lst[now][1]
            if lst[op][0] <= 0:
                lst[op][2] = False
            dfs(now+1)
            lst[now][0] += lst[op][1]
            lst[now][2] = True
            lst[op][0] += lst[now][1]
            lst[op][2] = True


dfs()
print(answer)