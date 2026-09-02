# Author: Kaustav Ghosh
# Problem: Find the Difference of Two Arrays
# Approach: Use set difference in both directions to find distinct values present in one array but not the other

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
