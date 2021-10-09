# https://leetcode.com/problems/course-schedule/
import collections
class Solution:
	def canFinish(self, numCourses, prerequisites) -> bool:
		courseMap = collections.defaultdict(list)
		for a, b in prerequisites:
			courseMap[a].append(b)
		flag = [True]
		def dfs(a, visited=list()):
			if a in visited:
				flag[0] = False
				return 
			visited.append(a)
			for i in courseMap[a]:
				dfs(i, visited)

		for i in list(courseMap.keys()):
			dfs(i)
			if flag[0] == False:
				break
		return flag[0]

a = Solution()
print(a.canFinish(2, [[1, 0], [0,1]]))