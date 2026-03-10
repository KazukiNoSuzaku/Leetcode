# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0,1,1]

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]

# Constraints:
# 0 <= n <= 10^5

# Author: Kaustav Ghosh

class Solution(object):
    def countBits(self, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
