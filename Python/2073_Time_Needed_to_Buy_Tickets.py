# Author: Kaustav Ghosh
# Problem: Time Needed to Buy Tickets
# Approach: Person k needs tickets[k] passes. Everyone at or before k contributes up to tickets[k] buys; everyone after k contributes up to tickets[k]-1 (they get one fewer pass before k finishes). Sum those capped amounts

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        target = tickets[k]
        total = 0
        for i, t in enumerate(tickets):
            if i <= k:
                total += min(t, target)
            else:
                total += min(t, target - 1)
        return total
