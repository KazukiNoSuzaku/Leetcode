# Author: Kaustav Ghosh
# Problem: Design an ATM Machine
# Approach: Track how many notes of each denomination (20, 50, 100, 200, 500) are held. Deposits add to the counts. Withdrawals greedily use the largest denominations first; compute the plan against a copy of the counts and only commit (returning the note breakdown) if the exact amount can be dispensed, otherwise report failure

class ATM(object):
    def __init__(self):
        self.denoms = [20, 50, 100, 200, 500]
        self.counts = [0] * 5

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i in range(5):
            self.counts[i] += banknotesCount[i]

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        plan = [0] * 5
        for i in range(4, -1, -1):
            take = min(amount // self.denoms[i], self.counts[i])
            plan[i] = take
            amount -= take * self.denoms[i]
        if amount != 0:
            return [-1]
        for i in range(5):
            self.counts[i] -= plan[i]
        return plan
