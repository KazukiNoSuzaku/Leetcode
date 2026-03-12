# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Interval DP - dp[i][j] = min moves to remove arr[i..j]

class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            dp[i][i + 1] = 1 if arr[i] == arr[i + 1] else 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = length  # worst case
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][n - 1]
