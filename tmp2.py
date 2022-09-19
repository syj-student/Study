from itertools import combinations, permutations
import re

def solution(user_id, banned_id):
    answer = set()
    p = list(map(lambda x: re.compile(x.replace('*', '.')+'$'), banned_id))
    for case in permutations(user_id, len(banned_id)):
        for m, u in zip(p, case):
            if not m.match(u):
                break
        else:
            answer.add(tuple(sorted(case)))


    return len(answer)

print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"]
    )
)