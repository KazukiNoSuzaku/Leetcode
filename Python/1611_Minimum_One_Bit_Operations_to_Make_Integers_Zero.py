# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Gray code inverse: convert from Gray code to binary
        result = 0
        while n:
            result ^= n
            n >>= 1
        return result
