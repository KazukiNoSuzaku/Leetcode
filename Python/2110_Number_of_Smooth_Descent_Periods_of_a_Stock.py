# Author: Kaustav Ghosh
# Problem: Number of Smooth Descent Periods of a Stock
# Approach: Track the length of the current run where each day is exactly one less than the previous. Each day contributes that run length to the count of valid subarrays ending there

class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        run = 0
        for i, p in enumerate(prices):
            if i > 0 and prices[i - 1] - p == 1:
                run += 1
            else:
                run = 1
            total += run
        return total
