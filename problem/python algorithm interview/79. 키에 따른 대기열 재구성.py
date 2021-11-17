# https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution:
	def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
		people.sort(key= lambda x, y:(x[0], -x[1]), reverse=True)
		result =list()
		for i in people:
			result.insert(i[1], i)
		return result