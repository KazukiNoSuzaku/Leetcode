# Author: Kaustav Ghosh

class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        reach = 0
        for c in coins:
            if c > reach + 1:
                break
            reach += c
        return reach + 1
