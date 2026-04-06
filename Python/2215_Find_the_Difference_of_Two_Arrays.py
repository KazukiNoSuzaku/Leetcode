# Author: Kaustav Ghosh
# Problem: 2215. Find the Difference of Two Arrays
# URL: https://leetcode.com/problems/find-the-difference-of-two-arrays/
# Difficulty: Easy
#
# Approach:
# Convert both lists to sets, then compute the set difference in both
# directions. Return each result as a list.

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: list[int]
        :type nums2: list[int]
        :rtype: list[list[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
