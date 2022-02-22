import bisect


def nextPermutation(nums) -> None:
    k = sorted(nums)
    print(k, list(reversed(k)), nums)
    if nums == list(reversed(k)):
        for i in range(len(nums)):
            nums[i] = k[i]
        return
    for i in range(len(nums)):
        tmp = nums[i+1:]
        if tmp == sorted(tmp, reverse=True):
            answer = sorted(answer)
            idx = bisect.bisect_right(answer, nums[i])
            if idx >= len(nums):
                k = reversed(nums)
                for i in range(len(nums)):
                    nums[i] = k[i]
                return
            a = nums[:i]
            a.append(answer.pop(idx))
            a = a + answer
            for i in range(len(nums)):
                nums[i] = a[i]
            return


a = [1, 3, 2]
nextPermutation(a)
print(a)
