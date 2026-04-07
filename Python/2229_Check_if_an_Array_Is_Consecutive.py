# Author: Kaustav Ghosh
# Problem: 2229. Check if an Array Is Consecutive
# URL: https://leetcode.com/problems/check-if-an-array-is-consecutive/
# Difficulty: Easy
# Note: Premium problem
#
# Approach:
# An array is consecutive if all elements are unique and the range spans
# exactly n values: max(nums) - min(nums) == n - 1 and len(set(nums)) == n.

class Solution(object):
    def isConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return max(nums) - min(nums) == len(nums) - 1 and len(set(nums)) == len(nums)
