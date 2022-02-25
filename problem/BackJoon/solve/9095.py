from itertools import combinations

container = [1, 2, 3]


cases = 0


def dfs(target_number, acc=0):
    global cases
    if acc > target_number:
        return
    if acc == target_number:
        cases += 1
        return
    for i in range(3):
        dfs(target_number, acc + container[i])


n = int(input())
for _ in range(n):
    x = int(input())
    dfs(x)
    print(cases)
    cases = 0
