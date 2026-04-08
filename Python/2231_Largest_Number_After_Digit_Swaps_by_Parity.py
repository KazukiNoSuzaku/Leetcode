# Author: Kaustav Ghosh
# Problem: 2231. Largest Number After Digit Swaps by Parity
# URL: https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
# Difficulty: Easy
#
# Approach:
# Separate digits into odd and even groups, sort each in descending order.
# Rebuild the number by replacing each digit with the largest available
# digit of the same parity.

class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(d) for d in str(num)]
        odds = sorted([d for d in digits if d % 2 == 1], reverse=True)
        evens = sorted([d for d in digits if d % 2 == 0], reverse=True)
        oi = 0
        ei = 0
        result = []
        for d in digits:
            if d % 2 == 1:
                result.append(odds[oi])
                oi += 1
            else:
                result.append(evens[ei])
                ei += 1
        return int(''.join(str(x) for x in result))
