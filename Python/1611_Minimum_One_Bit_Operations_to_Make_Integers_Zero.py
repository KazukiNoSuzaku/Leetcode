# Author: Kaustav Ghosh
# Problem: Minimum One Bit Operations to Make Integers Zero
# Approach: The allowed moves are exactly Gray-code steps, so n is a Gray code and the answer is its inverse (Gray -> binary via cumulative XOR)

class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res ^= n
            n >>= 1
        return res
