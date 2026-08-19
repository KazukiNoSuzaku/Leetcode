# Author: Kaustav Ghosh
# Problem: Two Furthest Houses With Different Colors
# Approach: The optimal pair must involve one of the two endpoints. Find the farthest house differing from the first, and the farthest differing from the last, and take the larger distance

class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        best = 0
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                best = max(best, j)
                break
        for i in range(n):
            if colors[i] != colors[n - 1]:
                best = max(best, n - 1 - i)
                break
        return best
