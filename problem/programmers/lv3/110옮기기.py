from collections import deque

# good
def solution2(s):
    def extract110(frag):
        stack = deque()
        cnt = 0
        for c in frag:
            if c == "0" and len(stack) >= 2 and  stack[-2] == stack[-1] == "1":
                stack.pop()
                stack.pop()
                cnt += 1
                continue
            stack.append(c)
        return "".join(stack), cnt

    def insert110(l):
        frag, cnt = extract110(l)
        acc = "110" * cnt
        idx = frag.rfind("0")
        if idx == -1:
            return acc + frag
        return frag[:idx+1] + acc + frag[idx+1:]

    answer = []
    for l in s:
        answer.append(insert110(l))
    return answer

# time out
def solution1(s):
    def extract110(frag):
        cnt = len(frag)
        while (idx := frag.find("110")) != -1:
            frag = frag.replace("110", "")
        cnt -= len(frag)
        return frag, cnt // 3

    def insert110(l):
        frag, cnt = extract110(l)
        acc = "110" * cnt
        idx = frag.rfind("0")
        if idx == -1:
            return acc + frag
        return frag[:idx+1] + acc + frag[idx+1:]

    answer = []
    for l in s:
        answer.append(insert110(l))
    return answer

# time out
def solution(s):
    def extract110(frag):
        cnt = 0
        while (frag_len := len((new_frag := frag.split("110")))) != 1:
            cnt += frag_len - 1
            frag = "".join(new_frag)
        return frag, cnt

    def insert110(l):
        frag, cnt = extract110(l)
        acc = "110" * cnt
        idx = frag.rfind("0")
        if idx == -1:
            return acc + frag
        return frag[:idx+1] + acc + frag[idx+1:]

    answer = []
    for l in s:
        answer.append(insert110(l))
    return answer


print(solution(["1110","100111100","0111111010"]))