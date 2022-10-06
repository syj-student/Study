def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    def checker(start, end):
        tmp = [0] * (end-start)
        tmp[0] = sticker[start]
        tmp[1] = max(sticker[start+1], tmp[0])
        for i in range(2, end-start):
            tmp[i] = max(tmp[i-2]+sticker[start+i], tmp[i-1])
        return tmp[-1]
    
    return max(checker(0, len(sticker)-1), checker(1, len(sticker)))