# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Group by name, flag if amount > 1000 or same name different city within 60 min

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city))

        invalid = set()
        for i in range(len(parsed)):
            if parsed[i][2] > 1000:
                invalid.add(i)
            for j in range(len(parsed)):
                if i != j and parsed[i][0] == parsed[j][0] and \
                   parsed[i][3] != parsed[j][3] and \
                   abs(parsed[i][1] - parsed[j][1]) <= 60:
                    invalid.add(i)

        return [transactions[i] for i in invalid]
