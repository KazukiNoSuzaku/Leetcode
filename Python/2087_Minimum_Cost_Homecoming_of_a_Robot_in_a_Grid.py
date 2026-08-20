# Author: Kaustav Ghosh
# Problem: Minimum Cost Homecoming of a Robot in a Grid
# Approach: The robot only needs to move toward home; each step into a new row or column pays that row/column cost. Summing the costs of every row and column entered between start and home (exclusive of the start) is optimal since detours only add cost

class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        sr, sc = startPos
        hr, hc = homePos
        total = 0
        step = 1 if hr >= sr else -1
        for r in range(sr + step, hr + step, step):
            total += rowCosts[r]
        step = 1 if hc >= sc else -1
        for c in range(sc + step, hc + step, step):
            total += colCosts[c]
        return total
