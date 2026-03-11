# Return the representation of integer n in base -2.

# Author: Kaustav Ghosh

class Solution(object):
    def baseNeg2(self, n):
        if n == 0: return '0'
        bits = []
        while n != 0:
            bits.append(n & 1)
            n = -(n >> 1)
        return ''.join(map(str, reversed(bits)))
