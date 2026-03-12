# Author: Kaustav Ghosh
# Minimax DP: player takes 1..2M piles, maximize own stones

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        # suffix sums
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            if i >= n:
                return 0
            if (i, m) in memo:
                return memo[(i, m)]
            if i + 2 * m >= n:
                memo[(i, m)] = suffix[i]
                return suffix[i]
            best = 0
            for x in range(1, 2 * m + 1):
                best = max(best, suffix[i] - dp(i + x, max(m, x)))
            memo[(i, m)] = best
            return best

        return dp(0, 1)
