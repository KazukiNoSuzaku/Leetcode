# Author: Kaustav Ghosh
# Problem: Maximum Binary String After Change
# Approach: The operations let us push all zeros together and turn all but one into ones; the result is all 1s with a single 0 at index (first_zero + zero_count - 1)

class Solution(object):
    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        if '0' not in binary:
            return binary
        zeros = binary.count('0')
        first = binary.index('0')
        res = ['1'] * len(binary)
        res[first + zeros - 1] = '0'
        return ''.join(res)
