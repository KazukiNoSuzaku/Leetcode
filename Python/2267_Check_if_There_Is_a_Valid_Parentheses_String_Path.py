# Author: Kaustav Ghosh
# Problem: Check if There Is a Valid Parentheses String Path
# Approach: DP over the set of reachable running balances (open minus close) at each cell, moving only right or down. '(' adds one, ')' subtracts one, and a balance may never go negative. A path is valid if balance 0 is reachable at the bottom-right cell. The path length must be even, else it is impossible

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # dp[c] = set of reachable balances at current row, column c
        dp = [set() for _ in range(n)]
        for r in range(m):
            ndp = [set() for _ in range(n)]
            for c in range(n):
                delta = 1 if grid[r][c] == '(' else -1
                incoming = set()
                if r == 0 and c == 0:
                    incoming.add(0)
                else:
                    if r > 0:
                        incoming |= dp[c]        # from above (previous row)
                    if c > 0:
                        incoming |= ndp[c - 1]   # from left (current row)
                for bal in incoming:
                    nb = bal + delta
                    if nb >= 0:
                        ndp[c].add(nb)
            dp = ndp
        return 0 in dp[n - 1]
