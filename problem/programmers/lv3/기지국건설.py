import math

def solution(n, stations, w):
    answer = 0
    stations.sort()
    rg = list()
    for i in stations:
        i -= 1
        start = i-w if i-w >= 0 else 0
        end = i+w if i+w < n else n
        if rg and rg[-1][1] >= start:
            rg[-1][1] = end
        else:
            rg.append([start, end])
    dis = list()
    prev = 0
    for s, e in rg:
        dis.append(s - prev)
        prev = e+1
    if prev < n:
        dis.append(n - prev)
    for d in dis:
        answer += math.ceil(d / (w*2+1))
    return answer

print(solution(
    16, [], 2
))