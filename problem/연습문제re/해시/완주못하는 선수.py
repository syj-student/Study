from collections import Counter

def solution(participant, completion):
    completion = Counter(completion)
    for p in participant:
        if p not in completion:
            return p
        completion[p] -= 1
        if completion[p] == 0:
            del completion[p]