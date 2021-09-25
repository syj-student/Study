# https://leetcode.com/problems/trapping-rain-water/

#class Solution:
#	def trap(self, height: List[int]) -> int:
#		stack = list()
#		volume = 0
#		for i in range(len(height)):
#			while stack and height[i] > height[stack[-1]]:
#				top = stack.pop()
#				if not len(stack):
#					break
#				distance = i - stack[-1] - 1
#				waters = min(height[i], height[stack[-1]]) - height[top]
#				volume += distance * waters
#			stack.append(i)
#		return volume

class Solution:
	def trap(self, height):
		if not height:
			return 0
		volume = 0
		left, right = 0, len(height) - 1
		left_max, right_max = height[left], height[right]
		while left <= right:
			left_max = max(left_max, height[left])
			right_max = max(right_max, height[right])
			if left_max <= right_max:
				volume += left_max - height[left]
				left += 1
			else:
				volume += right_max - height[right]
				right -= 1
		return volume

a = Solution()
b = [0, 2, 0, 1, 0, 0]
print(a.trap(b))