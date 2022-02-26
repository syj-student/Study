import sys
import itertools


def team_ability(team):
    ret = 0
    t = itertools.combinations(team, 2)
    for a, b in t:
        ret += table[a][b] + table[b][a]
    return ret


n = int(sys.stdin.readline())
table = list()
for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    table.append(l)

answer = float('inf')
teamA = set([x for x in range(n)])

for i in range(1, n):
    cases = itertools.combinations(teamA, i)
    for case in cases:
        teamB = case
        team = teamA - teamB
        answer = min(answer, abs(team_ability(team) - team_ability(teamB)))
        if answer == 0:
            break
    if answer == 0:
        break
print(answer)
