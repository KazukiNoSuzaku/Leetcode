# Author: Kaustav Ghosh
# Problem: Maximum Ascending Subarray Sum
# Approach: Sweep once, extending the current strictly-ascending run's sum or restarting it, tracking the best

class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = current = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += nums[i]
            else:
                current = nums[i]
            best = max(best, current)
        return best
