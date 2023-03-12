from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_index = defaultdict(list)
        for i in range(len(nums)):
            nums_index[nums[i]].append(i)
        for a in nums:
            b = target - a
            if a == b and (loc := nums_index.get(a)) and len(loc) >= 2:
                return (loc[0], loc[1])
            elif a != b and (loc := nums_index.get(b)):
                return (nums_index[a][0], loc[0])

    def test(self):
        print(self.twoSum([3,2,4], 6))
        
s = Solution()
s.test()