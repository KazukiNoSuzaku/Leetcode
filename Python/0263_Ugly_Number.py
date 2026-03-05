# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

# Example 1:
# Input: n = 6
# Output: true

# Example 2:
# Input: n = 1
# Output: true

# Example 3:
# Input: n = 14
# Output: false

# Constraints:
# -2^31 <= n <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1
