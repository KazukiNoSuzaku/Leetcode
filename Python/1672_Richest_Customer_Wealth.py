# Author: Kaustav Ghosh
# Problem: Richest Customer Wealth
# Approach: Each customer's wealth is their row sum; return the largest

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(sum(row) for row in accounts)
