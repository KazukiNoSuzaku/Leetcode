# Author: Kaustav Ghosh
# Problem: Keep Multiplying Found Values by Two
# Approach: Store the array in a set; while the current value is present, double it. Return the first value not found

class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        present = set(nums)
        while original in present:
            original *= 2
        return original
