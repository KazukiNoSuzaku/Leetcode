# Author: Kaustav Ghosh
# Problem: Running Sum of 1d Array
# Approach: Prefix sum in-place

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
