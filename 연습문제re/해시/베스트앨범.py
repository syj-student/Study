from collections import defaultdict

def solution(genres, plays):
    answer = []
    m = defaultdict(list)
    pt = defaultdict(int)
    for i in range(len(genres)):
        pt[genres[i]] += plays[i]
        m[genres[i]].append((plays[i], i))
    sortedpt = list()
    for k, v in pt.items():
        sortedpt.append((v, k))
    sortedpt.sort(reverse=True)
    for _, g in sortedpt:
        m[g].sort(reverse=True,  key=lambda x: (x[0], -x[1]))
        for i in range(min(2, len(m[g]))):
            answer.append(m[g][i][1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop", "good"], [150, 600, 150, 800, 2500, 1]))