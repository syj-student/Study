from collections import deque, Counter, defaultdict
from itertools import combinations
import re


def solution(user_id, banned_id):
    answer = 0
    banned_id = Counter(banned_id)
    d = defaultdict(set)
    for b in banned_id:
        p = re.compile(b.replace('*', '.')+'$')
        for u in user_id:
            if p.match(u):
                d[b].add(u)

    bm = banned_id.most_common()
    bm.reverse()
    def combination_maker(now=set(), depth=0):
        nonlocal bm, d, answer
        if depth == len(bm):
            answer += 1
            return

        b, n = bm[depth]
        t = combinations(d[b], n)
        for case in t:
            case = set(case)
            if case & now:
                continue
            combination_maker(now | case, depth+1)

    combination_maker()


    return answer

print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"]
    )
)