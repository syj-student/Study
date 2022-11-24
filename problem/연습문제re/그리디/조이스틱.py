def solution(name):
    answer = 0
    for c in name:
        answer += min(abs(ord('Z')-ord(c)+1), ord(c)-ord('A'))
    min_move = len(name)-1
    for i in range(len(name)):
        step = i+1
        while step < len(name) and name[step] == 'A':
            step += 1
        min_move = min(min_move, i*2+len(name)-step, 2*(len(name)-step)+i)
    answer += min_move
    return answer

print(solution("ABABAABA"))