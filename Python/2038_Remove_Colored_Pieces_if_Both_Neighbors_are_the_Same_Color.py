# Author: Kaustav Ghosh
# Problem 2038: Remove Colored Pieces if Both Neighbors are the Same Color

class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        alice = 0
        bob = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    alice += 1
                else:
                    bob += 1
        return alice > bob
