# Author: Kaustav Ghosh
# Problem: 1529 - Minimum Suffix Flips
# Approach: Count changes in target string from '0'

class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        result = 0
        current = '0'
        for c in target:
            if c != current:
                result += 1
                current = c
        return result
