# Author: Kaustav Ghosh
# Problem: Smallest Greater Multiple Made of Two Digits
# Approach: Enumerate numbers whose digits come only from {digit1, digit2}, by increasing length and increasing value. Return the first that exceeds k, is a multiple of k, and fits a 32-bit signed integer; otherwise -1

import itertools

class Solution(object):
    def findInteger(self, k, digit1, digit2):
        """
        :type k: int
        :type digit1: int
        :type digit2: int
        :rtype: int
        """
        LIMIT = 2 ** 31 - 1
        digits = sorted({str(digit1), str(digit2)})
        for length in range(1, 11):
            for combo in itertools.product(digits, repeat=length):
                if combo[0] == '0':
                    continue
                num = int(''.join(combo))
                if num > LIMIT:
                    continue
                if num > k and num % k == 0:
                    return num
        return -1
