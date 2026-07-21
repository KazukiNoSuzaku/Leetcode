# Author: Kaustav Ghosh
# Problem: Maximum Number of Consecutive Values You Can Make
# Approach: Sort coins; if we can already form [0, reach), a coin c <= reach extends the range to reach + c, otherwise there is a gap and we stop

class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        reach = 1  # can currently make every value in [0, reach)
        for c in sorted(coins):
            if c > reach:
                break
            reach += c
        return reach
