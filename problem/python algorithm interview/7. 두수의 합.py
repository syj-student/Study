# https://leetcode.com/problems/two-sum/

###
# C
###

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
	*returnSize = 2;
	int *returnArr= (int*) malloc((*returnSize)*sizeof(int));
	for(int i=0; i<(numsSize-1); i++){
		for(int j=i+1; j<numsSize; j++){
			if((nums[i]+nums[j]) == target){
				returnArr[0] = i;
				returnArr[1] = j;
				return returnArr;
			}
		}
	}
	returnArr[0] = -1;
	returnArr[1] = -1;
	return returnArr;
}

###
# python
###

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		nums_map = {}
		for i, num in enumerate(nums):
			nums_map[num] = i
		for i, num in enumerate(nums):
			if target - num in nums_map and nums_map[target - num] != i:
				return [i, nums_map[target - num]]
