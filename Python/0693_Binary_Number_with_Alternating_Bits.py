# Check if the binary representation of n has alternating bits.

# Author: Kaustav Ghosh

class Solution(object):
    def hasAlternatingBits(self, n):
        prev = n & 1
        n >>= 1
        while n:
            cur = n & 1
            if cur == prev: return False
            prev = cur
            n >>= 1
        return True
