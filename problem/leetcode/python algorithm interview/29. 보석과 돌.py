# https://leetcode.com/problems/jewels-and-stones/

class Solution:
	def numJewelsInStones(self, jewels: str, stones: str) -> int:
		cntMap = collections.Counter(stones);
		answer = 0;
		for jewel in jewels:
			answer += cntMap[jewel]
		return answer