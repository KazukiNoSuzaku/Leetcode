# Author: Kaustav Ghosh
# 1033. Moving Stones Until Consecutive
# https://leetcode.com/problems/moving-stones-until-consecutive/

class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        x, y, z = sorted([a, b, c])
        # max moves: move endpoints inward one by one
        max_moves = (y - x - 1) + (z - y - 1)
        # min moves
        if y - x == 1 and z - y == 1:
            min_moves = 0
        elif y - x <= 2 or z - y <= 2:
            min_moves = 1
        else:
            min_moves = 2
        return [min_moves, max_moves]
