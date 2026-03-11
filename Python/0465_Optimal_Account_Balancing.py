# You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti].
# Given a list of transactions between a group of people, return the minimum number of
# transactions required to settle the debt.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def minTransfers(self, transactions):
        balance = defaultdict(int)
        for f, t, a in transactions:
            balance[f] -= a
            balance[t] += a
        debts = [v for v in balance.values() if v != 0]

        def dfs(start):
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts):
                return 0
            res = float('inf')
            for i in range(start + 1, len(debts)):
                if debts[i] * debts[start] < 0:
                    debts[i] += debts[start]
                    res = min(res, 1 + dfs(start + 1))
                    debts[i] -= debts[start]
            return res

        return dfs(0)
