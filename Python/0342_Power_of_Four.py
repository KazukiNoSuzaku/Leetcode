# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4^x.

# Example 1:
# Input: n = 16
# Output: true

# Example 2:
# Input: n = 5
# Output: false

# Constraints:
# -2^31 <= n <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def isPowerOfFour(self, n):
        # n must be positive, a power of 2, and the single set bit must be at an even position
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0
