# You are painting a fence of n posts with k different colors. You must paint the posts
# following these rules: Every post must be painted exactly one color.
# There cannot be three or more consecutive posts with the same color.
# Given the two integers n and k, return the number of ways you can paint the fence.

# Example 1:
# Input: n = 3, k = 2
# Output: 6

# Example 2:
# Input: n = 1, k = 1
# Output: 1

# Constraints:
# 1 <= n <= 50
# 1 <= k <= 10^5

# Author: Kaustav Ghosh

class Solution(object):
    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        same = k
        diff = k * (k - 1)
        for _ in range(2, n):
            same, diff = diff, (same + diff) * (k - 1)
        return same + diff
