# Author: Kaustav Ghosh
# Problem 1869: Longer Contiguous Segments of Ones than Zeros

class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        max_ones = max_zeros = 0
        curr_ones = curr_zeros = 0
        for c in s:
            if c == '1':
                curr_ones += 1
                curr_zeros = 0
            else:
                curr_zeros += 1
                curr_ones = 0
            max_ones = max(max_ones, curr_ones)
            max_zeros = max(max_zeros, curr_zeros)
        return max_ones > max_zeros
