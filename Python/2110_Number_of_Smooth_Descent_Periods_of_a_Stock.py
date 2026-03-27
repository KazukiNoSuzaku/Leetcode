# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        result = 1
        length = 1
        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                length += 1
            else:
                length = 1
            result += length
        return result
