# Author: Kaustav Ghosh
# Problem: 2280. Minimum Lines to Represent a Line Chart
# URL: https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/
# Difficulty: Medium
#
# Approach:
# Sort by day. Compare slopes using cross multiplication to avoid floating point.
# Count line segments where slope changes.

class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        if len(stockPrices) <= 1:
            return 0
        stockPrices.sort()
        lines = 1
        for i in range(2, len(stockPrices)):
            dx1 = stockPrices[i][0] - stockPrices[i - 1][0]
            dy1 = stockPrices[i][1] - stockPrices[i - 1][1]
            dx2 = stockPrices[i - 1][0] - stockPrices[i - 2][0]
            dy2 = stockPrices[i - 1][1] - stockPrices[i - 2][1]
            if dy1 * dx2 != dy2 * dx1:
                lines += 1
        return lines
