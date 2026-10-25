# Author: Kaustav Ghosh
# Problem: Maximum Binary String After Change
# Approach: The two moves together let any zero be walked rightwards past a one, and let two adjacent zeros be collapsed into a one followed by a zero, so every zero but one can eventually be consumed and the survivor can be pushed as far right as the zeros allow. Working out where it lands needs no simulation: the leading ones are untouchable, and the remaining zeros collapse so that the single surviving zero sits just past the block of ones they became, which places it at the first zero's index plus the number of zeros, less one. A string with no zeros at all is already maximal and is returned unchanged.

class Solution(object):
    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        zeros = binary.count('0')
        if zeros <= 1:
            return binary
        first = binary.index('0')
        n = len(binary)
        hole = first + zeros - 1
        return '1' * hole + '0' + '1' * (n - hole - 1)
