# Author: Kaustav Ghosh
# Problem 2078: Two Furthest Houses With Different Colors

class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        ans = 0
        # Check from left end
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                ans = max(ans, i)
                break
        # Check from right end
        for i in range(n):
            if colors[i] != colors[n - 1]:
                ans = max(ans, n - 1 - i)
                break
        return ans
