# Author: Kaustav Ghosh
# Problem: Minimum Garden Perimeter to Collect Enough Apples
# Approach: A square of radius n contains 2*n*(n+1)*(2n+1) apples (sum of |i|+|j| over the grid). Binary search the smallest n whose total reaches neededApples; the perimeter is 8n

class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        def apples(n):
            return 2 * n * (n + 1) * (2 * n + 1)

        lo, hi = 1, 100000
        while lo < hi:
            mid = (lo + hi) // 2
            if apples(mid) >= neededApples:
                hi = mid
            else:
                lo = mid + 1
        return 8 * lo
