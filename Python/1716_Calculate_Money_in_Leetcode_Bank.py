# Author: Kaustav Ghosh
# Problem: Calculate Money in Leetcode Bank
# Approach: Week w (0-indexed) deposits w+1..w+7, summing to 7w+28; add the leftover days of the final partial week

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks, days = divmod(n, 7)
        total = 0
        for w in range(weeks):
            total += 7 * w + 28
        for d in range(days):
            total += weeks + 1 + d
        return total
