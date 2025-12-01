# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100

# Author: Kaustav Ghosh

class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]
        
        # There is only one way to reach any cell in the first row (by moving right)
        for j in range(n):
            dp[0][j] = 1
        
        # There is only one way to reach any cell in the first column (by moving down)
        for i in range(m):
            dp[i][0] = 1
        
        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                # The number of unique paths to reach cell (i, j) is the sum of
                # the unique paths to reach the cell directly above it and
                # the cell directly to the left of it
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # The bottom-right corner contains the total unique paths from top-left to bottom-right
        return dp[m - 1][n - 1]