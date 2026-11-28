# Author: Kaustav Ghosh
# Problem: Simple Bank System
# Approach: The accounts are numbered consecutively from one, so the balances sit in a plain list indexed one below the account number and every operation is a direct read or write with no searching. Each of the three operations fails for its own reasons and the checks must all pass before anything is written, otherwise a rejected transfer could still have moved money: an account number outside the known range is invalid, and a withdrawal or the outgoing side of a transfer additionally needs a balance that covers the amount. Because the checks are completed first, a failed operation leaves every balance untouched.

class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        self.accounts = len(balance)

    def _exists(self, account):
        return 1 <= account <= self.accounts

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if not self._exists(account1) or not self._exists(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self._exists(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self._exists(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
