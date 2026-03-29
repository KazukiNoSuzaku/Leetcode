# Author: Kaustav Ghosh
# Problem: 2165. Smallest Value of the Rearranged Number
# URL: https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
# Difficulty: Medium

class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        digits = sorted(str(abs(num)))
        if num > 0:
            # Move first non-zero digit to front
            for i, d in enumerate(digits):
                if d != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break
            return int(''.join(digits))
        else:
            # Sort descending for negative
            return -int(''.join(sorted(digits, reverse=True)))
