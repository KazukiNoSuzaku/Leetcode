# Author: Kaustav Ghosh
# Problem: Game of Nim
# Approach: This is ordinary Nim, and its theory says the player to move loses exactly when the XOR of all the pile sizes is zero. The reason is that from a non-zero XOR some pile can always be reduced to make the XOR zero, handing the losing position to the opponent, while from a zero XOR every move necessarily breaks it; the all-empty position has XOR zero and is a loss for whoever faces it, which anchors the induction. So Alice wins precisely when the XOR of the piles is not zero, which answers the problem's own follow-up about a linear solution without any search over positions.

class Solution(object):
    def nimGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        total = 0
        for pile in piles:
            total ^= pile
        return total != 0
