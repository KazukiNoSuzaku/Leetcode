# Author: Kaustav Ghosh
# Problem: Maximum Value of a String in an Array
# Approach: A string of digits is worth its numeric value and anything else is worth its length, so map each string accordingly and take the largest

class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        return max(int(s) if s.isdigit() else len(s) for s in strs)
