# Author: Kaustav Ghosh
# Problem: 2241. Design an ATM Machine
# URL: https://leetcode.com/problems/design-an-atm-machine/
# Difficulty: Medium
#
# Approach:
# Maintain counts of each denomination. On withdraw, greedily take from
# the largest denomination first. If the exact amount cannot be formed,
# return [-1, -1, -1, -1, -1] without modifying state.

class Solution(object):
    pass

class ATM(object):

    def __init__(self):
        self.bills = [0] * 5
        self.denoms = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i in range(5):
            self.bills[i] += banknotesCount[i]

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        result = [0] * 5
        for i in range(4, -1, -1):
            count = min(self.bills[i], amount // self.denoms[i])
            result[i] = count
            amount -= count * self.denoms[i]
        if amount != 0:
            return [-1, -1, -1, -1, -1]
        for i in range(5):
            self.bills[i] -= result[i]
        return result
