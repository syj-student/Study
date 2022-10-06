def solution(s):
    big, small = float('-inf'), float('inf')
    for i in map(int, s.split()):
        big = max(big, i)
        small = min(small, i)
    
    return "{0} {1}".format(small, big)