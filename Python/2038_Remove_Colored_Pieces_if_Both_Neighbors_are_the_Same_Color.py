# Author: Kaustav Ghosh
# Problem: Remove Colored Pieces if Both Neighbors are the Same Color
# Approach: A run of L same-colored pieces gives that player L-2 independent removals (its interior). Alice and Bob's moves don't interfere, so Alice wins exactly when her total interior count exceeds Bob's

from itertools import groupby

class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        alice = bob = 0
        for ch, group in groupby(colors):
            length = len(list(group))
            if length >= 3:
                if ch == 'A':
                    alice += length - 2
                else:
                    bob += length - 2
        return alice > bob
