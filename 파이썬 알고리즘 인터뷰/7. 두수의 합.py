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