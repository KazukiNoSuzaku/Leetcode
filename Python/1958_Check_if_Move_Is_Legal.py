# Author: Kaustav Ghosh
# Problem: Check if Move Is Legal
# Approach: From the placed cell, look in all 8 directions. A direction gives a good line if it starts with one or more opposite-colored cells and then hits a same-colored cell (line length >= 3), with no empty cell in between

class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        opp = 'B' if color == 'W' else 'W'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = rMove + dr, cMove + dc
            count = 0
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opp:
                count += 1
                r += dr
                c += dc
            if count >= 1 and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == color:
                return True
        return False
