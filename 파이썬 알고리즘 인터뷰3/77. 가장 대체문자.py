# https://leetcode.com/problems/longest-repeating-character-replacement/#

import collections


class Solution:
	def characterReplacement(self, s, k):
		counts = collections.Counter()
		left = 0
		for right in range(1, len(s)+1):
			counts[s[right-1]] += 1
			max_char_n = counts.most_common(1)[0][1]
			if right - left - max_char_n > k:
					counts[s[left]] -= 1
					left += 1
		return right - left

a = Solution()
print(a.characterReplacement("AAAAAAACCdfgfdsgsggsgqetnfmfmmtreCACABBCCAA", 2))