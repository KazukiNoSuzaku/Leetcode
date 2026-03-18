# Author: Kaustav Ghosh
# Problem: 1518 - Water Bottles
# Approach: Drink full bottles, exchange empties, repeat

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
            new_bottles = empty // numExchange
            total += new_bottles
            empty = empty % numExchange + new_bottles
        return total
