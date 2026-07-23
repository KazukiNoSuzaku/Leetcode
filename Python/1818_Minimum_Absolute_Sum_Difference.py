# Author: Kaustav Ghosh
# Problem: Minimum Absolute Sum Difference
# Approach: Compute the base sum, then for each index binary-search a sorted copy of nums1 for the value closest to nums2[i]; track the largest reduction a single swap can give

from bisect import bisect_left

class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums1)
        total = sum(abs(a - b) for a, b in zip(nums1, nums2))
        ordered = sorted(nums1)

        best_gain = 0
        for i in range(n):
            original = abs(nums1[i] - nums2[i])
            pos = bisect_left(ordered, nums2[i])
            for p in (pos, pos - 1):
                if 0 <= p < n:
                    best_gain = max(best_gain, original - abs(ordered[p] - nums2[i]))

        return (total - best_gain) % MOD
