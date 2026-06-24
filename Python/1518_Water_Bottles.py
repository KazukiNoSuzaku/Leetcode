# Author: Kaustav Ghosh
# Problem: Water Bottles
# Approach: Simulate — drink all full bottles, exchange empties for new full ones until not enough empties

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles
        while empty >= numExchange:
            new_full = empty // numExchange
            total += new_full
            empty = new_full + (empty % numExchange)
        return total
