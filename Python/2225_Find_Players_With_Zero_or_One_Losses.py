# Author: Kaustav Ghosh
# Problem: 2225. Find Players With Zero or One Losses
# URL: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
# Difficulty: Medium
#
# Approach:
# Count losses for each player using a dictionary. Players who never appear
# as a loser have zero losses; track all players seen. Return sorted lists
# of those with exactly 0 and exactly 1 loss.

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        losses = {}
        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            losses[loser] = losses.get(loser, 0) + 1

        no_loss = sorted([p for p, l in losses.items() if l == 0])
        one_loss = sorted([p for p, l in losses.items() if l == 1])
        return [no_loss, one_loss]
