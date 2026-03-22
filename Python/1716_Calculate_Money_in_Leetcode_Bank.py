# Author: Kaustav Ghosh
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        weeks = n // 7
        days = n % 7
        # Sum of full weeks: each week i (0-indexed) contributes 28 + 7*i
        total = 28 * weeks + 7 * weeks * (weeks - 1) // 2
        # Remaining days: start value is weeks + 1
        start = weeks + 1
        total += days * start + days * (days - 1) // 2
        return total
