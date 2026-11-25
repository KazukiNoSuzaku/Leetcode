# Author: Kaustav Ghosh
# Problem: Remove Colored Pieces if Both Neighbors are the Same Color
# Approach: A piece may only be taken when both its neighbours match its own colour, so every legal move sits strictly inside a run of identical colours and, crucially, taking it shortens that run by one without ever merging two runs or creating a move in the other colour's runs. That means the two players' move supplies are completely independent and fixed from the start: a run of length L offers exactly L minus two moves to the player owning its colour. Counting the run lengths once gives both totals, and since the players alternate with Alice first, Alice wins precisely when her total exceeds Bob's.

class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        moves = {'A': 0, 'B': 0}
        index = 0
        total = len(colors)
        while index < total:
            end = index
            while end < total and colors[end] == colors[index]:
                end += 1
            length = end - index
            if length > 2:
                moves[colors[index]] += length - 2
            index = end
        return moves['A'] > moves['B']
