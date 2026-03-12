# Author: Kaustav Ghosh
# 1060. Missing Element in Sorted Array
# https://leetcode.com/problems/missing-element-in-sorted-array/

class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def missing(idx):
            return nums[idx] - nums[0] - idx

        n = len(nums)
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        lo, hi = 0, n - 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if missing(mid) < k:
                lo = mid
            else:
                hi = mid
        return nums[lo] + k - missing(lo)
