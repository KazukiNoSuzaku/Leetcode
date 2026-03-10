# Given two integers a and b, return the sum of the two integers without using the
# operators + and -.

# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = 2, b = 3
# Output: 5

# Constraints:
# -1000 <= a, b <= 1000

# Author: Kaustav Ghosh

class Solution(object):
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        # handle negative numbers in Python's arbitrary precision
        if b == 0:
            return a & mask if a > 0xFFFFFFFF // 2 else a
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
