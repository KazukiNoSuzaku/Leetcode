# Author: Kaustav Ghosh
# Problem 2087: Minimum Cost Homecoming of a Robot in a Grid

class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        cost = 0
        sr, sc = startPos
        hr, hc = homePos
        # Move rows
        if sr < hr:
            for r in range(sr + 1, hr + 1):
                cost += rowCosts[r]
        else:
            for r in range(sr - 1, hr - 1, -1):
                cost += rowCosts[r]
        # Move columns
        if sc < hc:
            for c in range(sc + 1, hc + 1):
                cost += colCosts[c]
        else:
            for c in range(sc - 1, hc - 1, -1):
                cost += colCosts[c]
        return cost
