# Author: Kaustav Ghosh
# Problem: Check if All the Integers in a Range Are Covered
# Approach: The bounds are tiny, so just check each integer in [left, right] is inside some range

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        return all(any(a <= x <= b for a, b in ranges) for x in range(left, right + 1))
