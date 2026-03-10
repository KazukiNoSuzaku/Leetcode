# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize
# the product of those integers. Return the maximum product you can get.

# Example 1:
# Input: n = 2
# Output: 1

# Example 2:
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 * 3 * 4 = 36.

# Constraints:
# 2 <= n <= 58

# Author: Kaustav Ghosh

class Solution(object):
    def integerBreak(self, n):
        if n == 2: return 1
        if n == 3: return 2
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        return product * n
