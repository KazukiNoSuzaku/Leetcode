# Author: Kaustav Ghosh
# Problem: Make Two Arrays Equal by Reversing Sub-arrays
# Approach: Check if both arrays have the same multiset (sort both)

class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        return sorted(target) == sorted(arr)
