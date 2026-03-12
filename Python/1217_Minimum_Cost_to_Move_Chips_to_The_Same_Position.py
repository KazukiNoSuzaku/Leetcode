# Author: Kaustav Ghosh
# Count chips at odd vs even positions; min of the two is the answer

class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        odd = sum(1 for p in position if p % 2 == 1)
        even = len(position) - odd
        return min(odd, even)
