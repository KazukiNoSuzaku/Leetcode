# Author: Kaustav Ghosh
# Problem: Number of Ways to Buy Pens and Pencils
# Approach: Iterate over the number of pens that fit within the budget; for each, the remaining money allows (remaining // cost2) + 1 choices of pencils (including buying zero). Sum these counts

class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        ways = 0
        pens = 0
        while pens * cost1 <= total:
            remaining = total - pens * cost1
            ways += remaining // cost2 + 1
            pens += 1
        return ways
