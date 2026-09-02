# Author: Kaustav Ghosh
# Problem: Find Players With Zero or One Losses
# Approach: Tally each player's loss count from the matches (winners start at zero losses). Players with zero losses are those who appear but never lost; players with exactly one loss are those whose tally is one. Return both lists sorted

from collections import defaultdict


class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        losses = defaultdict(int)
        for winner, loser in matches:
            losses.setdefault(winner, 0)
            losses[loser] += 1

        zero = sorted(p for p, l in losses.items() if l == 0)
        one = sorted(p for p, l in losses.items() if l == 1)
        return [zero, one]
