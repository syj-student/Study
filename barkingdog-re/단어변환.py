

def solution(begin, target, words):
    def diff_check(a, b):
        diff = 0
        for x, y in zip(a, b):
            if x != y:
                diff += 1
                if diff > 1:
                    return False
        return True
    
    stack = [(begin, 0)]
    visited = set()
    while stack:
        now, cnt = stack.pop()
        if now == target:
            return cnt
        if now in visited:
            continue
        tmp = list()
        while words:
            nxt = words.pop()
            if diff_check(nxt, now):
                stack.append((nxt, cnt+1))
            else:
                tmp.append(nxt)
        words = tmp


    answer = 0
    return answer