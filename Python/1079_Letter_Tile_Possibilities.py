# Author: Kaustav Ghosh
# 1079. Letter Tile Possibilities
# https://leetcode.com/problems/letter-tile-possibilities/

from collections import Counter

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        count = Counter(tiles)

        def backtrack():
            total = 0
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    total += 1 + backtrack()
                    count[c] += 1
            return total

        return backtrack()
