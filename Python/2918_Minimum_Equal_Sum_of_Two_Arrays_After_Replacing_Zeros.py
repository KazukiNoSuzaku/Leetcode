from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1) + nums1.count(0)
        s2 = sum(nums2) + nums2.count(0)
        if not nums1.count(0) and s1 < s2:
            return -1
        if not nums2.count(0) and s2 < s1:
            return -1
        return max(s1, s2)
