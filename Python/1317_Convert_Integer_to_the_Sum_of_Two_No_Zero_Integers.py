# Find two integers A and B with no zero digit such that A + B = n.

# Author: Kaustav Ghosh

class Solution(object):
    def getNoZeroIntegers(self, n):
        def no_zero(x):
            while x:
                if x % 10 == 0: return False
                x //= 10
            return True
        for a in range(1, n):
            if no_zero(a) and no_zero(n - a):
                return [a, n - a]
