# Author: Kaustav Ghosh
# Problem: Stone Game VIII
# Approach: A move always replaces a prefix by its sum, so the state after any number of moves is fully described by how far into the prefix sums the game has reached; the player to move picks some position from there onwards and scores that prefix sum. Writing the score difference from the mover's point of view, choosing position j gives that prefix sum minus whatever the opponent can then achieve from j onwards, so the best play at a position is the better of taking it now or deferring. Sweeping the prefix sums from the back keeps that single running value, which makes the whole game one linear pass rather than a search over moves.

class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        from itertools import accumulate

        prefix = list(accumulate(stones))
        best = prefix[-1]
        for index in range(len(stones) - 2, 0, -1):
            candidate = prefix[index] - best
            if candidate > best:
                best = candidate
        return best
