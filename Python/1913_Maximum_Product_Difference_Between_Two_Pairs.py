# Author: Kaustav Ghosh
# Problem: Maximum Product Difference Between Two Pairs
# Approach: All values are positive, so the largest product comes from the two biggest numbers and the smallest from the two smallest. The answer is their difference

class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
