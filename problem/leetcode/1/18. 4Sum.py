class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		if len(nums) < 4:
			return list()
		nums.sort()
		answer = list()
		for i in range(len(nums)-3):
			for j in range(i+1, len(nums)-2):
				left, right = j + 1, len(nums) - 1
				while left < right:
					if nums[i] + nums[j] + nums[left] + nums[right] == target:
						answer.append((nums[i], nums[j], nums[left], nums[right]))
						left += 1
						right -= 1
					elif nums[i] + nums[j] + nums[left] + nums[right] > target:
						right -= 1
					else:
						left += 1
		return set(answer)


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res, n = set(), len(nums)

#         nums.sort()
#         numDict = {num: i for i, num in enumerate(nums)}

#         i = bisect_left(nums, target - sum(nums[-3:]), 0, n)  # lowest bound for target
#         r1 = bisect_right(nums, target / 4, i, n)  # upper bound for target
#         while i < r1:
#             target2 = target - nums[i]
#             j = bisect_left(nums, target2 - sum(nums[-2:]), i + 1, n)
#             r2 = bisect_right(nums, target2 / 3, j, n)
#             while j < r2:
#                 end3 = bisect_right(nums, target2 - nums[j] * 2, j + 1, n)
#                 target3 = target2 - nums[j]
#                 k = bisect_left(nums, target3 - nums[end3-1], j + 1, end3)
#                 r3 = bisect_right(nums, target3 / 2, k, n)
#                 while k < r3:
#                     target4 = target3 - nums[k]
#                     if (target4 in numDict) and (numDict[target4] > k):
#                         res.add((nums[i], nums[j], nums[k], target4))
#                     k = numDict[nums[k]] + 1
#                 j = numDict[nums[j]] + 1
#             i = numDict[nums[i]] + 1

#         return res

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
#         def twoSum(nums, target):
#             table = set()
#             unique = set() 
#             ans = []
            
#             for num in nums:
#                 if target-num in table:
#                     if (num, target-num) not in unique:
#                         ans.append([num, target-num])
#                         unique.add((num, target-num))    
                        
#                 table.add(num)
#             return ans
        
        
#         def kSum(nums, target, k):
#             ans = []
            
#             if not nums:
#                 return ans
            
#             ave = target // k
#             if nums[0] > ave or nums[-1] < ave:
#                 return ans
            
#             if k == 2:
#                 return twoSum(nums, target)
            
#             for i in range(len(nums)):
#                 if i == 0 or nums[i] != nums[i-1]:
#                     for subset in kSum(nums[i+1:], target - nums[i], k-1):
#                         ans.append([nums[i]]+subset)  
                        
#             return ans
        
#         nums.sort()
        
#         return kSum(nums, target, 4)