from sys import stdin

input = stdin.readline

town, capa = map(int, input().split())
post_info = list()
for _ in range(int(input())):
    f, t, p = map(int, input().split())
    post_info.append([f, t, p])
post_info.sort(key=lambda x: x[1])

town_post = [0] * (town+1)
answer = 0
for f, t, p in post_info:
    max_post_weight = 0
    for loc in range(f, t):
        max_post_weight = max(town_post[loc], max_post_weight)
    more = min(capa - max_post_weight, p)
    answer += more
    for loc in range(f, t):
        town_post[loc] += more
print(answer)
