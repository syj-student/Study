# https://leetcode.com/problems/combination-sum/

class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		result = list()
		
		def dfs(csum, index, path):
			if csum < 0:
				return
			if csum == 0:
				return result.append(path)
			for i in range(index, len(candidates)):
				dfs(csum - candidates[i], i, path + [candidates[i]])
		dfs(target, 0, [])
		return result

