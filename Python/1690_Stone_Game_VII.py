# Author: Kaustav Ghosh
# https://leetcode.com/problems/stone-game-vii/

class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        def range_sum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    range_sum(i + 1, j) - dp[i + 1][j],
                    range_sum(i, j - 1) - dp[i][j - 1]
                )
        return dp[0][n - 1]
