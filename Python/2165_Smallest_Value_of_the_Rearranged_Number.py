# Author: Kaustav Ghosh
# Problem: Smallest Value of the Rearranged Number
# Approach: For a negative number, the smallest value uses digits in descending order (largest magnitude). For a positive number, sort digits ascending but move the first non-zero digit to the front to avoid a leading zero

class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        if num < 0:
            digits = sorted(str(-num), reverse=True)
            return -int(''.join(digits))
        digits = sorted(str(num))
        if digits[0] == '0':
            j = next(i for i, d in enumerate(digits) if d != '0')
            digits[0], digits[j] = digits[j], digits[0]
        return int(''.join(digits))
