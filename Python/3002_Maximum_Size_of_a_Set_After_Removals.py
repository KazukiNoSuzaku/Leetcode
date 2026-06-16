from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        half = n // 2
        s1, s2 = set(nums1), set(nums2)
        common = s1 & s2
        only1 = len(s1) - len(common)
        only2 = len(s2) - len(common)

        take1 = min(only1, half)
        rem1 = half - take1
        take2 = min(only2, half)
        rem2 = half - take2

        take_common = min(len(common), rem1 + rem2)

        return take1 + take2 + take_common
