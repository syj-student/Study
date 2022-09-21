from collections import defaultdict

def solution(gems):
    counter = defaultdict(int)
    gem_list = set(gems)
    answer = [0, 0]
    real_answer = [float('inf'), list()]
    def checker():
        if len(gem_list) > len(counter):
            return False
        return True

    for i, g in enumerate(gems):
        counter[g] += 1
        if checker():
            answer[1] = i
            while True:
                if counter[gems[answer[0]]] > 1:
                    counter[gems[answer[0]]] -= 1
                    answer[0] += 1
                else:
                    break
                
            if (dis := answer[1] - answer[0]) < real_answer[0]:
                real_answer[0] = dis
                real_answer[1] = [answer[0]+1, answer[1]+1]
    return real_answer[1]



print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
