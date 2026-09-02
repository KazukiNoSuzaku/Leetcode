# Author: Kaustav Ghosh
# Problem: Check if an Array Is Consecutive
# Approach: The array is consecutive exactly when it has no duplicates and its span (max - min) equals n - 1, which forces it to be every integer from min to max once

class Solution(object):
    def isConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        return len(set(nums)) == n and max(nums) - min(nums) == n - 1
