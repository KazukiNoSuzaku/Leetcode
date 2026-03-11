# Merge stones by taking K consecutive piles into one. Return minimum total cost,
# or -1 if impossible.

# Author: Kaustav Ghosh

class Solution(object):
    def mergeStones(self, stones, k):
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]
        # dp[i][j] = min cost to merge stones[i..j]
        dp = [[0] * n for _ in range(n)]
        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for m in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j])
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += prefix[j+1] - prefix[i]
        return dp[0][n-1]
