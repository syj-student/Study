def sol(start, depth):
    if depth == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(start, len(nums)):
        if depth == 0 or arr[-1] <= nums[i]:
            arr.append(nums[i])
            sol(i, depth+1)
            arr.pop()
n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
arr = list()
sol(0, 0)