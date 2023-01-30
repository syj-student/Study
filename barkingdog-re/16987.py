from sys import stdin

input = stdin.readline
x = int(input())
eggs = list()
for _ in range(x):
    eggs.append(list(map(int, input().split())))
eggs_isbroken = set()
answer = 0

def egg_fight(now=0):
    global eggs, answer, eggs_isbroken

    i_isbroken = now_isbroken = False

    if now < len(eggs):
        if eggs[now][0] <= 0:
            egg_fight(now+1)
        else:
            for i in range(len(eggs)):
                if now == i or i in eggs_isbroken:
                    continue
                eggs[i][0] -= eggs[now][1]
                eggs[now][0] -= eggs[i][1]
                prev = eggs_isbroken.copy() 
                if eggs[i][0] <= 0: eggs_isbroken.add(i)
                if eggs[now][0] <= 0: eggs_isbroken.add(now)
                egg_fight(now+1)
                eggs_isbroken = prev
                eggs[i][0] += eggs[now][1]
                eggs[now][0] += eggs[i][1]

    answer = max(answer, len(eggs_isbroken))

egg_fight()
print(answer)