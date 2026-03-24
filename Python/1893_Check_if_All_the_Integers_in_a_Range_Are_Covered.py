# Author: Kaustav Ghosh
# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        for i in range(left, right + 1):
            covered = False
            for l, r in ranges:
                if l <= i <= r:
                    covered = True
                    break
            if not covered:
                return False
        return True
