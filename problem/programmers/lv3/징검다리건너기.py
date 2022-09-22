

# def solution(stones, k):
#     def checker():
#         start, end = 0, k
#         while end <= len(stones):
#             for i in range(start, end):
#                 if stones[i] > 0:
#                     start = i
#                     end = i + k
#                     break
#             else:
#                 return False
#         return True

#     def minus(n):
#         for i in range(len(stones)):
#             stones[i] -= n

#     prev = 0
#     target = sorted(set(stones))
#     answer = 0
#     for t in target:
#         m = t - prev
#         prev = t
#         minus(m)
#         if not checker():
#             return t


#     return answer

# from collections import deque
# import bisect

# def solution(stones, k):
#     window = deque()
#     lst = deque()
#     answer = float('-inf')
#     for i in range(k):
#         idx = bisect.bisect_right(lst, stones[i])
#         lst.insert(idx, stones[i])
#         window.append(stones[i])
#         answer = max(answer, stones[i])

#     for i in range(k, len(stones)):
#         left = window.popleft()
#         idx = bisect.bisect_left(lst, left)
#         del lst[idx]

#         right = stones[i]
#         window.append(right)
#         idx = bisect.bisect_left(lst, right)
#         lst.insert(idx, right)

#         answer = min(answer, lst[-1])

        
#     return answer

def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
        
    return left