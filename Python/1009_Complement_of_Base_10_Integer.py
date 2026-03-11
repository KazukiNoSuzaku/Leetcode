# Return the complement of a non-negative integer n (flip all bits in binary representation).

# Author: Kaustav Ghosh

class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0: return 1
        mask = 1
        while mask <= n:
            mask <<= 1
        return (mask - 1) ^ n
