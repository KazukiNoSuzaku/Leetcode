# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

# Example 1:
# Input: n = 3
# Output: 0

# Example 2:
# Input: n = 5
# Output: 1

# Example 3:
# Input: n = 0
# Output: 0

# Constraints:
# 0 <= n <= 10^4

# Author: Kaustav Ghosh

class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count
