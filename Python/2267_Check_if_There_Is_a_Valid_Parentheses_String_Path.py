# Author: Kaustav Ghosh
# Problem: 2267. Check if There Is a Valid Parentheses String Path
# URL: https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
# Difficulty: Hard
#
# Approach:
# DP/DFS with memoization. State is (row, col, open_count). Move right or down.
# '(' increments open_count, ')' decrements. Prune if open_count < 0.
# Valid if we reach (m-1, n-1) with open_count == 0.

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

        memo = set()

        def dfs(r, c, count):
            if count < 0 or count > (m - 1 - r) + (n - 1 - c):
                return False
            if (r, c, count) in memo:
                return False
            if r == m - 1 and c == n - 1:
                return count == 0
            memo.add((r, c, count))
            for nr, nc in ((r + 1, c), (r, c + 1)):
                if nr < m and nc < n:
                    delta = 1 if grid[nr][nc] == '(' else -1
                    if dfs(nr, nc, count + delta):
                        return True
            return False

        return dfs(0, 0, 1)
