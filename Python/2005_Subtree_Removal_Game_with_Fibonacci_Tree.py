# Author: Kaustav Ghosh
# Problem: Subtree Removal Game with Fibonacci Tree
# Approach: Deleting a node removes its whole subtree, and the loser is whoever has no move but the root, which makes this an ordinary impartial game whose position value is the exclusive-or of its two subtrees' values. Working out those values for the Fibonacci trees in turn shows them cycling with period six in the order index: the value collapses to zero exactly when that index leaves remainder one on division by six, and a zero value is precisely a loss for the player about to move. So Alice, moving first, loses only on those orders and wins on every other, which the single remainder test decides outright.

class Solution(object):
    def findGameWinner(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 6 != 1
