# An n-bit gray code sequence is a sequence of 2^n integers where:
# - Every integer is in the inclusive range [0, 2^n - 1]
# - The first integer is 0
# - An integer appears no more than once in the sequence
# - The binary representation of every pair of adjacent integers differs by exactly one bit
# Given an integer n, return any valid n-bit gray code sequence.

# Example 1:
# Input: n = 2
# Output: [0,1,3,2]

# Example 2:
# Input: n = 1
# Output: [0,1]

# Constraints:
# 1 <= n <= 16

# Author: Kaustav Ghosh

class Solution(object):
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(1 << n)]
