import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0
        if k == 0:
            return len(s)
        idx = 0
        while idx < len(s) and s.count(s[idx]) >= k:
            idx += 1
        if idx == len(s):
            return len(s)
        left = self.longestSubstring(s[:idx], k)
        right = self.longestSubstring(s[idx+1:], k)
        return max(left, right)


print(Solution().longestSubstring("aaabb", 3))
