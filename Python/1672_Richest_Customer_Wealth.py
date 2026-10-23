# Author: Kaustav Ghosh
# Problem: Richest Customer Wealth
# Approach: Each customer's wealth is independent of the others, so a single pass taking the largest row total answers it; there is nothing to sort and no need to keep the individual totals once the running maximum is known.

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(sum(customer) for customer in accounts)
