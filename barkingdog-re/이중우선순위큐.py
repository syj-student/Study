from collections import deque

def solution(operations):
    big, small = deque(), deque()
    for cmd in operations:
        c, n = cmd.split()
        
        if c == 'I':
            n = int(n)
            while big and big[0] < n:
                small.appendleft(big.popleft())
            while small and small[0] > n:
                big.appendleft(small.popleft())
            small.appendleft(n)
        else:
            if n == "-1":
                if small: small.pop()
                elif big: big.popleft()
                else: continue
            else:
                if big: big.pop()
                elif small: small.popleft()
                else: continue
    if big and small:
        return [big[-1], small[-1]]
    if big:
        return [big[-1], big[0]]
    if small:
        return [small[0], small[-1]]
    return [0, 0]

print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))