# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        # For a square garden of side length 2n, total apples = 2*n*(n+1)*(2*n+1)
        n = 1
        while 2 * n * (n + 1) * (2 * n + 1) < neededApples:
            n += 1
        return 8 * n
