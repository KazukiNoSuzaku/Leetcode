# Author: Kaustav Ghosh
# Problem: 1561 - Maximum Number of Coins You Can Get
# Approach: Sort, skip smallest third, sum every second element from 1/3 to end

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles) // 3
        result = 0
        i = len(piles) - 2
        while n > 0:
            result += piles[i]
            i -= 2
            n -= 1
        return result
