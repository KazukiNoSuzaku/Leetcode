# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer.

# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# Constraints:
# 1 <= n <= 10^4

# Author: Kaustav Ghosh

class Solution(object):
    def numSquares(self, n):
        dp = list(range(n + 1))
        i = 1
        while i * i <= n:
            sq = i * i
            for j in range(sq, n + 1):
                dp[j] = min(dp[j], dp[j - sq] + 1)
            i += 1
        return dp[n]
