# Author: Kaustav Ghosh
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        # Generate all valid column colorings (no two adjacent same color)
        def gen_columns(m):
            if m == 1:
                return [[0], [1], [2]]
            result = []
            for prev in gen_columns(m - 1):
                for c in range(3):
                    if c != prev[-1]:
                        result.append(prev + [c])
            return result

        columns = gen_columns(m)
        num_cols = len(columns)

        # Check if two columns are compatible (no same color in same row)
        def compatible(c1, c2):
            return all(c1[i] != c2[i] for i in range(m))

        # Precompute compatibility
        compat = [[] for _ in range(num_cols)]
        for i in range(num_cols):
            for j in range(num_cols):
                if compatible(columns[i], columns[j]):
                    compat[i].append(j)

        # DP
        dp = [1] * num_cols
        for _ in range(1, n):
            new_dp = [0] * num_cols
            for j in range(num_cols):
                for i in compat[j]:
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD
