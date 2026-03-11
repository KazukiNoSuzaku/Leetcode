# Given a string expression representing an expression of fraction addition and subtraction,
# return the calculation result in string format.

# Author: Kaustav Ghosh

from math import gcd
import re

class Solution(object):
    def fractionAddition(self, expression):
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        num, den = 0, 1
        for i in range(0, len(nums), 2):
            n, d = nums[i], nums[i+1]
            num = num * d + n * den
            den = den * d
            g = gcd(abs(num), abs(den))
            num //= g; den //= g
        return '%d/%d' % (num, den)
