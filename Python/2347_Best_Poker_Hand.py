# Author: Kaustav Ghosh
# Problem: Best Poker Hand
# Approach: Check hands from best to worst: five matching suits is a Flush; otherwise the highest count of any rank decides between Three of a Kind (3 or more), Pair (2) and High Card

from collections import Counter


class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        if len(set(suits)) == 1:
            return "Flush"
        most = max(Counter(ranks).values())
        if most >= 3:
            return "Three of a Kind"
        if most == 2:
            return "Pair"
        return "High Card"
