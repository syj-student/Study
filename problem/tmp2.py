def checker(reg, words):
    answer = 0
    direction, reg = reg
    for word in words:
        if len(reg) != len(word):
            continue
        same = False
        if direction == 'f':
            i = len(reg)
            while i >= 0:
                i -= 1
                if reg[i] == word[i]:
                    continue

                if reg[i] == '?':
                    same = True
                    break
                break
            if same:
                answer += 1
        else:
            for a, b in zip(reg, word):
                if a == b:
                    continue
                if a == '?':
                    same = True
                    break
                break

            if same:
                answer += 1
    return answer

def solution(words, queries):
    answer = []

    new_queries = list()
    for q in queries:
        if q[0] == '?':
            new_queries.append(('f', q))
        else:
            new_queries.append(('b', q))

    for reg in new_queries:
        answer.append(checker(reg, words))

    return answer

print(solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"]
))