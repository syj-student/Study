from collections import defaultdict

def solution(clothes):
    answer = 1
    closet = defaultdict(int)
    for c in clothes:
        closet[c[1]] += 1
    for v in closet.values():
        answer *= v+1
    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))