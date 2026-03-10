# Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10^n.

# Example 1:
# Input: n = 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 <= x < 100,
# excluding 11,22,33,44,55,66,77,88,99

# Example 2:
# Input: n = 0
# Output: 1

# Constraints:
# 0 <= n <= 8

# Author: Kaustav Ghosh

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        res = 10
        unique = 9
        available = 9
        for i in range(2, n + 1):
            unique *= available
            res += unique
            available -= 1
        return res
