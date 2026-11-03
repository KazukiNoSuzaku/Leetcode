# Author: Kaustav Ghosh
# Problem: Maximum Ascending Subarray Sum
# Approach: An ascending run can only be broken where a value fails to exceed the one before it, so a single pass keeps the sum of the run currently in progress and restarts it at exactly those breaks. The best sum seen so far is updated at every step, which covers runs of length one as well.

class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = running = nums[0]
        for previous, value in zip(nums, nums[1:]):
            running = running + value if value > previous else value
            if running > best:
                best = running
        return best
