# Author: Kaustav Ghosh
# Problem: 2154. Keep Multiplying Found Values by Two
# URL: https://leetcode.com/problems/keep-multiplying-found-values-by-two/
# Approach: Convert array to set, then repeatedly double original if found

class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        num_set = set(nums)
        while original in num_set:
            original *= 2
        return original
