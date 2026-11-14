# Author: Kaustav Ghosh
# Problem: Maximum Product Difference Between Two Pairs
# Approach: All the values are positive, so the difference is largest when the first product is as big as possible and the second as small as possible, and those are independently achieved by the two largest and the two smallest values; no pair can be shared because four distinct indices are required and the two extremes never overlap for an array of four or more. Sorting makes both pairs the ends of the array.

class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ordered = sorted(nums)
        return ordered[-1] * ordered[-2] - ordered[0] * ordered[1]
