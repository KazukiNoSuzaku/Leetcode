# Author: Kaustav Ghosh
# Problem: Maximum Height by Stacking Cuboids
# Approach: Since rotation is free, sort each cuboid's dimensions and the whole list; then it reduces to a longest-increasing-subsequence DP on height where a cuboid can sit above another only if all three sorted dims are >=

class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        for c in cuboids:
            c.sort()
        cuboids.sort()

        n = len(cuboids)
        dp = [c[2] for c in cuboids]  # height uses the largest dimension
        best = 0
        for i in range(n):
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0]
                        and cuboids[j][1] <= cuboids[i][1]
                        and cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
            best = max(best, dp[i])
        return best
