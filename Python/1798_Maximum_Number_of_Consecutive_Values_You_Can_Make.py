# Author: Kaustav Ghosh
# Problem: Maximum Number of Consecutive Values You Can Make
# Approach: Suppose every value from zero up to some reach is already obtainable. A further coin of value c extends that run to reach plus c exactly when c is no larger than reach plus one, because then the coin lands inside or immediately after the covered range and leaves no hole; if c is bigger the gap at reach plus one can never be filled by it or by any larger coin. Sorting the coins and taking them in order therefore settles the answer in one sweep, and the count includes zero itself.

class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        reach = 0
        for coin in sorted(coins):
            if coin > reach + 1:
                break
            reach += coin
        return reach + 1
