import sys


def cal_income(day, acc=0):
    finish_day = day + table[day][0]
    ret = 0
    if finish_day - 1 in table:
        acc += table[day][1]
    if finish_day in table:
        for i in range(finish_day, n+1):
            ret = max(ret, cal_income(i, acc))
        acc = ret
    return acc


n = int(sys.stdin.readline())
table = dict()
answer = 0
for i in range(1, n+1):
    d, v = map(int, sys.stdin.readline().split())
    table[i] = (d, v)
for start in range(1, n+1):
    answer = max(answer, cal_income(start))
print(answer)
