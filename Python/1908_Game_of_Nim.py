# Author: Kaustav Ghosh
# Problem: Game of Nim
# Approach: Classic Nim - the player to move loses exactly when the XOR (nim-sum) of all pile sizes is zero. Alice moves first, so she wins iff the nim-sum is nonzero

class Solution(object):
    def nimGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        nim_sum = 0
        for p in piles:
            nim_sum ^= p
        return nim_sum != 0
