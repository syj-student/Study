#include <stdio.h>

int main(void)
{
	int nums[5] = {5, 4, 1, 3, 2};
    int numsSize = 5;
	int tmp;
	for (int j = 0; j < numsSize; j++)
	{
		for (int i = j + 1; i < numsSize; i++)
		{
			if (nums[j] > nums[i])
			{
				tmp = nums[i];
				nums[i] = nums[j];
				nums[j] = tmp;
			}
		}
	}
	for (int i = 0; i < 5; i++)
		printf("%d\n", nums[i]);
}
