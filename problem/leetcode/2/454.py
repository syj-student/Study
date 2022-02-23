from typing import List
from collections import Counter, defaultdict


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        nums3 = Counter(nums3)
        nums4 = Counter(nums4)

        N1 = defaultdict(int)
        for num1, n1 in nums1.items():
            for num2, n2 in nums2.items():
                N1[num1 + num2] += n1 * n2

        N3 = defaultdict(int)
        for num3, n3 in nums3.items():
            for num4, n4 in nums4.items():
                N3[num3 + num4] += n3 * n4

        return sum(N1[n1] * N3[-n1] for n1 in N1 if -n1 in N3)
