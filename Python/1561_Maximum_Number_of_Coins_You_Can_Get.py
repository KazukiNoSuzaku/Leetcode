# Author: Kaustav Ghosh
# Problem: Maximum Number of Coins You Can Get
# Approach: Alice always claims the largest pile of whichever triple is chosen and Bob the smallest, so my take is the middle one; sorting and then repeatedly pairing the two biggest remaining piles with the smallest leftover pile means every triple costs me only one tiny pile, and the second-largest of each such triple is exactly every other pile counting down from the top, so after sorting I sum indices n, n+2, n+4, ... where n is the number of triples.

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles) // 3
        return sum(piles[n::2])
