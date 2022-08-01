import sys
sys.setrecursionlimit(10 ** 9)

def rec(start, now, road, road2):
    global vote, visited
    if now in road:
        return road2[road2.index(now):]
    if visited[now]:
        return list()
    visited[now] = True
    road.add(now)
    road2.append(now)
    return rec(start, vote[now], road, road2)

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    persons = int(input())
    vote = list(map(lambda x: int(x)-1, input().split()))
    visited = [False] * persons
    have_group = list()
    for start in range(persons):
        if not visited[start]:
            have_group.append(rec(start, start, set(), list()))
    print(persons - len(have_group))

