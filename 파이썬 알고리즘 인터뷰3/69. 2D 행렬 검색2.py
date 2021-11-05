# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		for i in range(len(matrix)):
			if matrix[i][-1] >= target:
				break
		for i in range(i, len(matrix)):
			if target in matrix[i]:
				return True
		return False