# Author: Kaustav Ghosh
# https://leetcode.com/problems/check-if-move-is-legal/

class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            r, c = rMove + dr, cMove + dc
            length = 1
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == '.':
                    break
                if board[r][c] == color:
                    if length >= 2:
                        return True
                    break
                r += dr
                c += dc
                length += 1
        return False
