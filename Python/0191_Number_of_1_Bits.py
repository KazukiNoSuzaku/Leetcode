# Given a positive integer n, write a function that returns the number of set bits in its binary representation
# (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation: The input binary representation of 11 is 00000000000000000000000000001011, so the return value is 3.

# Example 2:
# Input: n = 128
# Output: 1

# Example 3:
# Input: n = 2147483645
# Output: 30

# Constraints:
# 1 <= n <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
