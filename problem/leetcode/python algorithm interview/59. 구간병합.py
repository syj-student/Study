# https://leetcode.com/problems/merge-intervals/

class Solution:
	def merge(self, intervals):
		merged = list()
		for i in sorted(intervals, key=lambda x: x[0]):
			if merged and merged[-1][1] >= i[0]:
				merged[-1][1] = max(merged[-1][1], i[1])
			else:
				merged += i,
		return merged
a = Solution()

print(a.merge([[1,3],[2,6],[8,10],[15,18]]))