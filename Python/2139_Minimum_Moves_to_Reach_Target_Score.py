# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        moves = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            moves += 1
        # Remaining distance is covered by increments
        moves += target - 1
        return moves
