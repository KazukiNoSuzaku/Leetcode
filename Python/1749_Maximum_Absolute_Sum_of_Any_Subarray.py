# Author: Kaustav Ghosh
# Problem: Maximum Absolute Sum of Any Subarray
# Approach: The largest absolute sum is either the most positive or the most negative subarray, so run Kadane in both directions at once (empty subarray gives 0)

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = 0
        run_max = 0
        run_min = 0
        for x in nums:
            run_max = max(0, run_max + x)
            run_min = min(0, run_min + x)
            best = max(best, run_max, -run_min)
        return best
