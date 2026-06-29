# Author: Kaustav Ghosh
# Problem: Maximum Number of Coins You Can Get
# Approach: Sort ascending; Bob takes the smallest n piles, then you grab every second pile from the top (the second-largest of each chosen triple)

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles) // 3
        total = 0
        i = len(piles) - 2
        for _ in range(n):
            total += piles[i]
            i -= 2
        return total
