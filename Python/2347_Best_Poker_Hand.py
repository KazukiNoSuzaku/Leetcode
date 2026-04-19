# Author: Kaustav Ghosh
# 2347. Best Poker Hand
# https://leetcode.com/problems/best-poker-hand/
# Difficulty: Easy
#
# Check for Flush (all same suit), then Three of a Kind, Pair, or High Card.
# Straight is not possible with only 5 cards check per problem constraints.

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
        freq = Counter(ranks)
        max_freq = max(freq.values())
        if max_freq >= 3:
            return "Three of a Kind"
        if max_freq == 2:
            return "Pair"
        return "High Card"
