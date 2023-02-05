def solution(stones, k):
    left, right = 1, 200000000
    while left <= right:
        mid = (right + left) // 2
        if can_pass(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1
    return left

def can_pass(stones, k, friends):
    fall = k
    for duration in stones:
        if duration > friends: fall = k
        else: fall -= 1   
     
        if fall == 0:
            return False
    
    return True


print(
    solution(	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
)