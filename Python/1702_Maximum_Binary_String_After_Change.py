# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-binary-string-after-change/

class Solution(object):
    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        n = len(binary)
        zeros = binary.count('0')
        if zeros <= 1:
            return binary
        # Find first zero
        first_zero = binary.index('0')
        # All zeros can be consolidated to one zero at position first_zero + zeros - 1
        # Everything else becomes 1
        result = ['1'] * n
        result[first_zero + zeros - 1] = '0'
        return ''.join(result)
