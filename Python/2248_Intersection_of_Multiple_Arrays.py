# Author: Kaustav Ghosh
# Problem: 2248. Intersection of Multiple Arrays
# URL: https://leetcode.com/problems/intersection-of-multiple-arrays/
# Difficulty: Easy
#
# Approach:
# Convert each array to a set and intersect all of them. Return the
# sorted result.

class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result = set(nums[0])
        for i in range(1, len(nums)):
            result &= set(nums[i])
        return sorted(result)
