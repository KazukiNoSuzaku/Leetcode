# Author: Kaustav Ghosh
# Problem: Minimum Absolute Sum Difference
# Approach: Only one position may be replaced, so the total is the untouched sum of absolute differences minus the best single saving available anywhere. For a given position the saving is largest when the substituted value sits as close as possible to nums2 at that position, and the nearest candidate is found by binary search in a sorted copy of nums1, checking the two values that straddle the target. The whole scan therefore costs one sort plus a logarithmic lookup per position, and the modulus is applied only at the end so the saving is never compared against a wrapped value.

class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        from bisect import bisect_left

        MOD = 10 ** 9 + 7
        ordered = sorted(nums1)
        total = 0
        saving = 0
        for first, second in zip(nums1, nums2):
            gap = abs(first - second)
            total += gap
            position = bisect_left(ordered, second)
            if position < len(ordered):
                saving = max(saving, gap - (ordered[position] - second))
            if position:
                saving = max(saving, gap - (second - ordered[position - 1]))
        return (total - saving) % MOD
