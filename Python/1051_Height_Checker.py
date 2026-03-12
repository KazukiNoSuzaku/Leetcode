# Author: Kaustav Ghosh
# 1051. Height Checker
# https://leetcode.com/problems/height-checker/

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        return sum(1 for a, b in zip(heights, expected) if a != b)
