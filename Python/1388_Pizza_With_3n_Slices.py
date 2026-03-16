# Author: Kaustav Ghosh
# Problem: Pizza With 3n Slices
# Approach: DP pick max sum of n non-adjacent elements from circular array

class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        def solve(arr, picks):
            n = len(arr)
            dp = [[-float('inf')] * (picks + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                dp[i][0] = 0
            for i in range(1, n + 1):
                for j in range(1, picks + 1):
                    dp[i][j] = dp[i - 1][j]
                    if i >= 2:
                        dp[i][j] = max(dp[i][j], dp[i - 2][j - 1] + arr[i - 1])
                    elif j == 1:
                        dp[i][j] = max(dp[i][j], arr[i - 1])
            return dp[n][picks]

        n = len(slices) // 3
        return max(solve(slices[1:], n), solve(slices[:-1], n))
