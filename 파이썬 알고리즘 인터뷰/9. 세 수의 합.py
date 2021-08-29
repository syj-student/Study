import itertools
nums = [-1,0,1,2,-1,-4]

nums.sort()
ret = list()
for i in range(len(nums)):
	left = i + 1
	right = len(nums) - 1
	while left < right:
		tmp = nums[i] + nums[left] + nums[right]
		if tmp == 0:
			ret.append([nums[i], nums[left], nums[right]])
			break
		elif tmp < 0:
			left += 1
		else:
			right -= 1
print(ret)

#class Solution:
#	def threeSum(self, nums: List[int]) -> List[List[int]]:
#		tmp = set(nums.sort())
#		ret = list()
#		for lst in itertools.combinations(tmp, 3):
#			if sum(lst) == 0:
#				ret.append(lst)
#		ret = list(set(map(lambda x: tuple(sorted(x)), ret)))
#		return ret