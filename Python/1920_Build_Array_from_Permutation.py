# Author: Kaustav Ghosh
# Problem: Build Array from Permutation
# Approach: Each output position is defined by following the permutation twice from that position, and because the result is built into a new list the original array is never disturbed mid-pass, so a direct comprehension reads every lookup from the untouched input.

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[nums[index]] for index in range(len(nums))]
