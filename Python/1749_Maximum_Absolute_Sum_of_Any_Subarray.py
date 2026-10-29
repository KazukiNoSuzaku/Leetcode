# Author: Kaustav Ghosh
# Problem: Maximum Absolute Sum of Any Subarray
# Approach: A subarray's sum is the difference of two running totals, so the largest absolute sum is the widest spread those running totals ever reach, which is their maximum minus their minimum. Tracking both extremes in a single pass therefore answers it without running the maximum-subarray scan twice over negated values. The empty prefix counts as a running total of zero, which is what allows a subarray starting at the very beginning to be measured.

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        running = 0
        highest = 0
        lowest = 0
        for value in nums:
            running += value
            if running > highest:
                highest = running
            elif running < lowest:
                lowest = running
        return highest - lowest
