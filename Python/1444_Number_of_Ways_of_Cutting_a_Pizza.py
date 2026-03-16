# Author: Kaustav Ghosh
# Problem: Number of Ways of Cutting a Pizza (Premium)
# Approach: DP with prefix sum of apples, cut horizontally or vertically

class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        # prefix[i][j] = number of apples in subgrid from (i,j) to (m-1,n-1)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prefix[i][j] = (prefix[i + 1][j] + prefix[i][j + 1]
                                - prefix[i + 1][j + 1]
                                + (1 if pizza[i][j] == 'A' else 0))

        memo = {}

        def dp(r, c, cuts):
            if cuts == 0:
                return 1 if prefix[r][c] > 0 else 0
            if (r, c, cuts) in memo:
                return memo[(r, c, cuts)]
            result = 0
            # Horizontal cut
            for i in range(r + 1, m):
                if prefix[r][c] - prefix[i][c] > 0:
                    result = (result + dp(i, c, cuts - 1)) % MOD
            # Vertical cut
            for j in range(c + 1, n):
                if prefix[r][c] - prefix[r][j] > 0:
                    result = (result + dp(r, j, cuts - 1)) % MOD
            memo[(r, c, cuts)] = result
            return result

        return dp(0, 0, k - 1)
