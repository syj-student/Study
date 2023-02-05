from collections import defaultdict
import heapq

def solution(genres, plays):
    play_count = defaultdict(int)
    separate_by_genres = defaultdict(list)
    for i in range(len(genres)):
        play_count[genres[i]] += plays[i]
        heapq.heappush(separate_by_genres[genres[i]], (-plays[i], i))
    answer = []
    for genre in sorted(play_count, reverse=True, key= lambda x: play_count[x]):
        cnt = 2
        while separate_by_genres[genre] and cnt > 0:
            answer.append(heapq.heappop(separate_by_genres[genre])[1]); cnt -= 1
    return answer