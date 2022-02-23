import collections


class Solution:
    answer = 0

    def longestSubstring(self, s: str, k: int) -> int:
        counter = collections.Counter(s).most_common()
        least = counter[-1]
        s.split(least[0])
        return answer


print(Solution().longestSubstring("aaabb", 3))
