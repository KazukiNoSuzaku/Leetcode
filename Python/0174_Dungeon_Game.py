# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon.
# The knight starts in the top-left room and needs to rescue the princess.
# Each room has an integer value (negative for demon-infested, positive for magic orbs).
# The knight's health drops to 0 or below at any point means death.
# Determine the knight's minimum initial health to rescue the princess.

# Example 1:
# Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Output: 7

# Example 2:
# Input: dungeon = [[0]]
# Output: 1

# Constraints:
# m == dungeon.length, n == dungeon[i].length
# 1 <= m, n <= 200
# -1000 <= dungeon[i][j] <= 1000

# Author: Kaustav Ghosh

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                elif i == m - 1:
                    dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
                elif j == n - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]
