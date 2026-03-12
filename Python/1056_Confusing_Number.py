# Author: Kaustav Ghosh
# 1056. Confusing Number
# https://leetcode.com/problems/confusing-number/

class Solution(object):
    def confusingNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        digits = []
        original = n
        while n > 0:
            d = n % 10
            if d not in mapping:
                return False
            digits.append(mapping[d])
            n //= 10
        rotated = 0
        for d in digits:
            rotated = rotated * 10 + d
        return rotated != original
