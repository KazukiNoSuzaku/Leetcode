# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.

# Example 1:
# Input: n = 1
# Output: true

# Example 2:
# Input: n = 16
# Output: true

# Example 3:
# Input: n = 3
# Output: false

# Constraints:
# -2^31 <= n <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
