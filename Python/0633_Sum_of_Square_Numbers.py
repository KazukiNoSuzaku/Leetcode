# Given a non-negative integer c, decide whether there are integers a, b such that a^2 + b^2 = c.

# Author: Kaustav Ghosh

import math

class Solution(object):
    def judgeSquareSum(self, c):
        a = 0
        while a * a <= c:
            b = math.sqrt(c - a * a)
            if b == int(b):
                return True
            a += 1
        return False
