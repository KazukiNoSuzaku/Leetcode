# Author: Kaustav Ghosh
# Problem: Minimum Moves to Convert String
# Approach: Each move clears exactly three consecutive characters, so the only decision is where to place the moves, and the leftmost unconverted character must be covered by some move whose window cannot usefully start any earlier than that character itself. Starting the window there covers the most ground still ahead, so scanning left to right and placing a move at every unconverted character encountered, then skipping the three positions that move consumes, is optimal. Characters already satisfactory are simply stepped over one at a time.

class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        moves = 0
        index = 0
        total = len(s)
        while index < total:
            if s[index] == 'X':
                moves += 1
                index += 3
            else:
                index += 1
        return moves
