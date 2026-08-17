# Author: Kaustav Ghosh
# Problem: Simple Bank System
# Approach: Keep balances in a 1-indexed list. Each operation first validates account numbers (and sufficient funds for outgoing money) before applying the change, returning whether it succeeded

class Bank(object):
    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        self.n = len(balance)

    def _valid(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1, account2, money):
        """
        :rtype: bool
        """
        if not (self._valid(account1) and self._valid(account2)):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        """
        :rtype: bool
        """
        if not self._valid(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :rtype: bool
        """
        if not self._valid(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
