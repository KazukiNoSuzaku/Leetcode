# Author: Kaustav Ghosh
# Problem: Check if Move is Legal
# Approach: A good line must start at the cell being coloured, so there are only eight candidate lines, one per direction, and each can be tested by walking outwards from the move. Walking in a direction, the cells immediately after the move must all be the opposite colour, and the line is good the moment one of the player's own colour is reached, provided at least one opposite cell was passed, which is the problem's requirement that the line be at least three cells long with only the two endpoints matching the player. Hitting an empty cell or the edge of the board ends that direction with no line. Every direction is at most seven steps, so the whole check is constant work.

class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        other = "W" if color == "B" else "B"
        steps = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for down, across in steps:
            row, column = rMove + down, cMove + across
            passed = 0
            while 0 <= row < 8 and 0 <= column < 8:
                here = board[row][column]
                if here == other:
                    passed += 1
                    row += down
                    column += across
                    continue
                if here == color and passed > 0:
                    return True
                break
        return False
