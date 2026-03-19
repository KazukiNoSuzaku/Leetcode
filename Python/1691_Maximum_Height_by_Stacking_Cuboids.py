# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        # Sort each cuboid dimensions, then sort all cuboids
        for c in cuboids:
            c.sort()
        cuboids.sort()

        n = len(cuboids)
        dp = [c[2] for c in cuboids]

        for i in range(1, n):
            for j in range(i):
                if cuboids[j][0] <= cuboids[i][0] and cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        return max(dp)
