# Author: Kaustav Ghosh
# Problem: 2160. Minimum Sum of Four Digit Number After Splitting Digits
# URL: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
# Approach: Sort digits, pair smallest with largest positions to minimize two 2-digit numbers

class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = sorted(int(d) for d in str(num))
        # digits[0] and digits[1] as tens digits, digits[2] and digits[3] as units
        # to minimize sum: pair smallest two as tens digits
        new1 = digits[0] * 10 + digits[2]
        new2 = digits[1] * 10 + digits[3]
        return new1 + new2
