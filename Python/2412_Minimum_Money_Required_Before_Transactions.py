# Author: Kaustav Ghosh
# Problem: Minimum Money Required Before Transactions
# Approach: A transaction whose cost exceeds its cashback drains max(cost - cashback, 0) overall, and the worst ordering runs every other transaction first before demanding one transaction's full cost up front. So total all the net losses and, for each transaction in turn, swap its own loss for its full cost, keeping the largest requirement

class Solution(object):
    def minimumMoney(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        total = sum(max(cost - cashback, 0) for cost, cashback in transactions)
        return max(total - max(cost - cashback, 0) + cost for cost, cashback in transactions)
