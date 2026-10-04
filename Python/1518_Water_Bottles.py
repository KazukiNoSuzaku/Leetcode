# Author: Kaustav Ghosh
# Problem: Water Bottles
# Approach: Drink everything on hand, then keep trading empties for full bottles while enough empties remain, remembering that each bottle drunk leaves another empty behind

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drunk = numBottles
        empty = numBottles
        while empty >= numExchange:
            traded = empty // numExchange
            drunk += traded
            empty = empty % numExchange + traded
        return drunk
