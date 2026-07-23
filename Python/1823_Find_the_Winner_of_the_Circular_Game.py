# Author: Kaustav Ghosh
# Problem: Find the Winner of the Circular Game
# Approach: Josephus recurrence — the survivor's 0-indexed position grows as (prev + k) mod i as the circle rebuilds; add 1 for 1-indexing

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        winner = 0
        for size in range(2, n + 1):
            winner = (winner + k) % size
        return winner + 1
