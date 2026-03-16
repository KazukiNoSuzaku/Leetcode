# Author: Kaustav Ghosh
# Problem: Sort Integers by The Number of 1 Bits
# Approach: Sort by (popcount, value)

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
